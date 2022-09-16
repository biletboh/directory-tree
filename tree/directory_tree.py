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


class Node(UserDict):
    """
    The class that defines nodes of DirectoryTree.

    Attributes:
        data: A dict that stores node name as str and subdirs as list.
    """

    def __init__(self, *args, name: str = "", **kwargs):
        """
        Initializes node and sets node's name and subdirs.

        Args:
            name:
                A string representing node's name.
        """
        super().__init__(*args, name=name, **kwargs)
        self.data["name"] = name
        self.data["subdirs"] = []


class DirectoryTree(AbstractDirectoryTree):
    """
    The DirectoryTree is data structure that consist of root node that
    store nodes as subdirs that may contain other subdirs.

    This data structures imitates the behavior of the os directory tree.

    The class iherites from AbstractDirectoryTree and implements methods
    such as create, delete, move, and list.

    """

    def __init__(self):
        self.data = Node()

    def create(
        self,
        path: list,
        depth: int = 0,
        root: Optional[list] = None,
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
        if root is None:
            root = self.data["subdirs"]
        if len(path) > depth:
            if not any(path[depth] == d["name"] for d in root):
                root.append(Node(name=path[depth]))
            for i, d in enumerate(root):
                if d["name"] == path[depth]:
                    new_root = root[i]["subdirs"]
                    return self.create(path, depth=depth + 1, root=new_root)

    def delete(self, path):
        pass

    def move(self, path):
        pass

    def list(self):
        pass

    # def parse(path: str):
    #     parsed_path = self.parse(path)
    #     pass
