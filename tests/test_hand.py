
from hand import Hand

def test_empty_hand():
	temp = Hand()
	assert temp.list() == "[]"
