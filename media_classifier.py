import os
from collections import defaultdict
from models import MediaSummary, MediaDetails, IMAGE_EXTS, VIDEO_EXTS

def classify_files_in_folder(folder_path):
    heic_files = set()
    mov_files = set()
    total_size = 0
    counts = defaultdict(int)
    file_lists = defaultdict(list)

    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path, fname)
        if not os.path.isfile(fpath):
            continue
        ext = os.path.splitext(fname)[1].lower()
        base = os.path.splitext(fname)[0]
        total_size += os.path.getsize(fpath)

        if ext in IMAGE_EXTS:
            counts["photos"] += 1
            file_lists["photos"].append(fname)
            if ext == ".heic":
                heic_files.add(base)
        elif ext in VIDEO_EXTS:
            counts["videos"] += 1
            file_lists["videos"].append(fname)
            if ext == ".mov":
                mov_files.add(base)
        elif ext == ".gif":
            counts["gifs"] += 1
            file_lists["gifs"].append(fname)
        else:
            counts["other"] += 1
            file_lists["other"].append(fname)

        fname_upper = fname.upper()
        if "PORTRAIT" in fname_upper:
            counts["portraits"] += 1
            file_lists["portraits"].append(fname)
        if "PANO" in fname_upper:
            counts["panoramas"] += 1
            file_lists["panoramas"].append(fname)
        if "CINEMATIC" in fname_upper:
            counts["cinematic"] += 1
            file_lists["cinematic"].append(fname)
        if "SLOMO" in fname_upper or "SLOW" in fname_upper:
            counts["slow_mo"] += 1
            file_lists["slow_mo"].append(fname)
        if "TIMELAPSE" in fname_upper or "TIME" in fname_upper:
            counts["timelapse"] += 1
            file_lists["timelapse"].append(fname)
        if "BURST" in fname_upper:
            counts["burst"] += 1
            file_lists["burst"].append(fname)
        if "SELFIE" in fname_upper:
            counts["selfies"] += 1
            file_lists["selfies"].append(fname)
        if "SCREENSHOT" in fname_upper:
            counts["screenshots"] += 1
            file_lists["screenshots"].append(fname)
        if "SCREENRECORD" in fname_upper or "REC" in fname_upper:
            counts["screen_recordings"] += 1
            file_lists["screen_recordings"].append(fname)

        if ext == ".dng" or ext == ".raw":
            counts["raw"] += 1
            file_lists["raw"].append(fname)

    live_photos = heic_files.intersection(mov_files)
    counts["live_photos"] = len(live_photos)
    for base in live_photos:
        heic_name = base + ".HEIC"
        mov_name = base + ".MOV"
        if heic_name in file_lists["photos"]:
            file_lists["photos"].remove(heic_name)
        if mov_name in file_lists["videos"]:
            file_lists["videos"].remove(mov_name)
        file_lists["live_photos"].extend([heic_name, mov_name])

    counts["photos"] -= len(live_photos)
    counts["videos"] -= len(live_photos)
    if counts["photos"] < 0: counts["photos"] = 0
    if counts["videos"] < 0: counts["videos"] = 0

    summary = MediaSummary(
        photos=counts["photos"],
        videos=counts["videos"],
        live_photos=counts["live_photos"],
        portraits=counts["portraits"],
        panoramas=counts["panoramas"],
        raw=counts["raw"],
        cinematic=counts["cinematic"],
        slow_mo=counts["slow_mo"],
        timelapse=counts["timelapse"],
        burst=counts["burst"],
        selfies=counts["selfies"],
        screenshots=counts["screenshots"],
        screen_recordings=counts["screen_recordings"],
        gifs=counts["gifs"],
        other=counts["other"],
        size_bytes=total_size
    )
    return MediaDetails(summary=summary, file_lists=dict(file_lists))