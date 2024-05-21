import os
from pathlib import Path
import wit_project.commit
from . import conftest


def test_commit(path_folder):
    images = Path(path_folder) / ".wit" / "images"
    len_before = len(os.listdir(images))
    wit_project.commit.Commit("checking commit", path_folder).commit()
    len_after = len(os.listdir(images))
    assert len_before + 1 == len_after