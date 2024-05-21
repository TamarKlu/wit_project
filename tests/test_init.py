import wit_project.init
import os
from . import conftest

def test_init(path_folder):
    number_of_dirs_before = len(os.listdir(path_folder))
    wit_project.init.init(path_folder)
    number_of_dirs_later = len(os.listdir(path_folder))
    assert number_of_dirs_before + 1 == number_of_dirs_later


