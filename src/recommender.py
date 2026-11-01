import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file."""
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        songs = list(csv.DictReader(csv_file))

    for song in songs:
        song["id"] = int(song["id"])
        for field in ("energy", "tempo_bpm", "valence", "danceability", "acousticness"):
            song[field] = float(song[field])

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against a user's preferences."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_score = 1 - abs(song["energy"] - user_prefs["target_energy"])
    score += energy_score
    reasons.append(f"energy closeness (+{energy_score:.2f})")

    tempo_score = 0.5 * max(
        0,
        1 - abs(song["tempo_bpm"] - user_prefs["target_tempo"]) / 94,
    )
    score += tempo_score
    reasons.append(f"tempo closeness (+{tempo_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by how well they match the user's preferences."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, ", ".join(reasons)))

    return sorted(scored_songs, key=lambda result: result[1], reverse=True)[:k]
