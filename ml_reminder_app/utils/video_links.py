# List of YouTube video URLs from Krish Naik's ML playlist
# Video 1 is at index 0, Video 2 at index 1, etc.

video_links = [
    "https://www.youtube.com/watch?v=aircAruvnKk",  # 1
    "https://www.youtube.com/watch?v=cKxRvEZd3Mw",  # 2
    "https://www.youtube.com/watch?v=5WgKpS4Pz54",  # 3
    # ... (extend this with real video URLs)
    # Add up to 154 entries as needed
]

def get_video_url(video_number):
    """Get YouTube URL for specific video number"""
    # Default to Krish Naik's ML playlist
    base_url = "https://www.youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe"
    
    # You can customize this with specific video URLs if needed:
    # video_urls = {
    #     1: "https://www.youtube.com/watch?v=VIDEO_ID_1",
    #     2: "https://www.youtube.com/watch?v=VIDEO_ID_2",
    # }
    # return video_urls.get(video_number, base_url)
    
    return base_url
    # }
    # return video_urls.get(video_number, base_url)
    
    return base_url
