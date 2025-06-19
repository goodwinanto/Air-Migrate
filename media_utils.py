import os
import hashlib

def ensure_folder_exists(folder_path):
    """
    Ensure that the destination folder exists. Create it if it doesn't.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def file_hash(filepath, algo='sha256', blocksize=65536):
    """
    Calculate the hash of a file.
    """
    h = hashlib.new(algo)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(blocksize), b''):
            h.update(chunk)
    return h.hexdigest()

def bytes_to_human_readable(num_bytes):
    """
    Convert bytes to a human-readable string.
    """
    for unit in ['B','KB','MB','GB','TB','PB']:
        if num_bytes < 1024.0:
            return f"{num_bytes:.2f} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.2f} PB"

def is_folder_empty(folder_path):
    """
    Check if a folder is empty.
    """
    return not any(os.scandir(folder_path))