import filecmp
from pathlib import Path


def status():
    relitve_path = is_wit()
    if relitve_path != "":
        staging_area = relitve_path / ".wit" /"staging_area"
        Changes_to_be_committed = []
        if (relitve_path / ".wit" / "references.txt").exists():
            with open(relitve_path / ".wit" / "references.txt", "r") as txt:
                txt = txt.read()
                txt = txt.split(" ")
                commit_id = txt[2]
            commit_path = relitve_path / ".wit" / "images" / commit_id
            for path in staging_area.rglob("*"):
                if not (commit_path / path.name).exists():
                    Changes_to_be_committed.append(path.name)
        Untracked_files = []
        files_in_relitve_path = {file.name for file in relitve_path.rglob("*") if "wit" not in str(file)}
        files_in_staging_area = {file.name for file in staging_area.rglob("*")}
        Untracked_files= list(files_in_relitve_path.difference(files_in_staging_area))
        Changes_not_staged_for_commit = []
        for path in relitve_path.rglob("*"):
            for copied in staging_area.rglob("*"):
                if copied.name == path.name and copied.is_dir() and path.is_dir():
                    files_changed = filecmp.dircmp(path, copied) 
                    for file in files_changed.diff_files:
                        Changes_not_staged_for_commit.append(file)
            return Changes_to_be_committed ,Changes_not_staged_for_commit ,Untracked_files 
    
    
def is_wit():
    relitve_path = ""
    path = Path(r"C:\Users\User\Downloads\week01")
    path_while = path
    while path_while != path_while.parent:
        for p in path_while.iterdir():
            if p.name == ".wit":
                relitve_path = path_while
                return relitve_path
        if relitve_path == "":        
            path_while = path_while.parent
    return False


if __name__ == "__main__":
    print(status())


