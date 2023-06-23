# Copyright (c) [2023] [Ruben Haisma]
# All rights reserved.

# Description: This file contains the content filtering algorithm used to generate recommendations

def content_filtering(sp, danceability, energy, valence, user_genres, novelty_factor):
    # Generate recommendations based on target attributes, user preferences, and personalized genres
    recommendations = sp.recommendations(seed_genres=user_genres, limit=10,
                                         target_danceability=danceability,
                                         target_energy=energy,
                                         target_valence=valence)
    
    # Introduce novelty by selecting additional tracks from lesser-explored genres or artists
    novelty_tracks = []
    if novelty_factor > 0.0:
        for genre in user_genres:
            tracks = sp.recommendations(seed_genres=[genre], limit=int(novelty_factor * 10))['tracks']
            novelty_tracks.extend(tracks)

    return recommendations['tracks'] + novelty_tracks