import pytest
import requests


@pytest.mark.parametrize('num1, num2', [('str', 'string'),  # string
                                        ('123', '22'),  # int string
                                        ([12, 1], [123]),  # list
                                        (0.12, 8.93),  # float
                                        (-10, -1),  # negative int
                                        (-1.23, -10.0)])  # negative float
def test_all_wrong_input(num1, num2):
    # check that input parameters are wrong
    response = requests.post('http://0.0.0.0:8080/calc', json={"number1": num1, "number2": num2})
    assert response.status_code == 422

    # check that number of invalid parameters is two
    error_messages = response.json().get('detail')
    assert len(error_messages) == 2


@pytest.mark.parametrize('num1, num2', [(1, 'string'), (1, '22'), (1, [123]), (1, 8.93), (1, -1), (1, -10.0),
                                        ('str', 0), ('123', 0), ([12, 1], 0), (0.12, 0), (-10, 0), (-1.23, 0)])
def test_one_wrong_input(num1, num2):
    # check that input parameters are wrong
    response = requests.post('http://0.0.0.0:8080/calc', json={"number1": num1, "number2": num2})
    assert response.status_code == 422

    # check that number of invalid parameters is two
    error_messages = response.json().get('detail')
    assert len(error_messages) == 1


@pytest.mark.parametrize('num1, num2', [(n1, n2) for n1, n2 in enumerate(range(10), start=1)])
def test_ok_input(num1, num2):
    # check that input parameters are right
    response = requests.post('http://0.0.0.0:8080/calc', json={"number1": num1, "number2": num2})
    assert response.status_code == 200

    result_value = response.json().get('result')
    assert num1 + num2 == result_value
