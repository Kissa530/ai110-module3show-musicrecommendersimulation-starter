"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "target_tempo": 120,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nRecommendations for:")
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
