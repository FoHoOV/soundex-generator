from pprint import pprint

from soundex import html_parser, tokenizer, soundex_generator, utils


def main(show_same_soundexes_only: bool):
    # I count special characters such as @ and _ as normal characters that words can start with for exp: _what is a valid token
    # but the soundex generator filters the tokens by calling token.isalpha()
    raw_text = html_parser.get_text_from_url(html_parser.TEST_URL)
    tokens = tokenizer.extract_tokens(raw_text)
    soundexes = soundex_generator.generate_soundexes(tokens)
    if show_same_soundexes_only:
        pprint(utils.find_same_soundex_values(soundexes))
    else:
        pprint(soundexes)


if __name__ == "__main__":
    main(True)
