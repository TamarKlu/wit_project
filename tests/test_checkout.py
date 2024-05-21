import filecmp
from pathlib import Path
import wit_project.checkout
from . import conftest


def checkout_test(path_folder):
    refrence_before = path_folder / ".wit" / "references.txt"
    wit_project.checkout.Cheackout("master").checkout()
    refrences_after = path_folder / ".wit" / "references.txt"
    assert filecmp.cmp(refrence_before, refrences_after) == False