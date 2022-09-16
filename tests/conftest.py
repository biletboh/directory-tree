import pytest


@pytest.fixture
def node(name=""):
    return {"name": name, "subdirs": []}


@pytest.fixture
def tree_data():
    return {
        "name": "",
        "subdirs": [
            {
                "name": "vegetables",
                "subdirs": [
                    {
                        "name": "potato",
                        "subdirs": [],
                    },
                ],
            },
            {
                "name": "spices",
                "subdirs": [],
            },
            {
                "name": "drinks",
                "subdirs": [],
            },
        ],
    }
