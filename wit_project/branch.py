#Upload 176
import os
from pathlib import Path
import sys
import typing

def branch(NAME: str) -> None:
    relitve_path = is_wit(Path.cwd())
    if relitve_path is not None:
        refrences = relitve_path / "references.txt"
        with open(refrences, "r") as read:
            read = read.read()
            read = read.split(" ")
            commit_id = read[2]
            master = read[6]
        if len(read) > 6:
            with open(refrences, "w") as txt:
                txt.write(f"HEAD = {commit_id} \n master = {master} \n {NAME} = {commit_id}")
        else:
            with open(refrences, "a") as txt:
                txt.write(f" \n {NAME} = {commit_id}")


def is_wit(path: os.PathLike) -> None | os.PathLike:   
    current_path = path
    while current_path != current_path.parent:
        if len(list(current_path.rglob("*.wit"))) > 0:
            relitve_path = current_path / ".wit"
            return relitve_path 
        else:      
            current_path = current_path.parent
    return None


if __name__ == "__main__":
    branch(sys.argv[1])