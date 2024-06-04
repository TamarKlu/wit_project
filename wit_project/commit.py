#Upload 172
import typing

from datetime import datetime

import os
from pathlib import Path
import random
import shutil
import string
import sys


class Commit:
    def __init__(self, message: str, path: os.PathLike | None=None) -> None:
        self.commit_id = "".join(random.choices(string.hexdigits, k=40))
        self.message = message
        self.path = path
    
    def commit(self) -> None:
        self.relitve_path = self.is_wit(self.path)
        if self.relitve_path is not None:
            path_comit_id = self.relitve_path / "images" / self.commit_id
            path_comit_id.mkdir()
            path_file_commit_id = str(path_comit_id) + "/.txt"
            self.references = self.relitve_path / "references.txt"
            activted = self.relitve_path / "activted.txt"
            with open(activted, "r"):
                with open(activted, "r") as brench:
                    brench = brench.read()
                    brench = str(brench)
            if self.references.exists():
                with open(self.references, "r") as txt:
                    txt = txt.read()
                    txt = txt.split()
                    parent = txt[2]
                    master = txt[5]
                    if len(txt) > 6:
                        brench_id = txt[-1]
                        brench_name = txt[6]  
                    else:
                        brench_name = "none"
            else:
                parent = None
                master = self.commit_id
                brench_name = "none"
            if brench == "master":
                master = self.commit_id
            date = datetime.now()
            message = self.message
            with open(path_file_commit_id, "w") as commit_id_file:
                commit_id_file.write(f"parent = {parent} \n date = {date} \n message = The {message}")
            if brench_name == "none":
                with open(self.references, "w") as refrence:
                    refrence.write(f"HEAD = {self.commit_id} \n master = {master} ")
            elif brench == brench_name and brench_id == parent:
                with open(self.references, "w") as refrence:
                    refrence.write(f"HEAD = {self.commit_id} \n master = {master} \n {brench_name} = {self.commit_id}")
            else:        
                with open(self.references, "w") as refrence:
                    refrence.write(f"HEAD = {self.commit_id} \n master = {master} \n {brench_name} = {self.commit_id}")
            source = self.relitve_path / "staging_area"
            destanation = path_comit_id
            self.copying(source, destanation)

    def copying(self, source: os.PathLike, destanation: os.PathLike) -> None:
        source = source
        destanation = destanation
        for path in source.iterdir():
            if path.is_dir():
                shutil.copytree(path, str(destanation) + "\\" + path.name)
            else:
                shutil.copy(path, destanation)
        
    def is_wit(self, path: os.PathLike | None=None) -> None | os.PathLike:   
        if path is None:
            current_path = Path.cwd()
        else:
            current_path = Path(path)
        while current_path != current_path.parent:
            if len(list(current_path.rglob("*.wit"))) > 0:
                relitve_path = current_path / ".wit"
                return relitve_path 
            else:      
                current_path = current_path.parent
        return None


if __name__ == "__main__":
    Commit(sys.argv[1]).commit()