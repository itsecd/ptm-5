import pytest
import os
from utils import InterfaceFileOperation

@pytest.fixture
def intervace() -> InterfaceFileOperation:
    """
    The function for creating an instance InterfaceFileOperation for testing
    Returns InterfaceFileOperation
    """
    return InterfaceFileOperation()



def test_cmp_folder(intervace: InterfaceFileOperation, tmp_path):
    a = tmp_path.mkdir("src_folder").join("myfile")
    b = tmp_path.mkdir("dst_folder").join("myfile")
    assert intervace.cmp_folder(a.dirname, b.dirname)

# def test_something_else(tmp_path):
#     #create a file handle for "myfile" in "mydir" in temp folder
#     f1 = tmp_path.mkdir("mydir").join("myfile")

    
#     assert os.path.exists(f1.dirname)

if __name__ == '__main__':
    pytest.main(["-v", "-color=yes"])