import threading
import time
from datetime import datetime

try:
    from plyer import notification
    NOTIFICATION_AVAILABLE = True
except ModuleNotFoundError:
    print("plyer module not found. Install with: pip install plyer")
    NOTIFICATION_AVAILABLE = False

class ReminderScheduler:
    def __init__(self):
        self.running = False
        self.thread = None
        
    def start_reminders(self, progress_callback):
        """Start the reminder scheduler"""
        self.running = True
        self.progress_callback = progress_callback
        self.thread = threading.Thread(target=self._reminder_loop, daemon=True)
        self.thread.start()
        
    def stop_reminders(self):
        """Stop the reminder scheduler"""
        self.running = False
        
    def _reminder_loop(self):
        """Background loop for sending reminders"""
        while self.running:
            try:
                now = datetime.now()
                
                # Send reminders at specific times
                if (now.hour in [9, 14, 19] and now.minute == 0 and now.second < 30):
                    progress = self.progress_callback()
                    self._send_reminder(progress['current_video'], self._get_reminder_message(now.hour))
                    time.sleep(30)  # Prevent duplicate notifications
                
                # Check every minute
                time.sleep(60)
                
            except Exception as e:
                print(f"Reminder scheduler error: {e}")
                time.sleep(60)
                
    def _get_reminder_message(self, hour):
        """Get appropriate message based on time"""
        if hour == 9:
            return "🌅 Good morning! Start your day with ML learning!"
        elif hour == 14:
            return "☀️ Afternoon break! Time for your ML video!"
        elif hour == 19:
            return "🌙 Evening study time! Don't miss today's ML lesson!"
        return "📚 Time to continue your ML journey!"

    def _send_reminder(self, video_no, custom_message):
        """Send reminder with custom message"""
        if not NOTIFICATION_AVAILABLE:
            print(f"Reminder: {custom_message} - Video #{video_no}")
            return
        
        try:
            notification.notify(
                title="ML Learning Reminder",
                message=f"{custom_message}\nVideo #{video_no} is waiting!",
                timeout=10
            )
        except Exception as e:
            print("Notification failed:", e)

# Global reminder scheduler
reminder_scheduler = ReminderScheduler()

def send_notification(video_no):
    """Send immediate notification for current video"""
    if not NOTIFICATION_AVAILABLE:
        print(f"Reminder: Time to watch ML Video #{video_no}!")
        return
    
    try:
        notification.notify(
            title="ML Learning Reminder",
            message=f"Time to watch ML Video #{video_no}!",
            timeout=5
        )
    except Exception as e:
        print("Notification failed:", e)

def send_motivational_reminder(video_no):
    """Send motivational reminder"""
    messages = [
        f"🚀 You're doing great! Video #{video_no} awaits!",
        f"💪 Keep up the momentum! Time for Video #{video_no}!",
        f"🎯 Stay focused on your ML journey! Video #{video_no}!",
        f"⭐ Another step closer to ML mastery! Video #{video_no}!",
        f"🔥 Don't break the streak! Watch Video #{video_no}!"
    ]
    
    import random
    message = random.choice(messages)
    
    if not NOTIFICATION_AVAILABLE:
        print(f"Motivational Reminder: {message}")
        return
    
    try:
        notification.notify(
            title="ML Motivation Boost!",
            message=message,
            timeout=8
        )
    except Exception as e:
        print("Notification failed:", e)
    except Exception as e:
        print("Notification failed:", e)
        print(f"Motivational Reminder: {message}")
