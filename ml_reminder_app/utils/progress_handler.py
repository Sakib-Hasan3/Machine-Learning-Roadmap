import json
import os

# Data file configuration
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DATA_FILE = os.path.join(DATA_DIR, "progress.json")

def load_progress():
    """Load progress data from JSON file"""
    try:
        if not os.path.exists(DATA_FILE):
            print("Progress file not found. Creating with default values.")
            default_data = {"current_video": 1, "total_videos": 154}
            save_progress(default_data)
            return default_data
            
        with open(DATA_FILE, 'r') as f:
            content = f.read().strip()
            if not content:
                print("Progress file is empty. Creating with default values.")
                default_data = {"current_video": 1, "total_videos": 154}
                save_progress(default_data)
                return default_data
            
            return json.loads(content)
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}. Recreating with default values.")
        default_data = {"current_video": 1, "total_videos": 154}
        save_progress(default_data)
        return default_data
    except Exception as e:
        print("Failed to load progress data:", e)
        return {"current_video": 1, "total_videos": 154}

def save_progress(data):
    """Save progress data to JSON file"""
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Progress saved successfully")
    except Exception as e:
        print("Failed to save progress data:", e)
