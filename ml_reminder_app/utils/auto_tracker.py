import threading
import time
from datetime import datetime
from .watch_detector import get_watched_video_count
from .progress_handler import load_progress, save_progress
from .reminder import send_notification

class AutoTracker:
    def __init__(self, update_callback=None):
        self.update_callback = update_callback
        self.running = False
        self.thread = None
        
    def start_tracking(self):
        """Start background tracking"""
        self.running = True
        print("Auto-tracking started (browser history monitoring disabled for privacy)")
        
    def stop_tracking(self):
        """Stop background tracking"""
        self.running = False
        
    def manual_sync(self):
        """Manually sync progress - placeholder for now"""
        print("Manual sync requested - feature coming soon!")
        return False  # No sync performed
        while self.running:
            try:
                # Check every 30 minutes
                time.sleep(1800)
                
                if not self.running:
                    break
                    
                # Check if videos were watched
                watched_count = get_watched_video_count()
                
                if watched_count > 0:
                    progress = load_progress()
                    old_video = progress['current_video']
                    
                    # Update progress
                    progress['current_video'] = min(
                        progress['current_video'] + watched_count,
                        progress['total_videos']
                    )
                    
                    if progress['current_video'] > old_video:
                        save_progress(progress)
                        
                        # Notify UI to update
                        if self.update_callback:
                            self.update_callback()
                            
                        print(f"Auto-detected: Video {old_video} completed!")
                        
            except Exception as e:
                print(f"Auto-tracking error: {e}")
                
    def manual_sync(self):
        """Manually sync progress"""
        watched_count = get_watched_video_count()
        if watched_count > 0:
            progress = load_progress()
            progress['current_video'] = min(
                progress['current_video'] + watched_count,
                progress['total_videos']
            )
            save_progress(progress)
            return True
        return False
