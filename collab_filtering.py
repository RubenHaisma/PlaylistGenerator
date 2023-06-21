# Description: This file contains the collaborative filtering algorithm

def collaborative_filtering(sp):
    # Get the user's top artists
    top_artists = sp.current_user_top_artists(limit=5)

    # Print user's favorite artists
    print("Your favorite artists:")
    for i, artist in enumerate(top_artists['items'], 1):
        print(f"{i}. {artist['name']}")

    # Get the top tracks of similar users based on their top artists
    similar_users_tracks = []
    for artist in top_artists['items']:
        tracks = sp.artist_top_tracks(artist['id'], country='US')['tracks']
        similar_users_tracks.extend(tracks)

    # Return the recommended tracks from similar users' top tracks
    return similar_users_tracks

