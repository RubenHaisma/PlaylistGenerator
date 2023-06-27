# Copyright (c) [2023] [Ruben Haisma]
# All rights reserved.

# Description: This file contains the application(GUI) for the Spotify Playlist Generator

import tkinter as tk
from tkinter import messagebox
from content_filtering import content_based_filtering
from authenticate import authenticate

def generate_playlist():
    try:
        sp = authenticate()
        top_n = int(playlist_length_entry.get())
        playlist_name = playlist_name_entry.get()

        # Generate playlist using content-based filtering
        recommendations = content_based_filtering(sp, top_n)

        # Create a new playlist
        playlist_description = "Playlist generated using content-based filtering"
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
window.geometry("376x178")
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

# Create a space between the entry and the button
tk.Label(window, text="", bg=SPOTIFY_GREEN).pack()

# Generate...
generate_button = tk.Button(window, text="Generate Playlist", command=generate_playlist, bg='white', fg=SPOTIFY_GREEN, borderwidth=1)
generate_button.pack()

# Run the application
window.mainloop()
