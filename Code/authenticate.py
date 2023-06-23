# Description: This file contains the authenticate function, which prompts the user to enter their Spotify API credentials and returns a Spotify object with the user's access token.
import spotipy

def authenticate():
    # Change the credentials to your own Spotify API credentials if you want to use this code
    CLIENT_ID = "23f6f3d5a7f34c7c821587f67733c833"
    CLIENT_SECRET = "813cafcd03394d808e8214e5c566975c"
    REDIRECT_URI = "http://localhost:3000/"
    USER_ID = "117189269"
    SCOPE = 'playlist-modify-private playlist-read-private user-top-read user-read-recently-played'

    # Create an instance of the SpotifyOAuth class
    sp_oauth = spotipy.oauth2.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPE)

    # Get the cached token
    token_info = sp_oauth.get_cached_token()

    # If the cached token does not exist, ask the user to grant access via the generated URL
    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        print("Visit this URL and grant access:")
        print(auth_url)
        response = input("Enter the full URL you received after authorization: ")

        # Exchange the authorization code for an access token
        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)

    # Get the access token from the token information
    access_token = token_info['access_token']

    # Create a Spotify object with the access token
    sp = spotipy.Spotify(auth=access_token)

    return sp, USER_ID



# Copyright (c) 2023 Ruben Haisma
# All rights reserved.