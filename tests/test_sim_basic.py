import pytest
from tests.flo import diff
from game_of_greed.game import Game

pytestmark = [pytest.mark.version_2, pytest.mark.version_3]

def test_quitter():
    game = Game()
    errors = diff(game.play, path="tests/version_2/quitter.txt")
    assert not errors, errors[0]


def test_one_and_done():
    game = Game()
    errors = diff(game.play, path="tests/version_2/one_and_done.txt")
    assert not errors, errors[0]


def test_single_bank():
    game = Game()
    errors = diff(game.play, path="tests/version_2/bank_one_then_quit.txt")
    assert not errors, errors[0]


def test_bank_first_for_two_rounds():
    game = Game()
    errors = diff(game.play, path="tests/version_2/bank_first_for_2_rounds.txt")
    assert not errors, errors[0]