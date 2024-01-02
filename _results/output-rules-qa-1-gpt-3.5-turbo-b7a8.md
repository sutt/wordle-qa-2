# Rule-QA-1
**Run ID:** b7a8
**Model name:** gpt-3.5-turbo
**System Prompt:**
Below is a question about the game Wordle. Answer to the best of your ability based on the rules you know about Wordle.
<EVAL-ENDCHAR>


**Meta Data:**
- answer_type: mutliple-choice
- answer_suggested_length: 10

### Num-Guesses-1

<details>
<summary>meta_data:</summary>

- answer_type: mutliple-choice
- answer_suggested_length: 10

</details>


**Question:**
Below is a question about the game Wordle. Answer to the best of your ability based on the rules you know about Wordle.
Q: What is the maximum number of guesses you can make in a game of Wordle?
A) 5
B) 6
C) 7
D) No limit
<EVAL-ENDCHAR1>



**Completion:**
A) 5

**Ground Truth:**
B) 6

**Grade:**
False

### Num-Letter-1

<details>
<summary>meta_data:</summary>

- answer_type: mutliple-choice
- answer_suggested_length: 10

</details>


**Question:**
Below is a question about the game Wordle. Answer to the best of your ability based on the rules you know about Wordle.
Q: How many letter are in the word you are trying to guess?
A) 4
B) 5
C) 6
D) Any amount


**Completion:**
A) 4

**Ground Truth:**
B) 5

**Grade:**
False

### Terminology-Present-1

<details>
<summary>meta_data:</summary>

- answer_type: mutliple-choice
- answer_suggested_length: 10

</details>


**Question:**
Below is a question about the game Wordle. Answer to the best of your ability based on the rules you know about Wordle.
Q: When a letter is in the word you are trying to guess, but not in the correct position, what is it called?
A) Present
B) Absent
C) Correct
D) None of the above



**Completion:**
B) Absent

**Ground Truth:**
A) Present

**Grade:**
False

### Terminology-Absent-1

<details>
<summary>meta_data:</summary>

- answer_type: mutliple-choice
- answer_suggested_length: 10

</details>


**Question:**
Below is a question about the game Wordle. Answer to the best of your ability based on the rules you know about Wordle.
Q: When a letter is not in the word you are trying to guess, what is it called?
A) Present
B) Absent
C) Correct
D) None of the above



**Completion:**
D) None of the above.

**Ground Truth:**
B) Absent

**Grade:**
False

### Mechanics-Multiletter-1

<details>
<summary>meta_data:</summary>

- answer_type: mutliple-choice
- answer_suggested_length: 10

</details>


**Question:**
Below is a question about the game Wordle. Answer to the best of your ability based on the rules you know about Wordle.
Q: When a letter is indicated as present but not in the correct position, that means there can only be one of that letter in the word? 
A) True
B) False


**Completion:**
B) False

**Ground Truth:**
B) False

**Grade:**
True

### Mechanics-Basic-Reasoning-1

<details>
<summary>meta_data:</summary>

- answer_type: mutliple-choice
- answer_suggested_length: 10

</details>


**Question:**
Below is a question about the game Wordle. Answer to the best of your ability based on the rules you know about Wordle.
Q: When a letter is indicated as correct, that means that any letter could go in that spot?
A) True
B) False


**Completion:**
B) False

**Ground Truth:**
B) False

**Grade:**
True

### Mechanics-Basic-Reasoning-2

<details>
<summary>meta_data:</summary>

- answer_type: mutliple-choice
- answer_suggested_length: 10

</details>


**Question:**
Below is a question about the game Wordle. Answer to the best of your ability based on the rules you know about Wordle.
Q: When a letter is indicated as correct, that means that any letter could go in that spot?
A) True
B) False


**Completion:**
B) False

**Ground Truth:**
B) False

**Grade:**
True

### Mechanics-Guess-Valid-Word

<details>
<summary>meta_data:</summary>

- answer_type: mutliple-choice
- answer_suggested_length: 10

</details>


**Question:**
Below is a question about the game Wordle. Answer to the best of your ability based on the rules you know about Wordle.
Can you guess any combination of letters as your guess?
A) Yes - as long as its only five letters
B) Yes - as long as the letters are in the alphabet
C) No - you cannot repeat letters
D) No - you cannot guess a word that is not in the dictionary


**Completion:**
B) Yes - as long as the letters are in the alphabet

**Ground Truth:**
D) No - you cannot guess a word that is not in the dictionary

**Grade:**
False

