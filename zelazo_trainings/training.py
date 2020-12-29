import os
import requests


url = "https://www.googleapis.com/youtube/v3/search?"
youtube_key = os.environ.get("YOUTUBE_KEY")
payload = {
    "channedlId": "UCiOxbbkbhn2wXPo0zIrc1mA",
    "type": "video",
    "key": youtube_key,
    "video_duration": "long"
}

headers = {
  'Content-Type': 'application/json'
}
response = requests.get(url, headers=headers, params=payload)
text_response = response.text

print(text_response)
