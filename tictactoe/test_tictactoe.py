from tictactoe import player

X = "X"
O = "O"
EMPTY = None


def test_player():
    assert (
        player([[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]])
        == X
    )


def test_player1():
    assert (
        player([[X, EMPTY, X], [EMPTY, O, EMPTY], [EMPTY, EMPTY, EMPTY]]) == O
    )


def test_player2():
    assert player([[X, O, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]) == X
    

def test_player3():
    assert player([[X, O, EMPTY], [EMPTY,])]
                                   