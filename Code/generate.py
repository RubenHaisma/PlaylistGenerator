import spotipy as sp

# Import the authenticate and content_filtering functions from other files
from authenticate import authenticate
from content import content_based_filtering
from collab import create_user_track_matrix, collab_based_filtering
from hybrid import hybrid_filtering

def generate_playlist():
    """
    Generates a playlist using a hybrid of content-based filtering and collaborative filtering.

    This function prompts the user for input, generates recommendations using a combination of content-based filtering
    and collaborative filtering, creates a new playlist on Spotify, adds the recommended tracks to the playlist, and
    provides a link to the generated playlist.

    """
    # Authenticate user and obtain Spotify object
    sp = authenticate()

    # User input for playlist generation
    top_n = int(input("How many songs do you want in the playlist? "))
    user_id = sp.me()['id']

    # Create user-track matrix
    user_track_matrix, track_indices = create_user_track_matrix(sp, user_id)

    # Generate playlist using a combination of content-based filtering and collaborative filtering
    option = input("Do you want to use content-based filtering (1), collaborative filtering (2), or hybrid (3)? ")
    if option == "1":
        recommendations = content_based_filtering(sp, top_n)
    elif option == "2":
        recommendations = collab_based_filtering(sp, user_track_matrix, track_indices, top_n)
    elif option == "3":
        recommendations = hybrid_filtering(sp, user_id, top_n)

    # Create a new playlist
    playlist_name = input("What is the name of the new playlist? ")
    playlist_description = "Playlist generated using a hybrid of content-based filtering and collaborative filtering"
    playlist = sp.user_playlist_create(user=sp.me()['id'], name=playlist_name, public=True, description=playlist_description)

    # Add recommended tracks to the playlist
    sp.playlist_add_items(playlist_id=playlist['id'], items=recommendations)
    print("Playlist generated successfully!")

    # Provide a link to the playlist
    print("Playlist link: " + playlist['external_urls']['spotify'])

# Run the function
generate_playlist()




# Copyright (c) 2023 Ruben Haisma
# All rights reserved.