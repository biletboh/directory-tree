from abc import ABC, abstractmethod
from collections import UserDict
from typing import Optional


class AbstractDirectoryTree(ABC):
    """
    The blueprint for DirectoryTree data structure.

    The class enforces implementation of basic methods of
    data structure such as create, delete, move, and list.
    """

    @abstractmethod
    def create(self, path: str):
        """
        Implement method to insert nodes to the tree.
        """
        pass

    @abstractmethod
    def delete(self, path: str):
        """
        Implement method to remove nodes from the tree.
        """
        pass

    @abstractmethod
    def move(self, path: str):
        """
        Implement method to cut and paste nodes within the tree.
        """
        pass

    @abstractmethod
    def list(self):
        """
        Implement method to retrieve nodes of the tree.
        """
        pass


class Node:
    """
    The class that defines nodes of DirectoryTree.

    Attributes:
        name: str that stores directory names.
        subdirs: list of directory subdirectories.
    """

    def __init__(self, name: str = ""):
        """
        Initializes node and sets node's name and subdirs.

        Args:
            name:
                str representing node's name.
        """
        self.name = name
        self.subdirs = {}


class DirectoryTree(AbstractDirectoryTree):
    """
    The DirectoryTree is data structure that consist of root node that
    store nodes as subdirs that may contain other subdirs.

    This data structures imitates the behavior of the os directory tree.

    The class iherites from AbstractDirectoryTree and implements methods
    such as create, delete, move, and list.

    The class is responsible for data management.
    """

    def __init__(self):
        self._data = Node()

    def create(
        self,
        path: list,
    ):
        """
        Recursively add nodes to the directory tree.

        Args:
            path:
                A list representing a branch of the directory tree.
            depth:
                An int representing depth of the branch.
            root:
                A list that points to a parent node. If None root should
                default to the first node of the directory tree.
        """
        node = self._data
        for directory in path:
            if directory in node.subdirs:
                node = node.subdirs[directory]
            else:
                new_node = Node(name=directory)
                node.subdirs[directory] = new_node
                node = new_node
        return None

    def delete(
        self,
        path: list,
        depth: int = 0,
        root: Optional[list] = None,
    ):
        """
        Recursively remove nodes to the directory tree.

        Args:
            path:
                A list representing a branch of the directory tree.
            depth:
                An int representing depth of the branch.
            root:
                A list that points to a parent node. If None root should
                default to the first node of the directory tree.

        Returns:
            None or recursive call the method.

        Raises:
            ValueError: node does not exist.
        """
        if root is None:
            root = self._data["subdirs"]
        if len(path) > depth:
            if not any(path[depth] == d["name"] for d in root):
                raise ValueError(f"{path[depth]} does not exist")
            for i, d in enumerate(root):
                if d["name"] == path[depth]:
                    if len(path) == depth + 1:
                        return root.pop(i)
                    else:
                        new_root = root[i]["subdirs"]
                        return self.delete(
                            path, depth=depth + 1, root=new_root
                        )
        return None

    def move(
        self,
        path_from: list,
        path_to: list,
    ):
        """
        Recursively cuts and pastes nodes within the directory tree.

        Args:
            path_from:
                A list representing a branch of the directory tree
                where method must cut a node.
            path_to:
                A list representing a branch of the directory tree
                where method must paste a node.

        Returns:
            None.

        Raises:
            ValueError: node does not exist.
        """
        node = self.delete(path=path_from)
        path_to.append(node["name"])
        self.create(path=path_to, insert=node["subdirs"])
        return None

    def list(self):
        """
        Displays the directory tree data.

        Returns:
            A dict with the directory tree data.
        """
        return self._data

    def sort_by_name(self, e):
        return e["name"]
