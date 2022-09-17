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
def test_node(name):
    """
    Test if Node initializes dict with name and subdirs keys.
    """
    node = Node(name=name)
    assert node.name == name
    assert node.subdirs == {}


def test_abstract_issubclass():
    """
    Test if DirectoryTree is subclass of AbstractDirectoryTree.
    """
    assert issubclass(DirectoryTree, AbstractDirectoryTree)


def test_directory_tree_create():
    tree = DirectoryTree()
    path1 = ["fruits", "apples"]
    path2 = ["fruits", "berries", "strawberries"]
    tree.create(path1)
    tree.create(path2)
    assert "fruits" in tree._data.subdirs
    assert "apples" in tree._data.subdirs["fruits"].subdirs
    assert "berries" in tree._data.subdirs["fruits"].subdirs
    assert (
        "strawberries"
        in tree._data.subdirs["fruits"].subdirs["berries"].subdirs
    )


def test_directory_tree_delete(tree_data):
    path = ["vegetables", "potato"]
    tree = DirectoryTree()
    tree._data = tree_data
    tree.delete(path)
    dirnames = {d["name"] for d in tree_data["subdirs"][0]["subdirs"]}
    assert "potato" not in dirnames


def test_directory_tree_delete_value_error(tree_data):
    path = ["drinks", "cars"]
    tree = DirectoryTree()
    tree._data = tree_data
    with pytest.raises(ValueError, match=f"{path[1]} does not exist"):
        tree.delete(path)


def test_directory_tree_move(tree_data):
    path_from = ["vegetables", "juice"]
    path_to = ["drinks"]
    tree = DirectoryTree()
    tree._data = tree_data
    tree.move(path_from, path_to)
    dirnames_from = {d["name"] for d in tree_data["subdirs"][0]["subdirs"]}
    dirnames_to = {d["name"] for d in tree_data["subdirs"][2]["subdirs"]}
    assert "juice" not in dirnames_from
    assert "juice" in dirnames_to


def test_directory_tree_move_value_error(tree_data):
    path_from = ["spices", "juice"]
    path_to = ["drinks"]
    tree = DirectoryTree()
    tree._data = tree_data
    with pytest.raises(ValueError, match=f"{path_from[1]} does not exist"):
        tree.move(path_from, path_to)


def test_directory_tree_list():
    """
    Test if Node initializes dict with name and subdirs keys.
    """
    tree = DirectoryTree()
    assert tree._data == tree.list()
