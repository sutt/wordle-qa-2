import json
import random
from game import (
    WordleGame,
    Guesser,
    filter_fields,
)

QUESTION_DESCRIPTION = f'''
Task: fill-in the missing data.
    - missing data: results array of present/absent/correct
    - we know the word in the info
simulate a wordle game with outputs in json
always guess the word on the last output


'''

SYSTEM_PROMPT = f'''
Below is data from a Wordle game.

In the data, one portion is marked missing, indicated by the ??? tokens. 

Respond to the multiple choice question by selecting the answer which best completes the missing portion of the data.
'''

def permute_answer(
    answer: list,
    options: list = ['absent', 'present', 'correct'],
    k: float = None,
) -> list:
    k = 1 / len(answer) if k is None else k
    _new = [
        e if random.random() > k else random.choice(options)
        for e in answer
    ]
    if _new == answer:
        return permute_answer(answer)
    return _new

def obfuscate_output(
    output: list,
    obfuscate_token: str = '???',
) -> list:
    obs_index = 2 #random.randint(0,5)
    output = output.copy()
    answer = output[obs_index]['results']
    output[obs_index]['results'] = obfuscate_token
    return answer, output

def answer_template(
    answer: str, 
    num: int = 4,
) -> list:
    letters = 'abcdefghijk'
    options = [e.upper() for e in letters[:num]]
    answers = [permute_answer(answer) for _ in range(num-1)]
    correct_index = random.randint(0,num-1)
    answers.insert(correct_index, answer)
    answer_text = '\n'.join(
        f'''{option}) {answer}'''
        for option, answer in zip(options, answers)
    )
    option_truth = answer_text.split('\n')[correct_index]
    return option_truth, answer_text
    
def simulated_game(
) -> list:
    output = []
    game = WordleGame(word_type='common')
    secret_word = game.word
    guesser = Guesser()
    for _turn in range(3):
        guess_word = guesser.guess(common=True)
        info = game.play_round(guess_word)
        output.append(info)
    return output, secret_word

def make_question(
        
) -> dict:
    q_text = ''
    output, secret_word = simulated_game()
    fields=[
        "word",
        "current_row",
        "results",
        "win",
    ]
    output = filter_fields(output, fields=fields)
    ground_truth, question_obj = obfuscate_output(output)
    question_obj = {'secret_word': secret_word, 'turns': question_obj}
    option_truth, answer_text = answer_template(ground_truth)
    q_text += '\n```json\n'
    q_text += json.dumps(question_obj, indent=2)
    q_text += '\n```\n\n'
    q_text += 'Possible Answers:\n'
    q_text += answer_text
    return {
        'q_text': q_text,
        'a_text': option_truth,
    }

def make_markdown(
    q_text: str,
    a_text: str,
    index: int = 0,
) -> str:
    md = f'''
## Simulated-Missing-{index}
#### meta
#### question
{q_text}
<EVAL-ENDCHAR>
#### answer
{a_text}<EVAL-ENDCHAR>

'''
    return md



if __name__ == '__main__':
    
    # Params
    NUM_QUESTIONS = 15
    SEED = 2897
    if SEED is not None:
        random.seed(SEED)

    # Generate Output, print to stdout, and pipe to file
    md = ''
    for q_index in range(NUM_QUESTIONS):
        d = make_question()
        _md = make_markdown(
            d['q_text'],
            d['a_text'],
            q_index,
        )
        md += _md
        md += '\n\n'
    
    print(md)

    # def test_permute():     
    #     for i in range(10): 
    #         N = 5
    #         options = ['absent', 'present', 'correct']
    #         a = [random.choice(options) for _ in range(N)]
    #         a_2 = permute_answer(a)
    #         print(a)
    #         print(a_2)
    #         print('-----')
