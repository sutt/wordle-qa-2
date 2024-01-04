## Test on diff system prompt

**System prompt diff: (```bash
git diff miss-prompt-1a-bad  miss-prompt-1b-good```)**

```diff
Below is data from a Wordle game.

In the data, one portion is marked missing, indicated by the ??? tokens. 

Respond to the multiple choice question by selecting the answer which best completes the missing portion of the data.

+ Respond only with the letter and the text in the brackets, e.g. `A) ['absent', 'absent', 'absent', 'absent', 'absent']`. Do not include any other text in your response.

```
**Impact:**
 - 1a-Bad usually has a pre-amble in the answer due to a weak system prompt.
1b-Good corrects for this with an additional sentence in the system prompt and results in no preambles.

**Results:**
 
However there is no major diff in performance, bad is actually slightly more accurate. And note, the question are the exact same between questions