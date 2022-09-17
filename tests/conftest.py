import pytest
from tree.directory_tree import Node


@pytest.fixture
def tree_data():
    """
    Populate DirectoryTree with data.
    """
    data = Node()
    data.subdirs["vegetables"] = Node("vegetables")
    data.subdirs["fruits"] = Node("fruits")
    data.subdirs["drinks"] = Node("drinks")
    data.subdirs["vegetables"].subdirs["potatos"] = Node("potatos")
    data.subdirs["vegetables"].subdirs["tomatos"] = Node("tomatos")
    data.subdirs["fruits"].subdirs["apple"] = Node("apple")
    data.subdirs["fruits"].subdirs["apple"].subdirs["cider"] = Node("cider")
    data.subdirs["fruits"].subdirs["apple"].subdirs["cider"].subdirs[
        "homemade"
    ] = Node("homemade")
    return data
