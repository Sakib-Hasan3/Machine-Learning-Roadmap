import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from datetime import datetime
import threading
import time

# Utils import
from utils.progress_handler import load_progress, save_progress
from utils.reminder import send_notification
from utils.video_links import get_video_url

# Load progress data
progress = load_progress()

# --- Theme Colors ---
BG_DARK = "#1e1e1e"
CARD_BG = "#2c2c2c"
TEXT_COLOR = "#e0e0e0"
HIGHLIGHT = "#4CAF50"
ACCENT = "#3498db"

# Tkinter window
app = tk.Tk()
app.title("🖤 ML Tracker – Krish Naik")
app.geometry("500x400")
app.configure(bg=BG_DARK)
app.resizable(False, False)

# Fonts
FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_TEXT = ("Segoe UI", 11)
FONT_SMALL = ("Segoe UI", 9)

# --- Title ---
header = tk.Label(app, text="🧠 ML Tracker", font=FONT_TITLE, fg=HIGHLIGHT, bg=BG_DARK)
header.pack(pady=(20, 5))

sub = tk.Label(app, text="Track your Machine Learning journey with Krish Naik",
               font=FONT_SMALL, fg="#bbbbbb", bg=BG_DARK)
sub.pack(pady=(0, 20))

# --- Current Video Info ---
video_label = tk.Label(app, text=f"🎯 Video #{progress['current_video']}",
                       font=("Segoe UI", 13, "bold"), fg=TEXT_COLOR, bg=BG_DARK)
video_label.pack()

# --- Progress Bar ---
progress_percent = (progress['current_video'] / progress['total_videos']) * 100
progress_var = tk.DoubleVar(value=progress_percent)

style = ttk.Style()
style.theme_use("clam")
style.configure("dark.Horizontal.TProgressbar", 
                background=HIGHLIGHT, troughcolor="#3c3c3c", bordercolor=BG_DARK)

progress_bar = ttk.Progressbar(app, variable=progress_var, maximum=100,
                               length=350, style="dark.Horizontal.TProgressbar")
progress_bar.pack(pady=10)

progress_text = tk.Label(app, text=f"Progress: {progress['current_video']} / {progress['total_videos']} ({progress_percent:.1f}%)",
                         font=FONT_TEXT, fg="#aaaaaa", bg=BG_DARK)
progress_text.pack()

# --- Functions ---
def update_ui():
    """Update UI elements when progress changes"""
    global progress
    progress = load_progress()
    video_label.config(text=f"🎯 Video #{progress['current_video']}")
    progress_percent = (progress['current_video'] / progress['total_videos']) * 100
    progress_var.set(progress_percent)
    progress_text.config(text=f"Progress: {progress['current_video']} / {progress['total_videos']} ({progress_percent:.1f}%)")

def watch_video():
    """Open current video in browser"""
    url = get_video_url(progress['current_video'])
    webbrowser.open(url)

def mark_completed():
    """Mark current video as completed"""
    if progress['current_video'] < progress['total_videos']:
        progress['current_video'] += 1
        save_progress(progress)
        update_ui()
        messagebox.showinfo("✅ Success", "Video marked as completed!")
    else:
        messagebox.showinfo("🎉 Congratulations!", "You've completed all videos!")

def send_reminder():
    """Send notification reminder"""
    send_notification(progress['current_video'])

