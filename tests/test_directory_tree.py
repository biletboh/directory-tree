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
    assert "fruits" == tree.data["subdirs"][0]["name"]
    assert "apples" == tree.data["subdirs"][0]["subdirs"][0]["name"]
