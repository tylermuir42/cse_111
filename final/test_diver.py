import pytest
from unittest.mock import patch
from diver import random_stratagem_loadout, calculate_success_rate

#Using unittest mock to check the logic
#behind the random stragagem function
@patch('diver.read_log')
@patch('diver.random.sample')
def test_random_strategem_loadout(mock_sample, mock_read_log, capsys):
    #Mock the CSV data
    mock_read_log.return_value = {
        'Eagle Airstrike': ['data'],
        'Orbital Laser': ['data'],
        'Shield Generator': ['data'],
        'Resupply': ['data'],
        'Machine Gun': ['data']
    }

    #Mock the random sample to return a
    #fixed selection
    mock_sample.return_value = [
        ('Eagle Airstrike', ['data']),
        ('Shield Generator', ['data']),
        ('Resupply', ['data']),
        ('Machine Gun', ['data'])
    ]

    random_stratagem_loadout()
    captured = capsys.readouterr()
    output_lines = captured.out.strip().split('\n')

    #Check the output matches the mocked sample
    assert output_lines == [  
        'Eagle Airstrike',
        'Shield Generator',
        'Resupply',
        'Machine Gun',
    ]


#Using unittest mock to make a fake dictionary to check
#whether or not it works
@patch('diver.read_log')
@patch('diver.WIN_INDEX', 1)
@patch('diver.DATE_INDEX', 0)
def test_calculate_success_rate(mock_read_log, capsys):
    #Mock the return value of read_log
    mock_read_log.return_value = {     
        '2025-07-01': ['data', 'win'],
        '2025-07-02': ['data', 'lose'],
        '2025-07-03': ['data', 'win'],
    }

    calculate_success_rate()
    captured = capsys.readouterr()
    assert "Win/Lose ratio: 0.67" in captured.out


#Call to my actual file
pytest.main(["-v", "--tb=line", "-rN", __file__])