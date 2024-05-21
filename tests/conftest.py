
from pathlib import Path
import pytest
import tempfile



@pytest.fixture(scope="session")
def path_folder():
 path = tempfile.gettempdir()
 return path


@pytest.fixture(scope="session")
def folder_to_move():
    folder_to_move = tempfile.mkdtemp()
    name = Path(folder_to_move).name
    return name
