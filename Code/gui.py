import tkinter as tk
from tkinter import messagebox
from content_filtering import content_based_filtering
from collab_filtering import create_user_track_matrix, collab_based_filtering
from authenticate import authenticate
from hybrid_filtering import hybrid_filtering

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
window.geometry("376x520")
window.configure(bg=SPOTIFY_GREEN)

# Create the widgets
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




# Copyright (c) 2023 Ruben Haisma
# All rights reserved.