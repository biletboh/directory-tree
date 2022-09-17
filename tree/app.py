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

    def read_commands(self, file):
        with open(file, "r") as reader:
            for command in reader.readlines():
                self.run_command(command)

    def run_command(self, command):
        command = command.strip()
        print(command)
        command, path1, path2 = self.parse(command)
        if command == "CREATE":
            self.create(path1)
        elif command == "DELETE":
            self.delete(path1)
        elif command == "MOVE":
            if path2:
                self.move(path1, path2)
        elif command == "LIST":
            self.list()

    def parse(self, command: str):
        parsed_command = command.split(" ")
        command = parsed_command[0]
        if len(parsed_command) > 1:
            path1 = parsed_command[1].split("/")
        else:
            path1 = None
        if len(parsed_command) > 2:
            path2 = parsed_command[2].split("/")
        else:
            path2 = None
        return command, path1, path2

    def create(self, path: list):
        self.tree.create(path)

    def delete(self, path: list):
        try:
            self.tree.delete(path)
        except ValueError as e:
            path = "/".join(path)
            print(f"Cannot delete {path} - {e}")

    def move(self, path_from: list, path_to: list):
        self.tree.move(path_from, path_to)

    def list(
        self,
        depth: int = 0,
        root: Optional[list] = None,
    ):
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
