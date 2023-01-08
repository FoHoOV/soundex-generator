import re


def normalize(raw_tokens: [str]) -> set[str]:
    return set([token.lower().replace("'","").replace("\"","") for token in raw_tokens])


def extract_words(raw_text: str) -> [str]:
    return re.findall(r"""@?\w+['"]?\w+""", raw_text)


def extract_tokens(raw_text: str) -> [str]:
    words = extract_words(raw_text)
    normalized_tokens = normalize(words)
    return normalized_tokens
