"""
Command line runner for the Music Recommender Simulation.

Runs the recommender for several user profiles, including edge cases,
and prints the top 5 results with reasons for each.
"""

from src.recommender import load_songs, recommend_songs

PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop", "favorite_mood": "happy",
        "target_energy": 0.90, "target_tempo": 125,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi", "favorite_mood": "chill",
        "target_energy": 0.40, "target_tempo": 78,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock", "favorite_mood": "intense",
        "target_energy": 0.92, "target_tempo": 150,
    },
    "Conflicting: High Energy + Melancholy": {
        "favorite_genre": "classical", "favorite_mood": "melancholy",
        "target_energy": 0.90, "target_tempo": 140,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for name, user_prefs in PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n=== {name} ===")
        print(f"  Genre: {user_prefs['favorite_genre']}")
        print(f"  Mood: {user_prefs['favorite_mood']}")
        print(f"  Target energy: {user_prefs['target_energy']:.2f}")
        print(f"  Target tempo: {user_prefs['target_tempo']} BPM")
        print("\nTop recommendations:")

        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"\n{rank}. {song['title']} - {song['artist']} (Score: {score:.2f})")
            for reason in explanation.split(", "):
                print(f"   - {reason}")


if __name__ == "__main__":
    main()