import random
import uuid
import json

COMMON_WORDS_FN = './word-lists/common-words.txt'
VALID_WORDS_FN = './word-lists/valid-words.txt'

def load_words():
    with open(VALID_WORDS_FN, 'r') as f:
        valid_words = f.read().splitlines()
    with open(COMMON_WORDS_FN, 'r') as f:
        common_words = f.read().splitlines()
    return {
        'valid':  [e.lower().strip()  for e in valid_words],
        'common': [e.lower().strip()  for e in common_words],
    }

class UnicodeColors:
    '''https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit'''
    RESET =     '\033[0m'
    GRAY =      '\033[48;5;235m'
    YELLOW =    '\033[48;5;226m'
    GREEN =     '\033[48;5;106m'


class HTMLColors:
    '''https://en.wikipedia.org/wiki/Web_colors#HTML_color_names'''
    RESET =     'white'
    GRAY =      'gray'
    YELLOW =    'yellow'
    GREEN =     'green'


def format_html(letter, state):
    d = {
        "correct":  HTMLColors.GREEN,
        "present":  HTMLColors.YELLOW,
        "absent":   HTMLColors.GRAY,
        "empty":    HTMLColors.RESET
    }
    color = d.get(state, "white")
    if state == "empty":
        letter = "&#x25A1;"
    else:
        letter = letter.upper()
    snippet = f'<span style="background-color: {color}; width: 15px; display: inline-block;">{letter}</span>'
    return snippet


def format_str(letter, state):
    d = {
        "correct":  UnicodeColors.GREEN,
        "present":  UnicodeColors.YELLOW,
        "absent":   UnicodeColors.GRAY,
        "empty":    UnicodeColors.RESET
    }
    color = d.get(state, UnicodeColors.RESET)
    if state == "empty":
        letter = "\u25A1"
    return color + letter.upper() + UnicodeColors.RESET

def grid_to_str(grid_list, formatted=False):
    return "\n".join(
        [
            " ".join( 
                [ 
                    format_str(letter, state) if formatted else letter
                    for (state, letter) in row
                ]
            ) 
            for row in grid_list
        ]
    )

def grid_to_html(grid_list):
    return "<br>".join(
        [
            "".join( 
                [ 
                    format_html(letter, state) 
                    for (state, letter) in row
                ]
            ) 
            for row in grid_list
        ]
    )

class WordleGame:

    def __init__(self,
        word: str = None,         
        word_type: str = 'common',
        ) -> None:
        self.words = load_words()
        if word is not None:
            self.word = word.lower()
        else:
            self.word = random.choice(self.words[word_type])
        self.current_row = 0
        self.grid_state = [
            [('empty', '') for _ in range(5)]
            for _ in range(6)
        ]
        self.b_win = False
        self.uuid = str(uuid.uuid4())

    def check_input(self, word):
        word = word.lower()
        result = []
        for i, letter in enumerate(word):
            if letter == self.word[i]:
                result.append('correct')
            elif letter in self.word:
                result.append('present')
            else:
                result.append('absent')
        return result
    
    def play_round(self, word):
        err = None
        try:
            result_states = self.check_input(word)
            self.b_win = self.check_win(result_states)
            results_tuple = [
                (state, letter) 
                for state, letter in zip(result_states, list(word))
            ]
            self.grid_state[self.current_row] = results_tuple
            self.current_row += 1
            grid_str = grid_to_str(self.grid_state, formatted=True)
            grid_html = grid_to_html(self.grid_state)
        except Exception as e:
            err = str(e)
        info = {
            "word": word,
            "current_row": self.current_row - 1,
            "error": True if err else False,
            "error_text": err if err else None,
            "win": self.b_win,
            "results": None if err else result_states,
            "grid": None if err else self.grid_state,
            "grid_formatted": grid_str,
            "grid_html": grid_html,
        }
        return info
        
    @staticmethod
    def check_win(result_states):
        return all([state == 'correct' for state in result_states])

class Guesser:
    def __init__(self) -> None:
        self.words = load_words()

    def guess(
        self,
        common: bool = False,
    ) -> str:
        word_type = 'common' if common else 'valid'
        word = random.choice(self.words[word_type])
        return word

def simulated_game(
) -> list:
    output = []
    game = WordleGame(word="sails")
    guesser = Guesser()
    for _turn in range(6):
        guess_word = guesser.guess(common=True)
        info = game.play_round(guess_word)
        output.append(info)
        if info["win"]:
            break
    return output

def filter_fields(
    data: list,
    fields=[
        "word",
        "current_row",
        "error",
        "error_text",
        "win",
        "results",
        "grid",
        "grid_formatted",
        "grid_html"
    ]
) -> list:
    return [
        {k:v for k,v in e.items() if k in fields} 
        for e in data
    ]

def main():
    output = simulated_game()
    fields=[
        "word",
        "current_row",
        "results",
        "win",
    ]
    output = filter_fields(output, fields=fields)
    print(json.dumps(output, indent=2))

if __name__ == '__main__':
    main()