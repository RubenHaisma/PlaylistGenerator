from collab import create_user_track_matrix, collab_based_filtering
from content import content_based_filtering

def hybrid_filtering(sp, user_id, top_n):
    """
    Generates hybrid filtering recommendations based on a combination of content-based and collaborative filtering.

    Args:
        sp (spotipy.Spotify): Spotify object with user authentication.
        user_id (str): The user ID.
        top_n (int): Number of recommendations to generate.

    Returns:
        recommendations (list): List of recommended track URIs.
    """
    # Step 1: Content-Based Filtering
    content_recommendations = content_based_filtering(sp, top_n // 2)

    # Step 2: Collaborative Filtering
    user_track_matrix, track_indices = create_user_track_matrix(sp, user_id)
    collab_recommendations = collab_based_filtering(sp, user_track_matrix, track_indices, top_n // 2)

    # Step 3: Combine Recommendations
    recommendations = content_recommendations + collab_recommendations

    return recommendations





# Copyright (c) 2023 Ruben Haisma
# All rights reserved.