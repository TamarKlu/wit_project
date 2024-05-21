#Upload 171
import os
import logging
from pathlib import Path
import shutil



def add(path: str, current_diractory: os.PathLike | None=None) -> None:
    if current_diractory is None:
        current_diractory = Path.cwd()
    else:
        current_diractory = Path(current_diractory)
    path_to_add = current_diractory / Path(path)
    relitve_path = is_wit(path_to_add)
    destanation = relitve_path / "staging_area"
    logging.info('Preparing to copy the requested files to the staging area, if a wit folder exist')
    if relitve_path is not None:
        if path_to_add.is_dir():
            shutil.copytree(path_to_add, str(destanation) + "\\" + path_to_add.name, ignore=shutil.ignore_patterns(".wit"))
            with open (current_diractory / "help", "w" ) as help:
                help.write( "copy tree")
        else:
            shutil.copy(path_to_add, destanation)
            with open (current_diractory / "help", "w" ) as help:
                help.write( "copy")
    logging.info('The requested files were copied')
     

def is_wit(path: os.PathLike) :   
    current_path = path
    while current_path != current_path.parent:
        if len(list(current_path.rglob("*.wit"))) > 0:
            relitve_path = current_path / ".wit"
            with open (relitve_path  / "help", "a" ) as help:
                help.write( "wtf")
            return relitve_path 
        else:      
            current_path = current_path.parent
    return None


if __name__ == "__main__":
    add()




