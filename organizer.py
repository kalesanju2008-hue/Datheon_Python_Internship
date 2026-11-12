
"""
Automated File Organizer & Cleanup Utility
Run: python organizer.py
Moves files into category folders. It never deletes files and avoids
overwriting duplicate filenames by adding _1, _2, and so on.
"""
import os
import shutil
import logging
from pathlib import Path

FILE_CATEGORIES = {
    ".pdf": "Documents", ".doc": "Documents", ".docx": "Documents",
    ".txt": "Documents", ".rtf": "Documents", ".ppt": "Documents",
    ".pptx": "Documents", ".xls": "Documents", ".xlsx": "Documents",
    ".csv": "Documents",
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".gif": "Images", ".bmp": "Images", ".svg": "Images", ".webp": "Images",
    ".mp4": "Videos", ".mkv": "Videos", ".mov": "Videos",
    ".avi": "Videos", ".wmv": "Videos",
    ".mp3": "Audio", ".wav": "Audio", ".aac": "Audio", ".flac": "Audio",
    ".zip": "Archives", ".rar": "Archives", ".7z": "Archives",
    ".tar": "Archives", ".gz": "Archives",
    ".py": "Code", ".java": "Code", ".c": "Code", ".cpp": "Code",
    ".js": "Code", ".html": "Code", ".css": "Code", ".php": "Code",
    ".json": "Code",
}

LOG_FILE = Path(__file__).with_name("organizer.log")


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def unique_destination(destination):
    """Return a free filename without replacing an existing file."""
    if not destination.exists():
        return destination
    number = 1
    while True:
        candidate = destination.with_name(
            f"{destination.stem}_{number}{destination.suffix}"
        )
        if not candidate.exists():
            return candidate
        number += 1


def organize_folder(folder_path):
    folder = Path(folder_path).expanduser().resolve()

    if not folder.exists():
        print("Error: Folder does not exist.")
        return
    if not folder.is_dir():
        print("Error: The path is not a folder.")
        return

    moved = 0
    errors = 0
    print(f"\nOrganizing: {folder}\n")

    try:
        with os.scandir(folder) as entries:
            for entry in entries:
                try:
                    if not entry.is_file(follow_symlinks=False):
                        continue

                    source = Path(entry.path)
                    category = FILE_CATEGORIES.get(source.suffix.lower(), "Others")
                    target_folder = folder / category
                    target_folder.mkdir(exist_ok=True)

                    destination = unique_destination(target_folder / source.name)
                    shutil.move(str(source), str(destination))
                    moved += 1
                    logging.info("Moved %s to %s", source.name, category)

                except PermissionError as error:
                    errors += 1
                    logging.error("Permission denied for %s: %s", entry.name, error)
                except OSError as error:
                    errors += 1
                    logging.error("Could not move %s: %s", entry.name, error)

    except PermissionError as error:
        print(f"Cannot access folder: {error}")
        return
    except OSError as error:
        print(f"Could not scan folder: {error}")
        return

    print("\n" + "=" * 42)
    print("       FILE ORGANIZATION SUMMARY")
    print("=" * 42)
    print(f"Files moved successfully : {moved}")
    print(f"Errors                   : {errors}")
    print(f"Activity log             : {LOG_FILE}")
    print("=" * 42)


def main():
    setup_logging()
    print("AUTOMATED FILE ORGANIZER")
    print("Files will be moved into category folders. Nothing is deleted.")
    folder = input("\nEnter folder path to organize: ").strip().strip('"')

    if not folder:
        print("No folder entered. Exiting.")
        return

    confirm = input(f"\nOrganize files in '{folder}'? (y/n): ").strip().lower()
    if confirm == "y":
        organize_folder(folder)
    else:
        print("Cancelled. No files were moved.")


if __name__ == "__main__":
    main()
