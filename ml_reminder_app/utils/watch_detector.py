import os
import json
import sqlite3
from datetime import datetime, timedelta

def check_browser_history():
    """Check browser history for YouTube video watches"""
    # Chrome history location
    chrome_history = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
    
    try:
        # Create a copy to read from (Chrome locks the original)
        import shutil
        temp_history = "temp_history.db"
        shutil.copy2(chrome_history, temp_history)
        
        conn = sqlite3.connect(temp_history)
        cursor = conn.cursor()
        
        # Look for YouTube ML playlist videos in last 24 hours
        yesterday = datetime.now() - timedelta(days=1)
        timestamp = int(yesterday.timestamp() * 1000000)  # Chrome uses microseconds
        
        query = """
        SELECT url, title, visit_count, last_visit_time 
        FROM urls 
        WHERE url LIKE '%youtube.com/watch%' 
        AND url LIKE '%list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe%'
        AND last_visit_time > ?
        ORDER BY last_visit_time DESC
        """
        
        cursor.execute(query, (timestamp,))
        results = cursor.fetchall()
        
        conn.close()
        os.remove(temp_history)
        
        return len(results) > 0  # Return True if any ML videos were watched
        
    except Exception as e:
        print(f"Could not check browser history: {e}")
        return False

def get_watched_video_count():
    """Estimate how many videos were watched based on browser activity"""
    try:
        if check_browser_history():
            return 1  # Assume 1 video watched if browser history shows activity
        return 0
    except:
        return 0
