import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import os

from media_classifier import classify_files_in_folder
from media_mover import move_files_with_verification
from media_copier import copy_files_with_verification
from media_utils import bytes_to_human_readable, ensure_folder_exists

class AirMigrateApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AirMigrate")
        self.geometry("700x500")
        self.source_folder = tk.StringVar()
        self.dest_folder = tk.StringVar()
        self.media_summary = None
        self.file_lists = None

        self.create_widgets()

    def create_widgets(self):
        # Source folder selection
        tk.Label(self, text="iPhone/DCIM Folder:").pack(anchor="w")
        src_frame = tk.Frame(self)
        src_frame.pack(fill="x")
        src_entry = tk.Entry(src_frame, textvariable=self.source_folder, width=60)
        src_entry.pack(side="left", padx=5)
        tk.Button(src_frame, text="Browse", command=self.browse_source).pack(side="left")
        
        # Destination folder selection
        tk.Label(self, text="Destination Folder:").pack(anchor="w")
        dest_frame = tk.Frame(self)
        dest_frame.pack(fill="x")
        dest_entry = tk.Entry(dest_frame, textvariable=self.dest_folder, width=60)
        dest_entry.pack(side="left", padx=5)
        tk.Button(dest_frame, text="Browse", command=self.browse_dest).pack(side="left")

        # Scan and summary area
        tk.Button(self, text="Scan", command=self.scan_media).pack(pady=10)

        self.summary_text = tk.Text(self, height=10, state="disabled")
        self.summary_text.pack(fill="both", expand=False, padx=5, pady=5)

        # Transfer buttons
        transfer_frame = tk.Frame(self)
        transfer_frame.pack(pady=5)
        tk.Button(transfer_frame, text="Copy All (Verified)", command=self.start_copy, width=18).pack(side="left", padx=5)
        tk.Button(transfer_frame, text="Move All (Verified)", command=self.start_move, width=18).pack(side="left", padx=5)

        # Progress bar
        self.progress = ttk.Progressbar(self, orient="horizontal", mode="determinate", length=500)
        self.progress.pack(pady=10)

    def browse_source(self):
        folder = filedialog.askdirectory(title="Select iPhone/DCIM folder")
        if folder:
            self.source_folder.set(folder)

    def browse_dest(self):
        folder = filedialog.askdirectory(title="Select Destination folder")
        if folder:
            self.dest_folder.set(folder)

    def scan_media(self):
        folder = self.source_folder.get()
        if not os.path.isdir(folder):
            messagebox.showerror("Error", "Please select a valid source folder.")
            return
        self.append_summary("Scanning media files...")
        details = classify_files_in_folder(folder)
        self.media_summary = details.summary
        self.file_lists = details.file_lists
        self.show_summary(details)

    def show_summary(self, details):
        summary = details.summary
        lines = [
            f"Photos: {summary.photos}",
            f"Videos: {summary.videos}",
            f"Live Photos: {summary.live_photos}",
            f"Portraits: {summary.portraits}",
            f"Panoramas: {summary.panoramas}",
            f"Raw: {summary.raw}",
            f"Cinematic: {summary.cinematic}",
            f"Slow-mo: {summary.slow_mo}",
            f"Time-lapse: {summary.timelapse}",
            f"Burst: {summary.burst}",
            f"Selfies: {summary.selfies}",
            f"Screenshots: {summary.screenshots}",
            f"Screen Recordings: {summary.screen_recordings}",
            f"GIFs: {summary.gifs}",
            f"Other: {summary.other}",
            f"Total Size: {bytes_to_human_readable(summary.size_bytes)}"
        ]
        self.summary_text.config(state="normal")
        self.summary_text.delete("1.0", "end")
        self.summary_text.insert("end", "\n".join(lines))
        self.summary_text.config(state="disabled")

    def append_summary(self, text):
        self.summary_text.config(state="normal")
        self.summary_text.insert("end", text + "\n")
        self.summary_text.config(state="disabled")

    def start_copy(self):
        if not self.validate_transfer():
            return
        self.run_transfer_thread(copy=True)

    def start_move(self):
        if not self.validate_transfer():
            return
        self.run_transfer_thread(copy=False)

    def validate_transfer(self):
        if not self.source_folder.get() or not os.path.isdir(self.source_folder.get()):
            messagebox.showerror("Error", "Please select a valid source folder.")
            return False
        if not self.dest_folder.get():
            messagebox.showerror("Error", "Please select a destination folder.")
            return False
        ensure_folder_exists(self.dest_folder.get())
        if not self.media_summary or not self.file_lists:
            messagebox.showerror("Error", "Please scan media files first.")
            return False
        return True

    def run_transfer_thread(self, copy=True):
        files_to_transfer = []
        for flist in self.file_lists.values():
            files_to_transfer.extend([os.path.join(self.source_folder.get(), f) for f in flist])
        total_files = len(files_to_transfer)
        if total_files == 0:
            messagebox.showinfo("Info", "No files to transfer.")
            return

        self.progress["maximum"] = total_files
        self.progress["value"] = 0

        def transfer():
            success = 0
            failed = 0
            if copy:
                op_func = copy_files_with_verification
                op_name = "Copy"
            else:
                op_func = move_files_with_verification
                op_name = "Move"
            results = op_func(files_to_transfer, self.dest_folder.get())
            for idx, (fpath, status) in enumerate(results, 1):
                if status:
                    success += 1
                else:
                    failed += 1
                self.progress["value"] = idx
                self.append_summary(f"{op_name}d: {os.path.basename(fpath)} - {'OK' if status else 'FAILED'}")
            self.append_summary(f"{op_name} complete: {success} succeeded, {failed} failed.")

        thread = threading.Thread(target=transfer, daemon=True)
        thread.start()

if __name__ == "__main__":
    app = AirMigrateApp()
    app.mainloop()