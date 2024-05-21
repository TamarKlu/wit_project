from . import conftest
from pathlib import Path
import wit_project.add


def test_add(folder_to_move, path_folder):
    staging_area = Path( path_folder) / ".wit" / "staging_area"
    len_staging_area_before = len(list((staging_area.rglob("*"))))
    wit_project.add.add(folder_to_move, path_folder)
    len_staging_area_after = len(list((staging_area.rglob("*"))))
    assert len_staging_area_before + 1 == len_staging_area_after


