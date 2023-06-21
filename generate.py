import random

# Import the authenticate, collaborative_filtering, and content_filtering functions from other files
from authenticate import authenticate
from collab_filtering import collaborative_filtering
from content_filtering import content_filtering

def generate_playlist():
    # Step 0: Authenticate the user and create a Spotify object
    sp, USER_ID, PLAYLIST = authenticate()
    # Step 1: Retrieve user preferences for danceability, energy, valence, and novelty
    danceability = float(input("How important is danceability (0.0 - 1.0)? "))
    energy = float(input("How important is energy (0.0 - 1.0)? "))
    valence = float(input("How important is valence(positivity) (0.0 - 1.0)? "))
    novelty_factor = float(input("How important is novelty (0.0 - 1.0)? "))

    # Step 2: Prompt the user to choose the playlist generation method
    method = input("Choose playlist generation method ('genres', 'artists', or 'both'): ")

    # Step 3: Perform collaborative filtering or content filtering based on the chosen method
    recommendations = []
    if method == "genres":
        user_genres = input("Enter your preferred genres (comma-separated): ").split(",")
        recommendations = content_filtering(sp, danceability, energy, valence, user_genres, novelty_factor)
    elif method == "artists":
        recommendations = collaborative_filtering(sp)
    elif method == "both":
        user_genres = input("Enter your preferred genres (comma-separated): ").split(",")
        collaborative_recommendations = collaborative_filtering(sp)
        content_recommendations = content_filtering(sp, danceability, energy, valence, user_genres, novelty_factor)
        recommendations = collaborative_recommendations + content_recommendations
    else:
        print("Invalid method chosen. Exiting...")
        return

    # Step 4: Create a new private playlist and give it a name
    playlist_name = input("Enter a name for the playlist: ")
    playlist = sp.user_playlist_create(USER_ID, playlist_name, public=False,
                                       description='Playlist generated by Playlist Generator')

    # Step 5: Add the recommended tracks to the playlist in a shuffled order
    random.shuffle(recommendations)
    track_ids = [track['id'] for track in recommendations]
    sp.playlist_add_items(playlist['id'], track_ids)

    # Step 6: Show a link to the newly created playlist
    playlist_url = playlist['external_urls']['spotify']

    print("Playlist is generated and tracks are added. You can access it at:\n" + playlist_url)


# Call the generate_playlist function to generate a playlist
generate_playlist()