# JSON-state-reasoning-1
#### info
Written 11.26.23
Revised 12.17.23

Goal: Use programming style representations of the game state to answer questions about the game.

#### meta
- answer_type: mutliple-choice
- answer suggested length: 10

#### question
Below is the state of a wordle game. Use the output of state information to answer the question.

A B O U T
S A L E S
F L A M E
□ □ □ □ □
□ □ □ □ □
□ □ □ □ □

```json
[
    [['absent', 'a'], ['present', 'b'], ['correct', 'o'], ['absent', 'u'], ['absent', 't']], 
    [['present', 's'], ['absent', 'a'], ['absent', 'l'], ['absent', 'e'], ['correct', 's']], 
    [['absent', 'f'], ['absent', 'l'], ['absent', 'a'], ['absent', 'm'], ['absent', 'e']], 
    [['empty', ''], ['empty', ''], ['empty', ''], ['empty', ''], ['empty', '']], 
    [['empty', ''], ['empty', ''], ['empty', ''], ['empty', ''], ['empty', '']], 
    [['empty', ''], ['empty', ''], ['empty', ''], ['empty', ''], ['empty', '']]
]
```
<EVAL-ENDCHAR>

## Reason-Win
#### meta
#### answer
B) No<EVAL-ENDCHAR>
#### question
Based on the output, has the player won yet?
A) Yes
B) No
<EVAL-ENDCHAR>

## Reason-Win-2
#### meta
#### answer
B) No<EVAL-ENDCHAR>
#### question
Based on the output, do we know the secret word?
A) Yes
B) No
<EVAL-ENDCHAR>

## Reason-Win-3
#### meta
#### answer
B) No<EVAL-ENDCHAR>
#### question
Based on the output, has the player lost yet?
A) Yes
B) No

## Reason-Win-3
#### meta
#### answer
C) No - the player has not guessed all five letters in the correct order<EVAL-ENDCHAR>
#### question
Based on the output, has the player lost yet?
A) Yes - the player has found the secret word
B) Yes - the player has guessed five total letters correctly
C) No - the player has not guessed all five letters in the correct order
D) No - the order of the letters needs to be reversed
E) We don't know - there are still letters that can be guessed
<EVAL-ENDCHAR>

## Reason-Current-Turn-Num
#### meta
#### answer
B) No<EVAL-ENDCHAR>
#### question
What is the current turn number? 
A) 1
B) 2
C) 3
D) 4
E) None of the above
<EVAL-ENDCHAR>

## Reason-Words-Guessed
#### meta
#### answer
A) ABOUT, SALES, FLAME<EVAL-ENDCHAR>
#### question
What words have been tried?
A) ABOUT, SALES, FLAME
B) ABOUT, SALES
C) ABOUT
D) None of the above
<EVAL-ENDCHAR>

## Reason-Words-Guessed-2
#### meta
#### answer
B) ABOUT, SALES<EVAL-ENDCHAR>
#### question
What choice contains only valid words that have been tried?
A) STATE, FLAME
B) ABOUT, SALES
C) ABSENT, PRESENT, CORRECT
D) None of the above
<EVAL-ENDCHAR>

## Reason-Letters-Guessed
#### meta
#### answer
A) ABOUT, SALES, FLAME<EVAL-ENDCHAR>
#### question
What letters have been tried?
A) ABOUT, SALES, FLAME
B) ABOUT, SALES
C) ABOUT
D) None of the above
<EVAL-ENDCHAR>

## Reason-Letters-Guessed
#### meta
#### answer
D) None of the above<EVAL-ENDCHAR>
#### question
What letters do we know are in the secret word?
A) B, O, U
B) T, R, S
C) A, U, L
D) None of the above
<EVAL-ENDCHAR>

## Reason-Letters-Guessed-2
#### meta
#### answer
A) B, O, S<EVAL-ENDCHAR>
#### question
What letters do we know are in the secret word?
A) B, O, S
B) T, R, S
C) A, U, L
D) None of the above
<EVAL-ENDCHAR>
