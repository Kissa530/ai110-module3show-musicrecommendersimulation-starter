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

---

## Evaluation: Profile Results

I ran the recommender on four profiles: three typical listeners and one
deliberately conflicting edge case (18 songs loaded).

Chill Lofi: the top 4 feel right, because the three lofi songs and then ambient/chill are what I’d expect.
Deep Intense Rock: Storm Runner is right, but Velvet Meter (funk) at #3 doesn’t feel like rock.
High Energy + Melancholy: Winter Window (nearly silent) winning feels wrong for someone who wants high energy.

### High-Energy Pop
```
Genre: pop | Mood: happy | Target energy: 0.90 | Target tempo: 125 BPM

1. Sunrise City - Neon Echo (Score: 4.38)
   - genre match (+2.0)
   - mood match (+1.0)
   - energy closeness (+0.92)
   - tempo closeness (+0.46)

2. Gym Hero - Max Pulse (Score: 3.43)
   - genre match (+2.0)
   - energy closeness (+0.97)
   - tempo closeness (+0.46)

3. Rooftop Lights - Indigo Parade (Score: 2.35)
   - mood match (+1.0)
   - energy closeness (+0.86)
   - tempo closeness (+0.49)

4. Velvet Meter - The Pocket Lines (Score: 1.35)
   - energy closeness (+0.92)
   - tempo closeness (+0.43)

5. Storm Runner - Voltline (Score: 1.35)
   - energy closeness (+0.99)
   - tempo closeness (+0.36)
```

### Chill Lofi
```
Genre: lofi | Mood: chill | Target energy: 0.40 | Target tempo: 78 BPM

1. Midnight Coding - LoRoom (Score: 4.48)
   - genre match (+2.0)
   - mood match (+1.0)
   - energy closeness (+0.98)
   - tempo closeness (+0.50)

2. Library Rain - Paper Lanterns (Score: 4.42)
   - genre match (+2.0)
   - mood match (+1.0)
   - energy closeness (+0.95)
   - tempo closeness (+0.47)

3. Focus Flow - LoRoom (Score: 3.49)
   - genre match (+2.0)
   - energy closeness (+1.00)
   - tempo closeness (+0.49)

4. Spacewalk Thoughts - Orbit Bloom (Score: 2.28)
   - mood match (+1.0)
   - energy closeness (+0.88)
   - tempo closeness (+0.40)

5. Blue Hour Train - Calder Street (Score: 1.41)
   - energy closeness (+0.94)
   - tempo closeness (+0.47)
```

### Deep Intense Rock
```
Genre: rock | Mood: intense | Target energy: 0.92 | Target tempo: 150 BPM

1. Storm Runner - Voltline (Score: 4.48)
   - genre match (+2.0)
   - mood match (+1.0)
   - energy closeness (+0.99)
   - tempo closeness (+0.49)

2. Gym Hero - Max Pulse (Score: 2.39)
   - mood match (+1.0)
   - energy closeness (+0.99)
   - tempo closeness (+0.40)

3. Velvet Meter - The Pocket Lines (Score: 1.24)
   - energy closeness (+0.94)
   - tempo closeness (+0.30)

4. Sunrise City - Neon Echo (Score: 1.23)
   - energy closeness (+0.90)
   - tempo closeness (+0.33)

5. Rooftop Lights - Indigo Parade (Score: 1.20)
   - energy closeness (+0.84)
   - tempo closeness (+0.36)
```

### Conflicting: High Energy + Melancholy
```
Genre: classical | Mood: melancholy | Target energy: 0.90 | Target tempo: 140 BPM

1. Winter Window - Elena Voss (Score: 3.18)
   - genre match (+2.0)
   - mood match (+1.0)
   - energy closeness (+0.12)
   - tempo closeness (+0.06)

2. Slow Motion Lights - Neon Orchard (Score: 1.85)
   - mood match (+1.0)
   - energy closeness (+0.42)
   - tempo closeness (+0.43)

3. Gym Hero - Max Pulse (Score: 1.43)
   - energy closeness (+0.97)
   - tempo closeness (+0.46)

4. Storm Runner - Voltline (Score: 1.43)
   - energy closeness (+0.99)
   - tempo closeness (+0.44)

5. Sunrise City - Neon Echo (Score: 1.30)
   - energy closeness (+0.92)
   - tempo closeness (+0.38)
```

---

---


## Experiments You Tried

### Weight shift: half genre, double energy

I halved the genre bonus (2.0 → 1.0) and doubled the energy score (0–1.0 →
0–2.0). The maximum score stayed at 4.5. I then reran all four profiles.

**What changed:**
- **Chill Lofi** and **Deep Intense Rock** barely moved. The songs that match
  both genre and mood still came first.
- **High-Energy Pop** kept the same top 3, but Rooftop Lights (mood match only)
  moved much closer to Gym Hero (genre match only).
- **Conflicting: High Energy + Melancholy** changed the most (output below).

```
Genre: classical | Mood: melancholy | Target energy: 0.90 | Target tempo: 140 BPM

1. Storm Runner - Voltline (Score: 2.42)
   - energy closeness (+1.98)
   - tempo closeness (+0.44)

2. Gym Hero - Max Pulse (Score: 2.40)
   - energy closeness (+1.94)
   - tempo closeness (+0.46)

3. Winter Window - Elena Voss (Score: 2.30)
   - genre match (+1.0)
   - mood match (+1.0)
   - energy closeness (+0.24)
   - tempo closeness (+0.06)

4. Slow Motion Lights - Neon Orchard (Score: 2.27)
   - mood match (+1.0)
   - energy closeness (+0.84)
   - tempo closeness (+0.43)

5. Sunrise City - Neon Echo (Score: 2.22)
   - energy closeness (+1.84)
   - tempo closeness (+0.38)
```

**More accurate or just different?** Mostly different. Winter Window, a nearly
silent piano piece, fell from #1 to #3, which suits a listener who wants high
energy. But the new #1 and #2 match neither the genre nor the mood, so the
listener's "melancholy" preference is now ignored. The change shifts which
preference wins instead of fixing the problem.

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



