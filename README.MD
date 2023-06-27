# PlaylistGenerator

PlaylistGenerator is a Python algorithm that utilizes collaborative and content filtering to generate personalized playlists based on your music preferences. The algorithm includes a graphical user interface (GUI) for an enhanced user experience.

## How It Works

1. The algorithm connects to the Spotify API using the provided client ID, client secret, and redirect URI. It requests access to the required permissions via Spotify OAuth.

2. The GUI will open, click the "Generate Playlist" button, and the algorithm will generate a personalized playlist based on your listening history.

3. The algorithm applies content filtering based on the preferences to generate a diverse set of recommended tracks.

4. Finally, a new private playlist is created in your Spotify account with the generated recommended tracks.

## Customizing to Your Taste

You can customize the algorithm to better align with your own taste and preferences:

- Change the API credentials in `authenticate.py` to your own API credentials to make sure the playlist is created on your account. If not, you'll be provided with a link where you can see your new playlist!

- Adjust the parameters for content filtering in the `content_filtering` functions. This allows you to modify the criteria for, for instance the 'medium term'.

## Requirements

- Python 3.x
- Spotipy library (`pip install spotipy`)
- scikit-learn (`pip install scikit-learn`)

## Usage

1. Enter the required Spotify API details (client ID, client secret, redirect URI) in the `authenticate.py` file.

2. Ensure you have Python and the required libraries installed.

3. Run the `gui.py` script, and the GUI window will open.

4. Use the GUI to set a name for your new playlist.

5. Click the "Generate Playlist" button, and the algorithm will generate a personalized playlist based on your listening history.

6. A new private playlist will be automatically created in your Spotify account with the generated recommended tracks.
