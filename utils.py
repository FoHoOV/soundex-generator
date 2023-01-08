from collections import defaultdict

import soundex


class Result:
    pass


def find_same_soundex_values(soundexes: [soundex.Soundex]) -> [Result]:
    result = defaultdict(list)
    for soundex in soundexes:
        result[soundex.soundex].append(soundex.word)
    return list(((key, locs) for key, locs in result.items() if len(locs) > 1))
