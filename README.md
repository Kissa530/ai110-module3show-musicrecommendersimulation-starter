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


```python
user_profile = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.40,
    "target_tempo": 80,
}
```

- How does your `Recommender` compute a score for each song

Each song gets points from these rules (maximum 4.5):

- +2.0 for a genre match
- +1.0 for a mood match
- up to +1.0 for energy closeness: `1 - |song_energy - target_energy|`
- up to +0.5 for tempo closeness: `max(0, 1 - |song_bpm - target_bpm| / 94)`
  (94 is the tempo range in the catalog; the `max(0, ...)` keeps the score
  from going negative)

Genre is weighted most because it is usually the first filter people apply.
Mood is next because it captures the vibe, and tempo is lowest because it
overlaps with energy.


- How do you choose which songs to recommend?

Score every song, sort from highest to lowest, and return the top *k*.


Flow/Algorithm Recipe: 
```
INPUT
  user_profile = {genre, mood, target_energy, target_tempo}
        |
        v
PROCESS (loop over every row in songs.csv)
  for each song:
      score = 0
      if song.genre == profile.genre:  score += 2.0
      if song.mood  == profile.mood:   score += 1.0
      score += 1 - |song.energy - target_energy|
      score += 0.5 * max(0, 1 - |song.tempo - target_tempo| / 94)
      save (song, score)
        |
        v
OUTPUT
  sort all (song, score) pairs, highest first
  return the top K (e.g., 5)
```
Worked example (Library Rain, lofi/chill profile): genre match +2.00,
mood match +1.00, energy closeness +0.95, tempo closeness +0.46, for a total
of 4.41.


**Expected Biases**

- Genre carries the most weight, so the system may over-prioritize genre and
  miss great songs that match the user's mood and energy but not the genre.
- Moods and genres are exact-match labels, so "chill" and "relaxed" count as
  a total miss even though they are close.
- The catalog is small and most genres have only one song, so results can
  drop off sharply after the first match.
- The profile stores one genre and one mood, so users with mixed tastes are
  poorly represented.

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
Loaded songs: 18

Recommendations for:
  Genre: pop
  Mood: happy
  Target energy: 0.80
  Target tempo: 120 BPM

Top recommendations:

1. Sunrise City - Neon Echo (Score: 4.47)
   - genre match (+2.0)
   - mood match (+1.0)
   - energy closeness (+0.98)
   - tempo closeness (+0.49)

2. Gym Hero - Max Pulse (Score: 3.31)
   - genre match (+2.0)
   - energy closeness (+0.87)
   - tempo closeness (+0.44)

3. Rooftop Lights - Indigo Parade (Score: 2.44)
   - mood match (+1.0)
   - energy closeness (+0.96)
   - tempo closeness (+0.48)

4. Night Drive Loop - Neon Echo (Score: 1.40)
   - energy closeness (+0.95)
   - tempo closeness (+0.45)

5. Paper Kites - Willow Ferry (Score: 1.35)
   - energy closeness (+0.99)
   - tempo closeness (+0.36)
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



