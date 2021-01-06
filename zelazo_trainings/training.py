import os
from video import Video
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

    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers, params=payload)

    return response


def get_all_videos(channelId):
    response = get_response(channelId, None)
    items = response.json()["items"]

    while response.json().get("nextPageToken"):
        response = get_response(channelId, response.json()["nextPageToken"])
        items += response.json()["items"]

    return items


def create_list_of_videos():
    list_of_video_ids = []

    for item in get_all_videos("UCiOxbbkbhn2wXPo0zIrc1mA"):
        list_of_video_ids.append(item["id"]["videoId"])

    return list_of_video_ids


def get_info_about_video(id):
    url = "https://youtube.googleapis.com/youtube/v3/videos"
    youtube_key = os.environ.get("YOUTUBE_KEY")
    payload = {
        "part": "contentDetails",
        "key": youtube_key,
        "id": id
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers, params=payload)

    return response


def get_videos_info():
    video_ids = create_list_of_videos()
    video_info = []

    for video_id in video_ids:
        video_info.append(get_info_about_video(video_id).json())

    return video_info


def get_duration(video_details):
    return video_details["items"][0]["contentDetails"]["duration"]


def get_video_id(video_details):
    return video_details["items"][0]["id"]


video_objects = list(map(lambda element: Video(
    get_video_id(element), get_duration(element)), get_videos_info()))
long_videos = list(filter(lambda video: video.is_long, video_objects))

# print(long_videos)
# print(len(long_videos))
