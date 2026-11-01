# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

My recommender is content-based: it compares each song's attributes to a
listener's taste profile instead of learning from other users' behavior.

**Song features used:** genre, mood, energy, and tempo. The data also has
valence, danceability, and acousticness, but this version doesn't score them at all.

**User preferences considered:** a favorite genre, a favorite mood, a target
energy level, and a target tempo.

**How a score is built:** every song starts at zero and earns points.
- 2.0 points if its genre matches the listener's favorite
- 1.0 point if its mood matches
- up to 1.0 point for energy, with more points the closer the song's energy
  is to the target
- up to 0.5 points for tempo, scored the same way

The highest possible score is 4.5. The system scores all 18 songs, sorts them
from highest to lowest, and returns the top five, along with the reasons each
song earned its points.

**Why these weights:** genre counts the most because it is usually the first
filter listeners apply, mood comes next because it captures the vibe, and
tempo counts least because it overlaps with energy.

**Changes from the starter logic:** the starter only had placeholder
functions. I added closeness-based scoring for the numeric features (so a
song nearer the target beats one that is merely higher or lower), a reasons
list for every score, and tempo as a small extra signal.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system lets genre and mood labels outweigh the numbers. A genre match is
worth 2.0 points and a mood match 1.0, while energy and tempo together are
worth at most 1.5. When I tested a listener who wanted classical,
melancholy music with high energy (0.90), the top result was Winter Window,
a nearly silent piano piece with energy 0.02. Its genre and mood matches
added 3.0 points, which outweighed the fact that its energy was nowhere near
what the listener wanted. The catalog makes this worse: 13 of the 15 genres
have only one song, so a single label match tends to win no matter how poor
the song is on everything else. The system also ignores valence,
danceability, and acousticness, so listeners who care about those can't
express it.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

**Profiles tested:** High-Energy Pop (pop, happy, energy 0.90), Chill Lofi
(lofi, chill, energy 0.40), Deep Intense Rock (rock, intense, energy 0.92),
and a deliberately conflicting profile (classical, melancholy, energy 0.90).
I looked at whether each top 5 matched what a real listener with that taste
would expect, and whether the scoring reasons made sense.

**What surprised me:**
- The same songs kept appearing. Gym Hero, Sunrise City, and Storm Runner
  showed up in three of the four lists.
- A nearly silent piano piece (Winter Window) was the top pick for someone
  who wanted high energy.
- Pop and Rock got exactly the same five songs, just in a different order.

**Comparing pairs of profiles:**
- **Pop vs. Lofi:** no songs overlap. Pop pulls bright, high-energy tracks
  (Sunrise City), and Lofi pulls calm, slow ones (Midnight Coding). This
  makes sense because their genre, mood, and energy targets are all completely
  different.
- **Pop vs. Rock:** the same five songs, reordered. Each profile's own genre
  song wins (Sunrise City for Pop, Storm Runner for Rock), then the rest are
  high-energy songs. The catalog has only one rock song, so once it is used
  up, Rock falls back on the same energetic songs Pop uses.
- **Pop vs. Conflicting:** three songs appear in both lists (Gym Hero, Storm
  Runner, Sunrise City), because both profiles want energy 0.90. The
  Conflicting profile then puts Winter Window first because of its genre
  and mood matches.
- **Lofi vs. Rock:** no overlap, and they are opposites: low energy and slow
  versus high energy and fast. That is the result I expected from two
  listeners with opposite tastes.
- **Lofi vs. Conflicting:** no overlap. Lofi stays calm all the way down its
  list. The Conflicting profile is pulled between a calm genre and mood
  (classical, melancholy) and a loud energy target, so its list starts with
  two low-energy songs (Winter Window, Slow Motion Lights) and then switches
  to loud ones.
- **Rock vs. Conflicting:** Gym Hero, Storm Runner, and Sunrise City appear
  in both because both want high energy. The difference is the top spot:
  Rock's winner matches the genre, the mood, and the energy, while the
  Conflicting profile's winner matches only the labels.

**Why Gym Hero keeps showing up for "Happy Pop":** Gym Hero is a pop song,
so it earns the full 2.0 genre points, and its energy (0.93) is almost
exactly what a high-energy listener wants. It is not happy, because its
mood is "intense," so it misses the 1.0 mood points, but that still leaves
it ahead of every song that is happy but not pop. The system rewards "same
genre and same energy" more than "same mood," so a workout song can land in
a happy playlist.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
