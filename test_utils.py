import pytest
import os
import shutil
import zipfile


from utils import InterfaceFileOperation


@pytest.fixture
def intervace() -> InterfaceFileOperation:
    """
    The function for creating an instance InterfaceFileOperation for testing
    Returns InterfaceFileOperation
    """
    return InterfaceFileOperation()


@pytest.fixture()
def create_tmp_dir():
    """ fixture for craete test folder and then remove it"""

    path_dict = {
        "root": "test_folder",
        "src": "test_folder/src",
        "dst": "test_folder/dst",
        "non_exist_src": "test_folder/non_exist_src",
        "non_exist_dst": "test_folder/non_exist_dst",
        "src_1": "test_folder/src_1",
        "file": "test_folder/src/file.txt",
        "file_copy": "test_folder/dst/file.txt",
        "file_rec": "test_folder/src_1/file.txt",
    }
    if os.path.exists(path_dict["root"]):
        shutil.rmtree(path_dict["root"])

    os.mkdir(path_dict["root"])
    os.mkdir(path_dict["src_1"])
    os.mkdir(path_dict["src"])
    os.mkdir(path_dict["dst"])
    with open(path_dict["file"], "w") as file:
        file.write("test")
    yield path_dict

    shutil.rmtree(path_dict["root"])


def test_cmp_folder(intervace: InterfaceFileOperation, create_tmp_dir):
    """test copy folder function"""
    # equal folder
    assert intervace.cmp_folder(
        create_tmp_dir["src_1"], create_tmp_dir["dst"]) == True

    # non exists folder
    assert intervace.cmp_folder(
        create_tmp_dir["non_exist_src"], create_tmp_dir["non_exist_dst"]) == False

    # different folder
    assert intervace.cmp_folder(
        create_tmp_dir["src"], create_tmp_dir["dst"]) == False


def test_full_backup(intervace: InterfaceFileOperation, create_tmp_dir):
    """test copy function"""

    # copy exists
    intervace.full_backup(create_tmp_dir["src"], create_tmp_dir["dst"])
    assert os.path.isfile(create_tmp_dir["file_copy"]) == True

    # copy from non exists
    assert intervace.full_backup(
        create_tmp_dir["non_exist_src"], create_tmp_dir["dst"]) == False


def test_is_dir(intervace: InterfaceFileOperation, create_tmp_dir):
    """test is dir function"""
    assert intervace.is_dir((create_tmp_dir["src"])) == True
    assert intervace.is_dir(create_tmp_dir["non_exist_src"]) == False


def test_rename_folder(intervace: InterfaceFileOperation, create_tmp_dir):
    """test rename function folder"""
    #
    new_name = create_tmp_dir["src_1"][:-1] + "2"
    new_name_2 = create_tmp_dir["non_exist_src"] + "_2"
    assert intervace.rename_folder(new_name, create_tmp_dir["src_1"]) == True
    assert os.path.exists(new_name) == True

    # non exists folders rename
    assert intervace.rename_folder(
        new_name_2, create_tmp_dir["non_exist_src"]) == False
    assert os.path.exists(new_name_2) == False


def test_recover(intervace: InterfaceFileOperation, create_tmp_dir):
    intervace.recover(create_tmp_dir["src"], create_tmp_dir["src_1"])
    assert os.path.exists(create_tmp_dir["file_rec"])


def test_create_name(intervace: InterfaceFileOperation, create_tmp_dir):
    """test create name function"""
    assert intervace.create_name(create_tmp_dir["src"], create_tmp_dir["dst"])


def test_zipping(intervace: InterfaceFileOperation, create_tmp_dir):
    """test zipping function, 
    if input path ith file return path to zip in that folder
    if input zip return itself
    """
    path = intervace.ziping(create_tmp_dir["src"])
    assert zipfile.is_zipfile(path) == True
    assert intervace.ziping(path) == path


if __name__ == '__main__':
    pytest.main(["-v", "-color=yes"])
