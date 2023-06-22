# PlaylistGenerator

PlaylistGenerator is a Python algorithm that utilizes collaborative and content filtering to generate personalized playlists based on your music preferences. The algorithm now includes a graphical user interface (GUI) for an enhanced user experience.

## How It Works

1. The algorithm connects to the Spotify API using the provided client ID, client secret, and redirect URI. It requests access to the required permissions via Spotify OAuth.

2. The GUI will open, allowing you to input your music preferences for danceability, energy, valence, and playlist length. You can adjust the sliders to set the desired levels for each preference.

3. You can choose between different playlist generation methods: "Genres," "Artists," or "Both." Select the option that suits your preference.

4. If you choose "Genres" or "Both," you can enter your preferred genres (comma-separated) in the corresponding entry field.

5. Click the "Generate Playlist" button, and the algorithm will generate a personalized playlist based on your preferences.

6. The algorithm applies collaborative filtering or content filtering (or both) based on the chosen method and preferences to generate a diverse set of recommended tracks.

7. Finally, a new private playlist is created in your Spotify account with the generated recommended tracks.

## Customizing to Your Taste

You can customize the algorithm to better align with your own taste and preferences:

- Change the API credentials in `authenticate.py` to your own API credentials to make sure the playlist is created on your account. If not, you'll be provided with a link where you can see your new playlist!

- Adjust the parameters for collaborative and content filtering in the `collaborative_filtering` and `content_filtering` functions. This allows you to modify the criteria for similar users, musical attributes, and novelty.

- Experiment with the input preferences for danceability, energy, valence, and playlist length in the GUI to tailor the generated playlists to your personal taste.

## Requirements

- Python 3.x
- Spotipy library (`pip install spotipy`)

## Usage

1. Enter the required Spotify API details (client ID, client secret, redirect URI) in the `generate_playlist` function in the `gui.py` file.

2. Ensure you have Python and the required libraries installed.

3. Run the `gui.py` script, and the GUI window will open.

4. Use the sliders to set your preferences for danceability, energy, valence, and the playlist length. Choose the playlist generation method and enter your preferred genres (if applicable).

5. Click the "Generate Playlist" button, and the algorithm will generate a personalized playlist based on your preferences.

6. A new private playlist will be automatically created in your Spotify account with the generated recommended tracks.