# --- Auto Reminder System ---
class AutoReminder:
    def __init__(self):
        self.running = False
        self.thread = None
        self.reminder_times = [9, 14, 19]  # 9 AM, 2 PM, 7 PM
        
    def start(self):
        """Start auto reminder system"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._reminder_loop, daemon=True)
            self.thread.start()
            print("Auto reminders started for 9 AM, 2 PM, and 7 PM")
    
    def stop(self):
        """Stop auto reminder system"""
        self.running = False
        
    def _reminder_loop(self):
        """Background loop to check for reminder times"""
        last_reminder_hour = -1
        
        while self.running:
            try:
                now = datetime.now()
                current_hour = now.hour
                
                # Check if it's time for a reminder and we haven't sent one this hour
                if (current_hour in self.reminder_times and 
                    current_hour != last_reminder_hour and 
                    now.minute < 5):  # Send within first 5 minutes of the hour
                    
                    self._send_scheduled_reminder(current_hour)
                    last_reminder_hour = current_hour
                
                # Reset at midnight
                if current_hour == 0 and last_reminder_hour != 0:
                    last_reminder_hour = -1
                
                # Check every minute
                time.sleep(60)
                
            except Exception as e:
                print(f"Auto reminder error: {e}")
                time.sleep(60)
    
    def _send_scheduled_reminder(self, hour):
        """Send scheduled reminder with time-specific message"""
        progress_data = load_progress()
        video_num = progress_data['current_video']
        
        messages = {
            9: f"🌅 Good morning! Start your day with ML Video #{video_num}",
            14: f"☀️ Afternoon break! Time for ML Video #{video_num}",
            19: f"🌙 Evening study time! ML Video #{video_num} awaits!"
        }
        
        message = messages.get(hour, f"📚 Time for ML Video #{video_num}!")
        
        try:
            from utils.reminder import notification, NOTIFICATION_AVAILABLE
            if NOTIFICATION_AVAILABLE:
                notification.notify(
                    title="ML Learning Reminder",
                    message=message,
                    timeout=10
                )
            else:
                print(f"Auto Reminder: {message}")
                
        except Exception as e:
            print(f"Notification error: {e}")
            print(f"Auto Reminder: {message}")

# Initialize auto reminder system
auto_reminder = AutoReminder()

def toggle_auto_reminders():
    """Toggle auto reminders on/off"""
    if auto_reminder.running:
        auto_reminder.stop()
        auto_reminder_btn.config(text="🔔 Enable Auto Reminders", bg="#9b59b6")
        messagebox.showinfo("Auto Reminders", "Auto reminders disabled")
    else:
        auto_reminder.start()
        auto_reminder_btn.config(text="🔕 Disable Auto Reminders", bg="#e67e22")
        messagebox.showinfo("Auto Reminders", "Auto reminders enabled!\n⏰ Will remind at 9 AM, 2 PM, and 7 PM")

def reset_progress():
    """Reset progress to beginning"""
    result = messagebox.askyesno("Reset Progress", "Are you sure you want to reset your progress?")
    if result:
        progress['current_video'] = 1
        save_progress(progress)
        update_ui()
        messagebox.showinfo("Reset", "Progress has been reset!")

# --- Action Buttons ---
button_frame = tk.Frame(app, bg=BG_DARK)
button_frame.pack(pady=20)

# Modern button style
def create_button(parent, text, command, bg_color, row, col):
    btn = tk.Button(parent, text=text, command=command, font=FONT_TEXT,
                    bg=bg_color, fg="white", relief="flat", padx=15, pady=8,
                    cursor="hand2", activebackground=bg_color, activeforeground="white")
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
    
    # Hover effects
    def on_enter(e):
        btn.config(bg="#" + "".join([format(min(255, int(bg_color[i:i+2], 16) + 20), '02x') for i in (1, 3, 5)]))
    def on_leave(e):
        btn.config(bg=bg_color)
    
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# Configure grid columns
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

# Buttons
watch_btn = create_button(button_frame, "▶️ Watch Video", watch_video, ACCENT, 0, 0)
complete_btn = create_button(button_frame, "✅ Mark Completed", mark_completed, HIGHLIGHT, 0, 1)
remind_btn = create_button(button_frame, "🔔 Send Reminder", send_reminder, "#9b59b6", 1, 0)
reset_btn = create_button(button_frame, "🔄 Reset Progress", reset_progress, "#e74c3c", 1, 1)

# Add auto reminder toggle button
auto_reminder_btn = create_button(button_frame, "🔔 Enable Auto Reminders", toggle_auto_reminders, "#9b59b6", 2, 0)
button_frame.grid_rowconfigure(2, weight=1)

# Add reminder status label
reminder_status = tk.Label(button_frame, text="Auto reminders: 9 AM • 2 PM • 7 PM", 
                          font=("Segoe UI", 8), fg="#888888", bg=BG_DARK)
reminder_status.grid(row=2, column=1, padx=5, pady=5)

# --- Status Footer ---
footer = tk.Label(app, text="🚀 Keep learning and growing your ML skills!",
                  font=FONT_SMALL, fg="#888888", bg=BG_DARK)
footer.pack(side="bottom", pady=10)

# Initialize UI
update_ui()

# Start auto reminders by default
auto_reminder.start()
auto_reminder_btn.config(text="🔕 Disable Auto Reminders", bg="#e67e22")

# Auto reminder at startup if it's 10 AM
now = datetime.now()
if now.hour == 10:
    send_notification(progress['current_video'])

# Cleanup on exit
def on_closing():
    auto_reminder.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)

# Run the application
app.mainloop()