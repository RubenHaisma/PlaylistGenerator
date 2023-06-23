# Copyright (c) [2023] [Ruben Haisma]
# All rights reserved.

# Description: This file contains the application(GUI) for the Spotify Playlist Generator

import tkinter as tk
from tkinter import messagebox
from collab_filtering import collaborative_filtering
from content_filtering import content_filtering
from authenticate import authenticate
import random

def generate_playlist():
    try:
        sp, USER_ID = authenticate()
        danceability = float(danceability_slider.get())
        energy = float(energy_slider.get())
        valence = float(valence_slider.get())
        novelty_factor = float(novelty_slider.get())

        playlist_name = playlist_name_entry.get()
        playlist_length = int(playlist_length_entry.get())

        recommendations = []
        if method_var.get() == "genres":
            user_genres = genres_entry.get().split(",")
            recommendations = content_filtering(sp, danceability, energy, valence, user_genres, novelty_factor)
        elif method_var.get() == "artists":
            recommendations = collaborative_filtering(sp)
        elif method_var.get() == "both":
            user_genres = genres_entry.get().split(",")
            collaborative_recommendations = collaborative_filtering(sp)
            content_recommendations = content_filtering(sp, danceability, energy, valence, user_genres, novelty_factor)
            recommendations = collaborative_recommendations + content_recommendations
        else:
            messagebox.showerror("Error", "Invalid method chosen. Exiting...")
            return

        playlist = sp.user_playlist_create(USER_ID, playlist_name, public=False, description='Playlist generated by Playlistify')
        random.shuffle(recommendations)
        track_ids = [track['id'] for track in recommendations[:playlist_length]]
        sp.playlist_add_items(playlist['id'], track_ids)

        playlist_url = playlist['external_urls']['spotify']
        messagebox.showinfo("Success", f"Playlist is generated and tracks are added.\nYou can access it at:\n{playlist_url}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Spotify Green Color
SPOTIFY_GREEN = "#1DB954"

# Create the window
window = tk.Tk()
window.title("Playlist Generator")
window.geometry("376x678")
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

danceability_label = tk.Label(window, text="Danceability:", bg=SPOTIFY_GREEN, fg="white")
danceability_label.pack()
danceability_slider = tk.Scale(window, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, bg=SPOTIFY_GREEN, fg="white")
danceability_slider.pack()

energy_label = tk.Label(window, text="Energy:", bg=SPOTIFY_GREEN, fg="white")
energy_label.pack()
energy_slider = tk.Scale(window, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, bg=SPOTIFY_GREEN, fg="white")
energy_slider.pack()

valence_label = tk.Label(window, text="Valence:", bg=SPOTIFY_GREEN, fg="white")
valence_label.pack()
valence_slider = tk.Scale(window, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, bg=SPOTIFY_GREEN, fg="white")
valence_slider.pack()

novelty_label = tk.Label(window, text="Novelty:", bg=SPOTIFY_GREEN, fg="white")
novelty_label.pack()
novelty_slider = tk.Scale(window, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, bg=SPOTIFY_GREEN, fg="white")
novelty_slider.pack()

method_var = tk.StringVar()
method_label = tk.Label(window, text="Method (Choose one):", bg=SPOTIFY_GREEN, fg="white")
method_label.pack()
genres_radio = tk.Radiobutton(window, text="Genres", variable=method_var, value="genres", bg=SPOTIFY_GREEN, fg="white")
genres_radio.pack()
artists_radio = tk.Radiobutton(window, text="Artists", variable=method_var, value="artists", bg=SPOTIFY_GREEN, fg="white")
artists_radio.pack()
both_radio = tk.Radiobutton(window, text="Both", variable=method_var, value="both", bg=SPOTIFY_GREEN, fg="white")
both_radio.pack()

genres_label = tk.Label(window, text="Genres (comma-separated):", bg=SPOTIFY_GREEN, fg="white")
genres_label.pack()
genres_entry = tk.Entry(window)
genres_entry.pack()

# Create a space between the entry and the button
tk.Label(window, text="", bg=SPOTIFY_GREEN).pack()

# Generate...
generate_button = tk.Button(window, text="Generate Playlist", command=generate_playlist, bg='white', fg=SPOTIFY_GREEN, borderwidth=1)
generate_button.pack()

# Run the application
window.mainloop()