"""
TruthLens AI - SQLite Database Layer
Stores metadata, classifications, and audit logs for media analysis without persisting sensitive raw media.
"""

import sqlite3
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "truthlens.db")


def get_connection():
    """Create or connect to SQLite database with foreign keys and dict-like row support."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the schema for TruthLens AI analysis history."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analyses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                analysis_code TEXT UNIQUE NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                media_type TEXT NOT NULL,
                content_summary TEXT NOT NULL,
                model_name TEXT NOT NULL,
                prediction TEXT NOT NULL,
                confidence REAL NOT NULL,
                status TEXT NOT NULL,
                metadata_json TEXT
            )
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_analyses_timestamp ON analyses(timestamp DESC);
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_analyses_media_type ON analyses(media_type);
        """)
        conn.commit()


def insert_analysis(
    media_type: str,
    content_summary: str,
    model_name: str,
    prediction: str,
    confidence: float,
    status: str = "COMPLETED",
    metadata: Optional[Dict[str, Any]] = None
) -> str:
    """
    Insert a new analysis record and return its unique tracking code.
    """
    init_db()
    now_str = datetime.now().strftime("%Y%m%d%H%M%S")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM analyses")
        count = cursor.fetchone()[0] + 1
        analysis_code = f"TL-{media_type[:3].upper()}-{now_str[-6:]}-{count:04d}"
        
        meta_str = json.dumps(metadata or {})
        cursor.execute("""
            INSERT INTO analyses (
                analysis_code, timestamp, media_type, content_summary,
                model_name, prediction, confidence, status, metadata_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            analysis_code,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            media_type,
            content_summary[:300],  # Truncate summary for audit efficiency
            model_name,
            prediction,
            float(confidence),
            status,
            meta_str
        ))
        conn.commit()
        return analysis_code


def get_all_analyses(
    media_type: Optional[str] = None,
    search_query: Optional[str] = None,
    limit: Optional[int] = 100
) -> List[Dict[str, Any]]:
    """Retrieve filtered analyses."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM analyses WHERE 1=1"
        params = []
        
        if media_type and media_type != "All":
            query += " AND media_type = ?"
            params.append(media_type)
            
        if search_query and search_query.strip():
            query += " AND (content_summary LIKE ? OR model_name LIKE ? OR analysis_code LIKE ?)"
            wildcard = f"%{search_query.strip()}%"
            params.extend([wildcard, wildcard, wildcard])
            
        query += " ORDER BY timestamp DESC"
        if limit:
            query += " LIMIT ?"
            params.append(limit)
            
        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        results = []
        for row in rows:
            d = dict(row)
            try:
                d["metadata"] = json.loads(d["metadata_json"]) if d["metadata_json"] else {}
            except Exception:
                d["metadata"] = {}
            results.append(d)
        return results


def get_analysis_by_id(analysis_id: int) -> Optional[Dict[str, Any]]:
    """Retrieve full details of an analysis by integer ID or code."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM analyses WHERE id = ? OR analysis_code = ?", (analysis_id, str(analysis_id)))
        row = cursor.fetchone()
        if not row:
            return None
        d = dict(row)
        try:
            d["metadata"] = json.loads(d["metadata_json"]) if d["metadata_json"] else {}
        except Exception:
            d["metadata"] = {}
        return d


def get_statistics() -> Dict[str, Any]:
    """
    Compute actual stored metrics for the Command Center Dashboard:
    - Total analyses performed
    - Potentially suspicious/fake content detected
    - Real/authentic classifications
    - Text analyses count
    - Image analyses count
    - Video analyses count
    - Distribution & timeline data
    """
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM analyses")
        total = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM analyses WHERE prediction LIKE '%FAKE%' OR prediction LIKE '%SYNTHETIC%' OR prediction LIKE '%MANIPULATED%'")
        suspicious = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM analyses WHERE prediction LIKE '%REAL%' OR prediction LIKE '%AUTHENTIC%'")
        real = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM analyses WHERE media_type = 'Text'")
        text_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM analyses WHERE media_type = 'Image'")
        image_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM analyses WHERE media_type = 'Video'")
        video_count = cursor.fetchone()[0]
        
        # Recent activity (latest 10)
        cursor.execute("SELECT * FROM analyses ORDER BY timestamp DESC LIMIT 10")
        recent = [dict(r) for r in cursor.fetchall()]
        
        # Trends by day
        cursor.execute("""
            SELECT SUBSTR(timestamp, 1, 10) as day, COUNT(*) as count,
                   SUM(CASE WHEN prediction LIKE '%FAKE%' OR prediction LIKE '%SYNTHETIC%' OR prediction LIKE '%MANIPULATED%' THEN 1 ELSE 0 END) as suspicious_count
            FROM analyses
            GROUP BY day
            ORDER BY day DESC
            LIMIT 14
        """)
        trend_rows = cursor.fetchall()
        trends = [dict(r) for r in reversed(trend_rows)]
        
        # Distribution by media type
        cursor.execute("SELECT media_type, COUNT(*) as count FROM analyses GROUP BY media_type")
        media_dist = [dict(r) for r in cursor.fetchall()]
        
        # Distribution by prediction
        cursor.execute("SELECT prediction, COUNT(*) as count FROM analyses GROUP BY prediction")
        pred_dist = [dict(r) for r in cursor.fetchall()]
        
        return {
            "total": total,
            "suspicious": suspicious,
            "real": real,
            "text_count": text_count,
            "image_count": image_count,
            "video_count": video_count,
            "recent": recent,
            "trends": trends,
            "media_distribution": media_dist,
            "prediction_distribution": pred_dist
        }


def clear_history() -> int:
    """Clear all analysis history records from the database."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM analyses")
        deleted = cursor.rowcount
        conn.commit()
        return deleted


def delete_analysis(analysis_id: int) -> bool:
    """Delete a specific analysis record."""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM analyses WHERE id = ? OR analysis_code = ?", (analysis_id, str(analysis_id)))
        conn.commit()
        return cursor.rowcount > 0


# Initialize table on import
init_db()
