from tree.app import App
from tree.directory_tree import DirectoryTree


def test_app_create(mocker):
    mocker.patch("tree.directory_tree.DirectoryTree.create")
    app = App(tree=DirectoryTree())
    path = ["fruits", "apple"]
    app.create(path)
    DirectoryTree.create.assert_called_once()


def test_app_delete(mocker):
    mocker.patch("tree.directory_tree.DirectoryTree.delete")
    app = App(tree=DirectoryTree())
    path = ["fruits", "apple"]
    app.delete(path)
    DirectoryTree.delete.assert_called_once()


def test_app_move(mocker):
    mocker.patch("tree.directory_tree.DirectoryTree.move")
    app = App(tree=DirectoryTree())
    path_from = ["fruits", "apple"]
    path_to = ["vegetables"]
    app.move(path_from, path_to)
    DirectoryTree.move.assert_called_once()


def test_app_list(mocker, tree_data):
    mocker.patch("tree.directory_tree.DirectoryTree.list")
    tree = DirectoryTree()
    tree._data = tree_data
    app = App(tree=tree)
    app.list("LIST")
    DirectoryTree.list.assert_called()


def test_app_list_f(tree_data):
    tree = DirectoryTree()
    tree._data = tree_data
    app = App(tree=tree)
    app.list("LIST")
