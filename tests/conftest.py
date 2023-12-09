import pytest
import pandas as pd


@pytest.fixture()
def input_dicts():
    return {
        "id_left": [1, 2],
        "amount_left": [100, 150],
        "date_left": ["2023-01-01", "2023-01-02"],
    }, {
        "id_right": [1, 3],
        "amount_right": [100, 200],
        "date_right": ["2023-01-01", "2023-01-03"],
    }


@pytest.fixture()
def input_dfs():
    return pd.DataFrame({
        "id": [1, 2],
        "amount": [100, 150],
        "date": ["2023-01-01", "2023-01-02"],
    }), pd.DataFrame({
        "id": [1, 3],
        "amount": [100, 200],
        "date": ["2023-01-01", "2023-01-03"],
    })


@pytest.fixture()
def output_dfs():
    return pd.DataFrame({
        "id": [1],
        "amount": [100],
        "date": ["2023-01-01"],
    }), pd.DataFrame({
        "id": [2],
        "amount": [150],
        "date": ["2023-01-02"],
    }), pd.DataFrame({
        "id": [3],
        "amount": [200],
        "date": ["2023-01-03"],
    })
