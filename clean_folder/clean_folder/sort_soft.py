import sys
from pathlib import Path
import shutil

CATEGORIES = {
    "музика": [".mp3", ".wav", ".amr", ".ogg"],
    "документи": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
    "зображення": [".jpeg", ".png", ".jpg", ".svg"],
    "відео": [".avi", ".mp4", ".mov", ".mkv"],
    "архіви": [".zip", ".gz", ".tar"]
}


def get_categories(file: Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"


def move_file(file: Path, category: str, root_dir: Path) -> None:
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir(parents=True)
    new_path = target_dir.joinpath(file.name)

    if new_path.exists():
        i = 1
        while True:
            new_name = f"{file.stem}_{i}{file.suffix}"
            new_path = target_dir.joinpath(new_name)
            if not new_path.exists():
                break
            i += 1

    file.replace(new_path)


def unpack_archives(archive: Path, target_dir: Path) -> None:
    shutil.unpack_archive(str(archive), str(target_dir))


def sort_folder(path: Path) -> None:
    for element in path.glob("**/*"):
        if element.is_file():
            category = get_categories(element)
            move_file(element, category, path)


def main() -> str:
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"

    if not path.exists():
        return "Folder does not exist"

    sort_folder(path)

    return "All Ok"


if __name__ == '__main__':
    print(main())

