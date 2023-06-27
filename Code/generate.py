# Copyright (c) 2023 Ruben Haisma
# All rights reserved.

import spotipy as sp

# Import the authenticate and content_filtering functions from other files
from authenticate import authenticate
from content_filtering import content_based_filtering

def generate_playlist():
    # Authenticate user and obtain Spotify object
    sp = authenticate()

    # User input for playlist generation
    top_n = int(input("How many songs do you want in the playlist? "))

    # Generate playlist using content-based filtering
    recommendations = content_based_filtering(sp, top_n)

    # Create a new playlist
    playlist_name = input("What is the name of the new playlist? ")
    playlist_description = "Playlist generated using content-based filtering"
    playlist = sp.user_playlist_create(user=sp.me()['id'], name=playlist_name, public=True, description=playlist_description)

    # Add recommended tracks to the playlist
    sp.playlist_add_items(playlist_id=playlist['id'], items=recommendations)
    print("Playlist generated successfully!")

    # Provide a link to the playlist
    print("Playlist link: " + playlist['external_urls']['spotify'])

if __name__ == '__main__':
    generate_playlist()
