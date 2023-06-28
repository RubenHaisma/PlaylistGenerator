import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from authenticate import authenticate

def create_user_track_matrix(sp, user_id):
    """
    Creates a user-track matrix based on user listening history.

    This function retrieves the user's listening history from the Spotify API and creates a user-track matrix,
    where each row represents a user and each column represents a track. The matrix is populated with interaction
    values indicating the user's listening activity for each track.

    Parameters:
        - sp (spotipy.Spotify): The authenticated Spotify object.
        - user_id (str): The user ID.

    Returns:
        - user_track_matrix (pd.DataFrame): The user-track matrix.
        - track_indices (dict): A dictionary mapping track IDs to column indices in the matrix.
    """
    # Get user's listening history
    sp = authenticate()
    listening_history = sp.current_user_recently_played(limit=50)

    # Create an empty DataFrame
    df = pd.DataFrame(columns=['user_id', 'track_id', 'interaction'])

    # Iterate over listening history and populate the DataFrame
    for item in listening_history['items']:
        track_id = item['track']['id']
        df = df._append({'user_id': user_id, 'track_id': track_id, 'interaction': 1}, ignore_index=True)

    # Create track indices dictionary
    track_indices = {track_id: i for i, track_id in enumerate(df['track_id'].unique())}

    # Remove duplicate entries
    df = df.drop_duplicates(['user_id', 'track_id'])

    # Convert DataFrame to user-track matrix
    user_track_matrix = df.pivot(index='user_id', columns='track_id', values='interaction').fillna(0)

    return user_track_matrix, track_indices


def collab_based_filtering(sp, user_track_matrix, track_indices, top_n):
    """
    Generates collaborative filtering recommendations based on the user-track matrix.

    Args:
        sp (spotipy.Spotify): Spotify object with the user's access token.
        user_track_matrix (scipy.sparse.csr_matrix): User-track matrix.
        track_indices (dict): Mapping of track indices to track IDs.
        top_n (int): Number of recommendations to generate.

    Returns:
        recommendations (list): List of track URIs for the recommendations.
    """
    # Calculate item-item similarity using cosine similarity
    item_similarity = cosine_similarity(user_track_matrix.T)

    # Get the user's most recent track
    sp = authenticate()
    recent_track = sp.current_user_recently_played(limit=1)['items'][0]['track']
    recent_track_id = recent_track['id']

    # Check if the recent track ID is in the track indices dictionary
    if recent_track_id in track_indices:
        recent_track_index = track_indices[recent_track_id]

        # Get top-N similar tracks
        similarities = item_similarity[recent_track_index]
        top_similar_tracks_indices = similarities.argsort()[-top_n:][::-1]

        # Get track URIs for the recommendations
        recommendations = []
        for index in top_similar_tracks_indices:
            track_id = list(track_indices.keys())[index]
            track_uri = f"spotify:track:{track_id}"
            recommendations.append(track_uri)

        return recommendations

    else:
        raise ValueError("Recent track ID is not in the track indices dictionary.")



# Copyright (c) 2023 Ruben Haisma
# All rights reserved.