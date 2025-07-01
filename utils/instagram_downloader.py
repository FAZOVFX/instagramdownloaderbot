import instaloader
import os
from pydub import AudioSegment

def download_instagram_post(url):
    L = instaloader.Instaloader(dirname_pattern="downloads", save_metadata=False, post_metadata_txt_pattern="")
    shortcode = url.split("/")[-2]
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    L.download_post(post, target=shortcode)

    media_path = f"downloads/{shortcode}/{shortcode}.mp4"
    audio_path = None

    if os.path.exists(media_path):
        audio_path = f"downloads/{shortcode}/{shortcode}.mp3"
        AudioSegment.from_file(media_path).export(audio_path, format="mp3")
    return media_path, audio_path
