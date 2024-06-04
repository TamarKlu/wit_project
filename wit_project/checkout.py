#Upload 174
import typing

import filecmp
import os
import logging
from pathlib import Path
import shutil
import sys
from typing import Tuple


class Cheackout():
    def __init__(self, commend: str, current_path: os.PathLike | None=None):
        if current_path is None:
            self.relitve_path = self.is_wit(Path.cwd(

            ))
        else:
            self.relitve_path = self.is_wit(current_path)
        self.currnt_diroctory = self.relitve_path.parent
        self.commend = commend
        self.staging_area = self.relitve_path / "staging_area"
        self.references = self.relitve_path / "references.txt"
        self.brench = None
    
    def which_commend(self) -> Tuple[str, str, str, str]:
        brench_name = None
        brench = None
        with open(self.references, "r") as txt:
            txt = txt.read()
            txt = txt.split()
            master = txt[5]
            commit_id_ref = txt[2]
            if len(txt) > 6:
                brench = txt[-1]
                brench_name = txt[6]           
        if self.commend == "commit_id":
            commit_id = commit_id_ref
        elif self.commend == brench_name:
            commit_id = brench
        elif self.commend == "master":
            commit_id = master
        else:
            return None
        return (commit_id, master, brench, brench_name)

    def checking_before_checkout(self) -> bool | None:
        status1 = Status(self.commit_id)
        status1.status()
        Changes_to_be_committed = status1.Changes_to_be_committed
        Changes_not_staged_for_commit = status1.Changes_not_staged_for_commit
        logging.debug("the file txt will always be in changes to be commited because it will be in the commit file but not in the staging area.") 
        if len(Changes_not_staged_for_commit) == 0 and len(Changes_to_be_committed) == 1 and self.relitve_path is not None:
            return True
            
    def checkout(self) -> None:
        if self.which_commend() is None:
            return "wrong commend"
        else:
            self.commit_id, self.master, self.brench, self.branch_name = self.which_commend()
        self.commit_path = self.relitve_path / "images" / self.commit_id
        logging.info("erasing files in the directory")
        if self.checking_before_checkout():
            for paths in self.currnt_diroctory.rglob("*"):
                for copied in self.commit_path.rglob("*"):
                    if copied.name == paths.name and paths.is_dir() and paths.is_dir() and ".wit" not in str(paths):
                        shutil.rmtree(paths)
                    elif paths.name == copied.name and copied.is_file() and copied.is_file() and ".wit" not in str(paths):
                        os.unlink(paths)
            logging.info("copying files to directory")
            for copied in self.commit_path.iterdir():
                if copied.is_dir():
                    shutil.copytree(copied, (str(self.currnt_diroctory) + "\\" + copied.name))
                else:
                    shutil.copy(copied, self.currnt_diroctory)
        logging.info("updating references file and activted file if nececssarry")
        self.update()
        
    def update(self) -> None:
        if self.brench is not None:
            with open(self.references, "w") as txt_write:
                txt_write.write(f"HEAD = {self.commit_id} \n master = {self.master} \n {self.branch_name} = {self.brench}")
        else:
            with open(self.references, "w") as txt_write:
                txt_write.write(f"HEAD = {self.commit_id} \n master = {self.master} \n ")

        activted = self.relitve_path / "activted.txt"
        if self.brench is not None and self.commend != "master":
            with open(activted, "w") as activted:
                activted.write(f"{self.branch_name}")
        elif self.commend == "master":
            with open(activted, "w") as activted:
                activted.write("master")

    def is_wit(self, path: os.PathLike) -> None | os.PathLike:   
        current_path = path
        while current_path != current_path.parent:
            if len(list(current_path.rglob("*.wit"))) > 0:
                relitve_path = current_path / ".wit"
                return relitve_path 
            else:      
                current_path = current_path.parent
        return None


class Status:
    def __init__(self, commit_id: str) -> None:
        self.Changes_to_be_committed = []
        self.Untracked_files = [] 
        self.Changes_not_staged_for_commit = [] 
        self.relitve_path = self.is_wit(Path.cwd())
        self.currnt_diroctory = self.relitve_path.parent
        self.checking_commit_id = commit_id
    
    def status(self) -> str:
        if self.relitve_path is not None:
            commit_path = self.relitve_path / "images" / self.checking_commit_id
            staging_area = self.relitve_path / "staging_area"        
            files_in_relitve_path = {file.name for file in self.relitve_path.rglob("*")}
            files_in_staging_area = {file.name for file in staging_area.rglob("*")}
            self.Untracked_files = list(files_in_relitve_path.difference(files_in_staging_area))
            for path in self.currnt_diroctory.rglob("*"):
                for copied in staging_area.rglob("*"):
                    if copied.name == path.name and copied.is_dir() and path.is_dir():
                        files_changed = filecmp.dircmp(path, copied) 
                        for file in files_changed.diff_files:
                            self.Changes_not_staged_for_commit.append(file)
            files_in_commit = {file.name for file in commit_path.rglob("*")}
            self.Changes_to_be_committed = list(files_in_commit.difference(files_in_staging_area)) 
            return f"Changes to be committed: {self.Changes_to_be_committed} \n  Changes not staged for commit: {self.Changes_not_staged_for_commit} \n Untracked files: {self.Untracked_files}" 

    def is_wit(self, path: None | os.PathLike) -> None | os.PathLike:   
        current_path = path
        while current_path != current_path.parent:
            if len(list(current_path.rglob("*.wit"))) > 0:
                relitve_path = current_path / ".wit"
                return relitve_path 
            else:      
                current_path = current_path.parent
        return None


if __name__ == "__main__":
    Cheackout(sys.argv[1]).checkout()
    