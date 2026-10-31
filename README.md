# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real platforms like Spotify and YouTube combine collaborative filtering
(learning from other users' behavior) with content-based filtering (matching
song attributes). My recommender is content-based only: it compares each
song's attributes to a user's taste profile.



- What features does each `Song` use in your system

`genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`. In this first version, only genre, mood, energy, and tempo
are scored. The other three are loaded but not yet used.

- What information does your `UserProfile` store

`favorite_genre`, `favorite_mood`, `target_energy`, and `target_tempo`.

- How does your `Recommender` compute a score for each song

Genre and mood score 1 for a match and 0 otherwise. Energy and tempo score by
closeness to the user's target (`1 - |song_value - target_value|`, with tempo
scaled by its range), so songs nearer the target score higher. The total is a
weighted sum: `2.0·genre + 1.5·mood + 2.0·energy + 0.5·tempo`. Genre weighs
most because it is the first filter people usually apply.

- How do you choose which songs to recommend

Score every song, sort from highest to lowest, and return the top *k*.


Flow: UserProfile + songs → score each song → sort → top *k*

Limitation: Heavy genre weighting may over-favor a user's usual genre
and create a filter bubble (covered in my Model Card).

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



