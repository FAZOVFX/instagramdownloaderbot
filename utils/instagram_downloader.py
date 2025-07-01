import instaloader
import os
from pydub import AudioSegment
from dotenv import load_dotenv

load_dotenv()

def download_instagram_post(url):
    shortcode = url.split("/")[-2]
    download_dir = f"/tmp/{shortcode}"
    os.makedirs(download_dir, exist_ok=True)

    L = instaloader.Instaloader(dirname_pattern=download_dir, save_metadata=False)
    
    try:
        L.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
    except:
        pass  # login bo‘lmasa davom etadi

    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=shortcode)
    except Exception as e:
        return None, None

    video_path = f"{download_dir}/{shortcode}.mp4"
    audio_path = None

    if os.path.exists(video_path):
        audio_path = f"{download_dir}/{shortcode}.mp3"
        AudioSegment.from_file(video_path).export(audio_path, format="mp3")

    return video_path if os.path.exists(video_path) else None, audio_path
