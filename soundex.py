from __future__ import annotations
import dataclasses
import re
from typing import Callable


class Soundex:

    def __init__(self, word: str, soundex: str | None = None):
        self.word = word

        if soundex is None:
            self.soundex = word
            return
        self.soundex = soundex

    def __getitem__(self, index: int) -> str:
        return self.soundex[index]

    def __repr__(self):
        return f"Soundex({self.word=}, {self.soundex}"

    def update(self, new_soundex: str) -> Soundex:
        self.soundex = new_soundex
        return self


def update_soundex_list(soundexes: list[Soundex], update_func: Callable[[str], str]):
    for i in range(len(soundexes)):
        soundexes[i] = soundexes[i].update(soundexes[i][0].upper() + update_func(soundexes[i][1:]))


# replace any of ['A', E', 'I', 'O', 'U', 'H', 'W', 'Y'] with 0
def change_vowels_to_0(soundexes: list[Soundex]):
    vowel_replaces_regex = re.compile(r"""[AEIOUHWY]""", re.IGNORECASE)
    update_soundex_list(soundexes, lambda value: vowel_replaces_regex.sub("0", value))


# performs this operation
# B, F, P, V → 1
# C, G, J, K, Q, S, X, Z → 2
# D,T → 3
# L → 4
# M, N → 5
# R → 6
def change_letters_to_digits(soundexes: list[Soundex]):
    def substitute_characters(soundexes: list[Soundex], characters: str, number: int):
        regex = re.compile(f"[{characters}]", re.IGNORECASE)
        update_soundex_list(soundexes, lambda value: regex.sub(str(number), value))

    substitute_characters(soundexes, "BFPV", 1)
    substitute_characters(soundexes, "CGJKQSXZ", 2)
    substitute_characters(soundexes, "DT", 3)
    substitute_characters(soundexes, "L", 4)
    substitute_characters(soundexes, "MN", 5)
    substitute_characters(soundexes, "R", 6)


def remove_consecutive_digits(soundexes: list[Soundex]):
    regex = re.compile(r"""(\d)\1+""", re.IGNORECASE)
    update_soundex_list(soundexes, lambda value: regex.sub(r"\1", value))


def remove_all_zeros(soundexes: list[Soundex]):
    regex = re.compile(r"""0""", re.IGNORECASE)
    update_soundex_list(soundexes, lambda value: regex.sub(r"", value))


def check_soundexes_lengths(soundexes: list[Soundex]):
    update_soundex_list(soundexes, lambda value: value + "0" * (3 - len(value)) if len(value) < 3 else value[0:3])


def generate_soundexes(tokens: [str]) -> list[Soundex]:
    soundexes = [Soundex(token) for token in tokens]
    change_vowels_to_0(soundexes)
    change_letters_to_digits(soundexes)
    remove_consecutive_digits(soundexes)
    remove_all_zeros(soundexes)
    check_soundexes_lengths(soundexes)
    return soundexes
