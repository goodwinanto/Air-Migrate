from collections import namedtuple

IMAGE_EXTS = {
    '.heic', '.heifs', '.heics',
    '.jpg', '.jpeg',
    '.png', '.gif', '.tiff', '.bmp',
    '.raw', '.dng'
}
VIDEO_EXTS = {
    '.mov', '.mp4', '.m4v',
    '.avi', '.3gp'
}

MediaSummary = namedtuple("MediaSummary", [
    "photos", "videos", "live_photos", "portraits", "panoramas", "raw", "cinematic",
    "slow_mo", "timelapse", "burst", "selfies", "screenshots", "screen_recordings", "gifs", "other", "size_bytes"
])

MediaDetails = namedtuple("MediaDetails", [
    "summary",
    "file_lists"
])