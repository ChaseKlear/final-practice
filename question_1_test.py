from question_1 import Card

def card_values_test(rank: int, suit: str, expected_rank: int, expected_suit: str, expected_name: str, expected_shorthand: str):
    obj = Card(rank, suit)
    actual_rank = obj.get_rank()
    actual_suit = obj.get_suit() if obj._Card__suit else ''
    actual_name = obj.get_name() if obj._Card__name else ''
    actual_shorthand = obj.get_shorthand() if obj._Card__shorthand else ''

    assert actual_rank == expected_rank
    assert actual_suit.lower() == expected_suit.lower()
    assert actual_shorthand.lower() == expected_shorthand.lower()
    assert actual_name.lower() == expected_name.lower()


SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANK_TO_NAME = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}


def test_q1_card_lessthan_10():
    for suit in SUITS:
        for rank in range(2, 10):
            card_values_test(rank, suit, rank, suit, f'{rank} of {suit}', f'{rank}{suit[0]}')


def test_q1_card_private():
    '''
    Tests that attributes are private, i.e. have the double underscore prefix
    '''
    obj = Card(3, 'Diamonds')
    rank_str = '_Card__rank'
    suit_str = '_Card__suit'
    name_str = '_Card__name'
    shorthand_str = '_Card__shorthand'
    attribs = dir(obj)
    assert rank_str in attribs
    assert suit_str in attribs
    assert name_str in attribs
    assert shorthand_str in attribs
    assert 'rank' not in attribs
    assert 'suit' not in attribs
    assert 'name' not in attribs
    assert 'shorthand' not in attribs


def test_q1_card_frozen():
    try:
        Card(3, 'Diamonds').some_value = 'Not valid'
        raise AssertionError() from AttributeError('Card object should be frozen.')
    except AttributeError:
        assert True


def test_q1_card_10():
    for suit in SUITS:
        card_values_test(10, suit, 10, suit, f'10 of {suit}', f'10{suit[0]}')


def test_q1_card_greaterthan_10():
    for suit in SUITS:
        for rank in range(11, 15):
            card_values_test(rank, suit, rank, suit, f'{RANK_TO_NAME[rank]} of {suit}', f'{RANK_TO_NAME[rank][0]}{suit[0]}')


def test_q1_card_repr():
    for suit in SUITS:
        for rank in range(2, 15):
            expected_prefix = '\u001b[31;1m'
            if suit in {'Clubs', 'Spades'}:
                expected_prefix = '\u001b[36;1m'
            expected_suffix = '\u001b[0m'
            actual = repr(Card(rank, suit))
            assert expected_prefix in actual
            assert expected_suffix in actual


def test_q1_card_sort():
    c1 = Card(3, 'Diamonds')
    c2 = Card(14, 'Clubs')
    c3 = Card(9, 'Spades')
    c4 = Card(10, 'Hearts')
    actual = str(sorted([c1, c2, c3, c4]))
    expected = '[\u001b[36;1mAC\u001b[0m, \u001b[31;1m10H\u001b[0m, \u001b[36;1m9S\u001b[0m, \u001b[31;1m3D\u001b[0m]'
    assert actual == expected


def test_q1_card_set():
    c1 = Card(3, 'Diamonds')
    c2 = Card(3, 'Diamonds')
    c3 = Card(14, 'Clubs')
    c4 = Card(9, 'Spades')
    c5 = Card(10, 'Hearts')
    actual = {c1, c2, c3, c4, c5}
    expected = {c1, c3, c4, c5}
    assert len(actual & expected) == 4
    assert len(actual ^ expected) == 0
    assert actual == expected
