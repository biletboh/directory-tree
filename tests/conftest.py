import pytest


@pytest.fixture
def node(name=""):
    return {"name": name, "subdirs": {}}


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
                    {
                        "name": "juice",
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
                "subdirs": [
                    {
                        "name": "hot",
                        "subdirs": [],
                    },
                    {
                        "name": "cold",
                        "subdirs": [
                            {
                                "name": "lemonade",
                                "subdirs": [],
                            },
                            {
                                "name": "beer",
                                "subdirs": [],
                            },
                        ],
                    },
                ],
            },
        ],
    }
