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
    """
    Test if DirectoryTree can create child nodes.
    """
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
    """
    Test if DirectoryTree can delete child nodes.
    """
    path = ["vegetables", "potatos"]
    tree = DirectoryTree()
    tree._data = tree_data
    tree.delete(path)
    assert "potato" not in tree._data.subdirs["vegetables"].subdirs


def test_directory_tree_delete_value_error(tree_data):
    """
    Test if DirectoryTree delete method raises value error
    in cases there is nothing to delete.
    """
    path = ["drinks", "cars"]
    tree = DirectoryTree()
    tree._data = tree_data
    with pytest.raises(ValueError, match=f"{path[1]} does not exist"):
        tree.delete(path)


def test_directory_tree_move(tree_data):
    """
    Test if DirectoryTree can move child elements within the tree.
    """
    path_from = ["fruits", "apple", "cider"]
    path_to = ["drinks"]
    tree = DirectoryTree()
    tree._data = tree_data
    tree.move(path_from, path_to)
    assert "cider" not in tree._data.subdirs["fruits"].subdirs["apple"].subdirs
    assert "cider" in tree._data.subdirs["drinks"].subdirs
    assert "homemade" in tree._data.subdirs["drinks"].subdirs["cider"].subdirs


def test_directory_tree_move_value_error(tree_data):
    """
    Check if DirectoryTree move method raises value error
    in case there is no child to move.
    """
    path_from = ["vegetables", "juice"]
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
