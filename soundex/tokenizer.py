import re


def normalize(raw_tokens: list[str]) -> set[str]:
    return set([token.lower().replace("'","").replace("\"","") for token in raw_tokens])


def extract_words(raw_text: str) -> list[str]:
    return re.findall(r"""@?\w+['"]?\w+""", raw_text)


def extract_tokens(raw_text: str) -> set[str]:
    words = extract_words(raw_text)
    normalized_tokens = normalize(words)
    return normalized_tokens
