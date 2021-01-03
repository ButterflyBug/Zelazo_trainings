import os
import requests


def get_response(channelId, pageToken):

    url = "https://www.googleapis.com/youtube/v3/search"
    youtube_key = os.environ.get("YOUTUBE_KEY")
    maxResult = int("50")
    payload = {
        "part": "snippet",
        "channelId": channelId,
        "type": "video",
        "key": youtube_key,
        "videoDuration": "long",
        "maxResults": maxResult,
        "pageToken": pageToken
    }

    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers, params=payload)

    return response


def get_all_videos(channelId):
    response = get_response(channelId, None)
    items = response.json()["items"]

    while response.json().get("nextPageToken"):
        response = get_response(channelId, response.json()["nextPageToken"])
        items += response.json()["items"]

    return items


for item in get_all_videos("UCiOxbbkbhn2wXPo0zIrc1mA"):
    print(item["id"]["videoId"])
