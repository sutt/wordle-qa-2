### Leaderboard: `{input_sheet, model}` on `pct_correct`

| input_name             | model_name     |   num_questions |   pct_correct |
|:-----------------------|:---------------|----------------:|--------------:|
| What Shows Up          | gpt-4          |               1 |          1    |
| What Shows Up          | gpt-3.5-turbo  |               1 |          0    |
| Rule-QA-1              | gpt-4          |               8 |          1    |
| Rule-QA-1              | gpt-3.5-turbo  |               8 |          0.38 |
| Rule-QA-1              | llama_13b_chat |               8 |          0.38 |
| JSON-state-reasoning-1 | gpt-4          |              10 |          0.7  |
| JSON-state-reasoning-1 | gpt-3.5-turbo  |              10 |          0.5  |
| JSON-state-reasoning-1 | llama_13b_chat |               9 |          0.11 |

### Runs: `{input_sheet, model}` on number of `run_id`'s

| input_name             | model_name     |   run_id |
|:-----------------------|:---------------|---------:|
| JSON-state-reasoning-1 | gpt-3.5-turbo  |        1 |
| JSON-state-reasoning-1 | gpt-4          |        1 |
| JSON-state-reasoning-1 | llama_13b_chat |        1 |
| Rule-QA-1              | gpt-3.5-turbo  |        1 |
| Rule-QA-1              | gpt-4          |        1 |
| Rule-QA-1              | llama_13b_chat |        1 |
| What Shows Up          | gpt-3.5-turbo  |        1 |
| What Shows Up          | gpt-4          |        1 |

### All Questions: list of all question names by sheet

| input_name             | name                        |
|:-----------------------|:----------------------------|
| JSON-state-reasoning-1 | Reason-Current-Turn-Num     |
| JSON-state-reasoning-1 | Reason-Letters-Guessed      |
| JSON-state-reasoning-1 | Reason-Letters-Guessed-2    |
| JSON-state-reasoning-1 | Reason-Win                  |
| JSON-state-reasoning-1 | Reason-Win-2                |
| JSON-state-reasoning-1 | Reason-Win-3                |
| JSON-state-reasoning-1 | Reason-Words-Guessed        |
| JSON-state-reasoning-1 | Reason-Words-Guessed-2      |
| Rule-QA-1              | Mechanics-Basic-Reasoning-1 |
| Rule-QA-1              | Mechanics-Guess-Valid-Word  |
| Rule-QA-1              | Mechanics-Multiletter-1     |
| Rule-QA-1              | Num-Guesses-1               |
| Rule-QA-1              | Num-Letter-1                |
| Rule-QA-1              | Terminology-Absent-1        |
| Rule-QA-1              | Terminology-Present-1       |
| What Shows Up          | Q-1                         |
