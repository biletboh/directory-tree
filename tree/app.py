from .directory_tree import AbstractDirectoryTree
from typing import Optional


class App:
    """
    The App
    """

    def __init__(self, tree: AbstractDirectoryTree):
        """
        Initializes app with the directory tree.

        Args:
            tree:
                A directory tree data structure.
        """
        self.tree = tree

    def create(self, command, path):
        print(f"{command} {path}")
        parsed_path = path.split("/")
        self.tree.create(parsed_path)

    def delete(self, command, path):
        print(f"{command} {path}")
        parsed_path = path.split("/")
        self.tree.delete(parsed_path)

    def move(self, command, path_from, path_to):
        print(f"{command} {path_from} {path_to}")
        parsed_path_from = path_from.split("/")
        parsed_path_to = path_to.split("/")
        self.tree.move(parsed_path_from, parsed_path_to)

    def list(
        self,
        command: str,
        depth: int = 0,
        root: Optional[list] = None,
    ):
        if command:
            print(command)
        if root is None:
            data = self.tree.list()
            root = data["subdirs"]
            generated_list = self.generate_list(root=root)
            for node in generated_list:
                print(node)

    def generate_list(
        self,
        depth: int = 0,
        root: list = [],
    ):
        for node in root:
            tab = "  " * depth
            name = node["name"]
            yield f"{tab}{name}"
            if node["subdirs"]:
                yield from self.generate_list(
                    depth=depth + 1, root=node["subdirs"]
                )
