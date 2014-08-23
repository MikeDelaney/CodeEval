from array_absurdity import array_absurdity


def test_array_absurdity_ex1():
    input_list = ['0', '1', '2', '3', '0']
    assert array_absurdity(input_list) == '0'


def test_array_absurdity_ex2():
    input_list = ['0', '1', '10', '3', '2', '4', '5', '7', '6', '8',
                  '11', '9', '15', '12', '13', '4', '16', '18', '17', '14']
    assert array_absurdity(input_list) == '4'
