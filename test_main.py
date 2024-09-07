import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from main import extract_dummy_data, extract_api_data, transform, quality_assurance, load

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'London', 'Paris']
    })

def test_extract_dummy_data():
    result = extract_dummy_data()
    assert isinstance(result, pd.DataFrame)
    assert len(result) > 0
    assert 'name' in result.columns
    assert 'age' in result.columns

@patch('main.requests.get')
def test_extract_api_data(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30}
    ]
    mock_get.return_value = mock_response

    result = extract_api_data()
    assert isinstance(result, list)
    assert len(result) == 2
    assert 'name' in result[0] and 'age' in result[0]

def test_transform(sample_data):
    result = transform(sample_data)
    assert 'birth_year' in result.columns
    assert all(result['birth_year'] == 2023 - result['age'])
    assert all(result['name'].str.isupper())

def test_quality_assurance():
    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Alice'],
        'age': [25, 30, 25],
        'city': ['New York', 'London', 'New York']
    })
    result = quality_assurance(df)
    assert len(result) == 2  # Duplicates removed

@patch('main.pd.DataFrame.to_csv')
@patch('main.pd.DataFrame.to_json')
def test_load(mock_to_json, mock_to_csv, sample_data):
    load(sample_data, 'output')
    mock_to_csv.assert_called_once_with('output.csv', index=False)
    mock_to_json.assert_called_once_with('output.json', orient='records')

# Add more tests as needed