from abc import ABC, abstractmethod


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

    def create(self, path: list, insert: dict = {}):
        """
        Recursively add nodes to the directory tree.

        Args:
            path:
                A list representing a branch of the directory tree.
        """
        node = self._data
        for directory in path:
            if directory in node.subdirs:
                node = node.subdirs[directory]
            else:
                new_node = Node(name=directory)
                node.subdirs[directory] = new_node
                node = new_node
        if insert:
            node.subdirs = insert
        return None

    def delete(self, path: list):
        """
        Recursively remove nodes to the directory tree.

        Args:
            path:
                A list representing a branch of the directory tree.
        Returns:
            Removed node.

        Raises:
            ValueError: node does not exist.
        """
        node = self._data
        depth = len(path)
        for i, directory in enumerate(path):
            if directory in node.subdirs:
                if depth == i + 1:
                    removed = node.subdirs.pop(directory)
                    return removed
                node = node.subdirs[directory]
            else:
                raise ValueError(f"{directory} does not exist")
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
        path_to.append(node.name)
        self.create(path=path_to, insert=node.subdirs)
        return None

    def list(self):
        """
        Displays the directory tree data.

        Returns:
            A dict with the directory tree data.
        """
        return self._data
