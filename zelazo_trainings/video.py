import isodate


class Video():
    LONG_VIDEO_TRESHOLD = 50

    def __init__(self, video_id, duration):
        self.video_id = video_id
        self.duration = duration

    def raw_duration(self, video_id):
        return self.duration

    def duration_in_seconds(self):
        return isodate.parse_duration(self.duration).total_seconds()

    @property
    def is_long(self):
        return self.duration_in_seconds() >= self.LONG_VIDEO_TRESHOLD * 60
