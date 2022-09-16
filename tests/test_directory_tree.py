import pytest

from tree.directory_tree import (
    AbstractDirectoryTree,
    DirectoryTree,
    Node,
)


@pytest.mark.parametrize(
    "method",
    [
        "create",
        "delete",
        "move",
        "list",
    ],
)
def test_abstarct_tree_methods(method):
    """
    Test if AbstractDirectoryTree defines methods for node management.
    """
    assert hasattr(AbstractDirectoryTree, method)
    assert hasattr(
        getattr(AbstractDirectoryTree, method), "__isabstractmethod__"
    )


@pytest.mark.parametrize(
    "name",
    [
        "",
        "fruits",
    ],
)
def test_node(name, node):
    """
    Test if Node initializes dict with name and subdirs keys.
    """
    node["name"] = name
    assert node == Node(name=name)


def test_abstract_issubclass():
    """
    Test if DirectoryTree is subclass of AbstractDirectoryTree.
    """
    assert issubclass(DirectoryTree, AbstractDirectoryTree)


def test_directory_tree_create():
    tree = DirectoryTree()
    path = ["fruits", "apples"]
    tree.create(path)
    assert "fruits" == tree.data["subdirs"][-1]["name"]
    assert "apples" == tree.data["subdirs"][-1]["subdirs"][-1]["name"]


def test_directory_tree_delete(tree_data):
    path = ["vegetables", "potato"]
    tree = DirectoryTree()
    tree.data = tree_data
    tree.delete(path)
    dirnames = {d["name"] for d in tree_data["subdirs"][0]["subdirs"]}
    assert "potato" not in dirnames


def test_directory_tree_delete_value_error(tree_data):
    path = ["drinks", "cars"]
    tree = DirectoryTree()
    tree.data = tree_data
    with pytest.raises(ValueError, match=f"{path[1]} does not exist"):
        tree.delete(path)