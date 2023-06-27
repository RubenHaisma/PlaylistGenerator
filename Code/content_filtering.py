from sklearn.metrics.pairwise import cosine_similarity
from authenticate import authenticate

from sklearn.metrics.pairwise import cosine_similarity

def content_based_filtering(sp, top_n):
    # Step 1: Collect User Data
    sp = authenticate()
    user_tracks = sp.current_user_top_tracks(limit=50, time_range='medium_term')['items']
    user_track_ids = [track['id'] for track in user_tracks]

    # Step 2: Extract Track Features
    user_track_features = get_track_features(sp, user_track_ids)

    # Step 3: Build User Profile
    user_profile = build_user_profile(user_track_features)

    # Step 4: Find Similar Tracks
    all_tracks = get_all_tracks(sp)
    similarities = calculate_track_similarities(user_profile, all_tracks)

    # Step 5: Generate Recommendations
    recommendations = get_top_n_recommendations(similarities, top_n)

    return recommendations


def get_track_features(sp, track_ids):
    track_features = []
    for track_id in track_ids:
        audio_features = sp.audio_features(track_id)[0]
        track_features.append({
            'id': track_id,
            'danceability': audio_features['danceability'],
            'energy': audio_features['energy'],
            'valence': audio_features['valence']
        })

    return track_features


def build_user_profile(track_features):
    user_profile = {
        'danceability': sum(track['danceability'] for track in track_features) / len(track_features),
        'energy': sum(track['energy'] for track in track_features) / len(track_features),
        'valence': sum(track['valence'] for track in track_features) / len(track_features)
    }

    return user_profile


def get_all_tracks(sp):
    tracks = sp.search(q='year:2022', type='track', limit=50)['tracks']['items']
    track_ids = [track['id'] for track in tracks]

    audio_features = sp.audio_features(track_ids)
    all_tracks = []
    for i, track in enumerate(tracks):
        audio_feature = audio_features[i]
        all_tracks.append({
            'id': track['id'],
            'danceability': audio_feature['danceability'],
            'energy': audio_feature['energy'],
            'valence': audio_feature['valence']
        })

    print("All tracks: ", all_tracks)  # Debugging print statement

    return all_tracks


def calculate_track_similarities(user_profile, tracks):
    user_matrix = [[user_profile['danceability'], user_profile['energy'], user_profile['valence']]]
    track_matrix = [[track['danceability'], track['energy'], track['valence']] for track in tracks]

    similarities = cosine_similarity(user_matrix, track_matrix)

    return similarities[0]

def get_top_n_recommendations(similarities, top_n):
    sp = authenticate()
    all_tracks = get_all_tracks(sp)
    recommendations = []
    for i in range(len(similarities)):
        recommendations.append((i, similarities[i]))  # Store track index and similarity

    recommendations.sort(key=lambda x: x[1], reverse=True)  # Sort by similarity in descending order
    recommendations = recommendations[:top_n]  # Get top-N recommendations

    track_uris = []
    for recommendation in recommendations:
        track_index = recommendation[0]
        track_id = all_tracks[track_index]['id']
        if track_id:
            track_uri = f"spotify:track:{track_id}"
            track_uris.append(track_uri)

    print("Track URIs: ", track_uris)  # Debugging print statement

    return track_uris




