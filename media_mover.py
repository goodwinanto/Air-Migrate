import os
import shutil
import hashlib

def file_hash(filepath, algo='sha256', blocksize=65536):
    h = hashlib.new(algo)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(blocksize), b''):
            h.update(chunk)
    return h.hexdigest()

def move_file_with_verification(src, dest_folder):
    """
    Copy src to dest_folder, verify hash, then delete src if hashes match.
    Returns True if successful, False otherwise.
    """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    dest = os.path.join(dest_folder, os.path.basename(src))
    try:
        shutil.copy2(src, dest)
        src_hash = file_hash(src)
        dest_hash = file_hash(dest)
        if src_hash == dest_hash:
            os.remove(src)
            return True
        else:
            print(f"Hash mismatch: {src} and {dest}")
            os.remove(dest)
            return False
    except Exception as e:
        print(f"Failed to move {src}: {e}")
        if os.path.exists(dest):
            os.remove(dest)
        return False

def move_files_with_verification(file_paths, dest_folder):
    results = []
    for fpath in file_paths:
        result = move_file_with_verification(fpath, dest_folder)
        results.append((fpath, result))
    return results