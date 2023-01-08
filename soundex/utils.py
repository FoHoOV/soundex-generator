from collections import defaultdict

from soundex import soundex_generator


def find_same_soundex_values(soundexes: list[soundex_generator.Soundex]) -> [soundex_generator.Soundex]:
    result = defaultdict(list)
    for soundex in soundexes:
        result[soundex.soundex].append(soundex.word)
    return list(((key, locs) for key, locs in result.items() if len(locs) > 1))
