# What Shows Up

First attempt at the What Shows Up style questions

Written 12.15.2023

Use wordle-api utility to help assist

**Random Thoughts:**
 - Cool very hard problem: keep trying the letter of 'present' in each wrong position until by process of elimination it must be in the final untried spot / or the only non-correct spot left.
 - This assignment get's a little tricky because if a letter is correct, there could still be another use of that letter in other positions of the word e.g. secret word=IMAMS, 1st guess: OMEGA -  M in position #2 is correct. 2nd guess: STEMS M in position #2 is correct therefore M guessed in position #3 (e.g. AMMOS) that M in second position would be marked present. But does the game only do this when a second M is present in the word?
 - condition (4) "we don't know if it's absent/correct" is rare; can only occur when one letter is still missing (?)
 - condition (6) "we do know it's present" is rare; guessing a second instance of a letter which is has already been correct
 secret:    slots
 one:       slate
 two:       slope
 three:     sloot   (O is position #4 we know it's present: it can't be absent because O exists in the word, but it can't be correct because that position must be T)
 - Would love to have unicode characters in the questions or emojis
 - could add in (E) none of the above as a choice
 - Could ask the knowledge-state for only one letter, therefore ask the number which creates more possibilities (7 instead of 4)
 

**Extra prompt stuff...**

 - Don't use your knowledge of valid words to answer the question. Only use your knowledge of the rules, considering any permutation of letters of the appropriate length as a possible word.
 - You don't know the secret word in these questions, therefore you only have partial knowledge of meaning you can eliminate possibilities that certain letters in certain positions will have certain game-states.



**Errata**
 - bueller? bueller? bueller?

#### question
The following question is about the game of Wordle. Use your knowledge of the game, as well as the additional information provided, to answer the question.

Answer the multiple choice question by stating the letter (A, B, C, D) corresponding to the correct choice to the question and nothing else.

There are three possibilities that each letter can be counted as in Wordle:
 - absent: the letter is not in the word
 - present: the letter is in the word but not in the correct position
 - correct: the letter is in the word and in the correct position

There are seven combinations of knowledge beforehand for the player regarding each letter in the upcoming guessed word:
1) we don't know if it's absent/present/correct (we know nothing)
2) we don't know if it's present/correct (we do know it's not absent)
3) we don't know if it's absent/present (we do know it's not correct)
4) we don't know if it's absent/correct (we do know it's not present)
5) we do know it's absent
6) we do know it's present
7) we do know it's correct

Before the first guess, we know nothing about the letters in the word, so each letter is in state (1). Thus we would write the knowledge state of this guess as:
A: 1 P: 1 P: 1 L: 1 E: 1

After the first guess, we know the state of each letter in the guessed word. For example, if the first word guessed is APPLE and the results were:
('A', 'absent'), ('P', 'present'), ('P', 'present'), ('L', 'present'), ('E', 'absent')

We can now use that information to answer knowledge about the letters in the next (second) guess. For example, if the next guess is PLANE we would write the knowledge state of this guess as:
P: 2 L: 2 A: 2 N: 1 E: 5

Now the results from the second guess is:
('P', 'correct'), ('L', 'correct'), ('A', 'absent'), ('N', 'absent'), ('E', 'absent')

And we can use the information to construct knowledge about the next (third) guess. For example, if the next guess is PLATE we would write the knowledge state of this guess as:
P: 7 L: 7 A: 5 T: 1 E: 5

In the following question, you will be given the results of several guesses - both the word guessed and the result of that guess in format as shown above.  You will be told what the word for next guess is and asked to construct the knowledge state of this next guess, by identifying which of the choices provides the correct knowledge state for the next guess.

Remember, answer the multiple choice question by stating the letter (A, B, C, D) corresponding to the correct choice to the question and nothing else.

#### meta
 - answer_suggested_length: 100
 - answer_type: multiple-choice

## Q-1
#### meta
 - hidden word: MARRY
#### question
You played the following two words in order: IMAMS, MAPLE 

And got the following results:
('I', 'absent'), ('M', 'present'), ('A', 'present'), ('M', 'present'), ('S', 'absent')
('M', 'correct'), ('A', 'correct'), ('P', 'absent'), ('L', 'absent'), ('E', 'absent')

Now you play the word: RUGBY. Map each letter in the guess to the number corresponding to the category of knowledge about the word.

Choices:
A) R: 3 U: 3 G: 1 B: 1 Y: 1
B) R: 3 U: 3 G: 1 B: 1 Y: 2
C) R: 1 U: 1 G: 1 B: 2 Y: 2
D) R: 3 U: 3 G: 1 B: 3 Y: 5
<EVAL-ENDCHAR>

#### answer
A<EVAL-ENDCHAR>

## Q-2
