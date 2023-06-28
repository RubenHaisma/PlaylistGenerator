import tkinter as tk
from tkinter import messagebox
from content import content_based_filtering
from collab import create_user_track_matrix, collab_based_filtering
from hybrid import hybrid_filtering
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def authenticate():
    """
    Authenticates the user and returns a Spotify object with the user's access token.

    Returns:
        sp (spotipy.Spotify): Spotify object with the user's access token.
    """

    # Get user input for authentication values
    CLIENT_ID = client_id_entry.get()
    CLIENT_SECRET = client_secret_entry.get()
    REDIRECT_URI = redirect_uri_entry.get()
    USER_ID = user_id_entry.get()
    SCOPE = 'playlist-modify-private playlist-read-private user-top-read user-read-recently-played user-library-read playlist-modify-public'

    # Create an instance of the SpotifyOAuth class with user input values
    sp_oauth = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPE)

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

    return sp

def generate_playlist():
    """
    Generates a playlist using content-based filtering or a hybrid of content-based filtering and collaborative filtering.

    This function is triggered when the "Generate Playlist" button is clicked in the GUI.
    It retrieves the playlist name and length from the user inputs, generates recommendations using
    content-based filtering or the hybrid approach, creates a new playlist on Spotify, adds the recommended tracks to the playlist,
    and displays a success message box with the URL of the generated playlist.

    """
    try:
        sp = authenticate()
        top_n = int(playlist_length_entry.get())
        playlist_name = playlist_name_entry.get()

        # User-track matrix and track indices for collaborative filtering
        user_id = sp.me()['id']
        user_track_matrix, track_indices = create_user_track_matrix(sp, user_id)

        # Generate playlist using content-based filtering or the hybrid approach
        option = playlist_option.get()
        if option == 1:
            recommendations = content_based_filtering(sp, top_n)
        elif option == 2:
            recommendations = collab_based_filtering(sp, user_track_matrix, track_indices, top_n)
        elif option == 3:
            recommendations = hybrid_filtering(sp, user_id, top_n)

        # Create a new playlist
        playlist_description = "Playlist generated using content-based filtering" if option == 1 else "Playlist generated using a hybrid of content-based filtering and collaborative filtering"
        playlist = sp.user_playlist_create(user=sp.me()['id'], name=playlist_name, public=True, description=playlist_description)

        # Add recommended tracks to the playlist
        sp.playlist_add_items(playlist_id=playlist['id'], items=recommendations)

        # Get the URL of the playlist
        playlist_url = playlist['external_urls']['spotify']

        messagebox.showinfo("Success", f"Playlist is generated and tracks are added.\nYou can access it at:\n{playlist_url}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Spotify Green Color
SPOTIFY_GREEN = "#1DB954"

# Create the window
window = tk.Tk()
window.title("Playlist Generator")
window.geometry("376x580")
window.configure(bg=SPOTIFY_GREEN)

# Create the widgets
authentication_label = tk.Label(window, text="Authentication:", bg=SPOTIFY_GREEN, fg="white")
authentication_label.pack()

client_id_label = tk.Label(window, text="Client ID:", bg=SPOTIFY_GREEN, fg="white")
client_id_label.pack()
client_id_entry = tk.Entry(window)
client_id_entry.pack()

client_secret_label = tk.Label(window, text="Client Secret:", bg=SPOTIFY_GREEN, fg="white")
client_secret_label.pack()
client_secret_entry = tk.Entry(window)
client_secret_entry.pack()

redirect_uri_label = tk.Label(window, text="Redirect URI:", bg=SPOTIFY_GREEN, fg="white")
redirect_uri_label.pack()
redirect_uri_entry = tk.Entry(window)
redirect_uri_entry.pack()

user_id_label = tk.Label(window, text="User ID:", bg=SPOTIFY_GREEN, fg="white")
user_id_label.pack()
user_id_entry = tk.Entry(window)
user_id_entry.pack()

# Create a space between the authentication and playlist options
tk.Label(window, text="", bg=SPOTIFY_GREEN).pack()

playlist_name_label = tk.Label(window, text="Name your new playlist:", bg=SPOTIFY_GREEN, fg="white")
playlist_name_label.pack()
playlist_name_entry = tk.Entry(window)
playlist_name_entry.pack()

playlist_length_label = tk.Label(window, text="Playlist Length:", bg=SPOTIFY_GREEN, fg="white")
playlist_length_label.pack()
playlist_length_entry = tk.Entry(window, width=3)
playlist_length_entry.pack()

# Playlist Option
playlist_option = tk.IntVar(value=1)

option_frame = tk.Frame(window, bg=SPOTIFY_GREEN)
option_frame.pack()

playlist_option_label = tk.Label(option_frame, text="Choose an option for playlist generation:", bg=SPOTIFY_GREEN, fg="white")
playlist_option_label.pack()

content_option = tk.Radiobutton(option_frame, text="Content-Based Filtering", variable=playlist_option, value=1, bg=SPOTIFY_GREEN, fg="white")
content_option.pack(anchor="w")

collab_option = tk.Radiobutton(option_frame, text="Collaborative Filtering", variable=playlist_option, value=2, bg=SPOTIFY_GREEN, fg="white")
collab_option.pack(anchor="w")

hybrid_option = tk.Radiobutton(option_frame, text="Hybrid (Content + Collaborative)", variable=playlist_option, value=3, bg=SPOTIFY_GREEN, fg="white")
hybrid_option.pack(anchor="w")

# Create a space between the entry and the button
tk.Label(window, text="", bg=SPOTIFY_GREEN).pack()

# Generate...
generate_button = tk.Button(window, text="Generate Playlist", command=generate_playlist, bg='white', fg=SPOTIFY_GREEN, borderwidth=1)
generate_button.pack()

# Run the application
window.mainloop()
