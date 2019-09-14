import unittest

from hw_app import hello_world_print


def test_forbidden_first():
    forbidden_first = ('bye', 'goodbye', 'farewell')
    first_word = hello_world_print.get_just_word()
    assert first_word not in forbidden_first


def test_forbidden_second():
    forbidden_second = ('city', 'town', 'earth', 'ERROR')
    second_word = hello_world_print.get_db_word()
    assert second_word not in forbidden_second


def test_phrase_len():
    phrase = hello_world_print.get_phrase()
    assert len(phrase) == 11
