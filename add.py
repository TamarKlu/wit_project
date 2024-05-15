#Upload 171
import os
from pathlib import Path
import shutil


def add(path: str) -> None:
    current_diroctory = Path.cwd()
    path_to_add = current_diroctory / Path(path)
    relitve_path = is_wit(path_to_add)
    destanation = relitve_path / "staging_area"
    if relitve_path is not None:
        if path_to_add.is_dir():
            shutil.copytree(path_to_add, str(destanation) + "\\" + path_to_add.name, ignore=shutil.ignore_patterns(".wit"))
        else:
            shutil.copy(path_to_add, destanation)
     

def is_wit(path: os.PathLike) :   
    current_path = path
    while current_path != current_path.parent:
        if len(list(current_path.rglob("*.wit"))) > 0:
            relitve_path = current_path / ".wit"
            return relitve_path 
        else:      
            current_path = current_path.parent
    return None


if __name__ == "__main__":
    add(r"git init.docx")




