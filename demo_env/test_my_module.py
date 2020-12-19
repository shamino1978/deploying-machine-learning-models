from mymod import square

import pytest

'''
@pytest.fixture
def input_value():
	return 4
'''
@pytest.mark.parametrize(
	'inputs',[2,3,4,5]
	)


def test_square_gives_correct_value(inputs):
	#when
	subject=square(inputs)

	#then
	assert subject==16
	
