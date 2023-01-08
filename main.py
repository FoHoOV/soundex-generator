from pprint import pprint

import html_parser
import soundex
import tokenizer
import utils


def main():
    # I count special characters such as [@, _] as normal characters that words can start with for exp: _salam is a valid token
    raw_text = html_parser.get_text_from_url(html_parser.TEST_URL)
    tokens = tokenizer.extract_tokens(raw_text)
    soundexes = soundex.generate_soundexes(tokens)
    pprint(utils.find_same_soundex_values(soundexes))


if __name__ == "__main__":
    main()
