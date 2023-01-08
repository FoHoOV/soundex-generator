from __future__ import annotations
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
        return f"Soundex(word={self.word}, soundex={self.soundex}"

    def update(self, new_soundex: str) -> Soundex:
        self.soundex = new_soundex
        return self


def update_soundex_list(soundexes: list[Soundex], update_func: Callable[[str], str]):
    for i in range(len(soundexes)):
        soundexes[i].update(soundexes[i][0].upper() + update_func(soundexes[i][1:]))


def update_soundex_list_with_regex(soundexes: list[Soundex], pattern: str, update_func: Callable[[re.Pattern, str], str]):
    regex = re.compile(pattern, re.IGNORECASE)
    update_soundex_list(soundexes, lambda value: update_func(regex, value))


# replace any of ['A', E', 'I', 'O', 'U', 'H', 'W', 'Y'] with 0
def change_vowels_to_0(soundexes: list[Soundex]):
    update_soundex_list_with_regex(soundexes, r"""[AEIOUHWY]""", lambda regex, value: regex.sub("0", value))


# performs this operation
# B, F, P, V → 1
# C, G, J, K, Q, S, X, Z → 2
# D,T → 3
# L → 4
# M, N → 5
# R → 6
def change_letters_to_digits(soundexes: list[Soundex]):
    update_soundex_list_with_regex(soundexes, r"[BFPV]", lambda regex, value: regex.sub("1", value))
    update_soundex_list_with_regex(soundexes, r"[CGJKQSXZ]", lambda regex, value: regex.sub("2", value))
    update_soundex_list_with_regex(soundexes, r"[DT]", lambda regex, value: regex.sub("3", value))
    update_soundex_list_with_regex(soundexes, r"L", lambda regex, value: regex.sub("4", value))
    update_soundex_list_with_regex(soundexes, r"[MN]", lambda regex, value: regex.sub("5", value))
    update_soundex_list_with_regex(soundexes, r"R", lambda regex, value: regex.sub("7", value))


def remove_consecutive_digits(soundexes: list[Soundex]):
    update_soundex_list_with_regex(soundexes, r"""(\d)\1+""", lambda regex, value: regex.sub(r"\1", value))


def remove_all_zeros(soundexes: list[Soundex]):
    update_soundex_list_with_regex(soundexes, r"""0""", lambda regex, value: regex.sub(r"", value))


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
