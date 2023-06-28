# PlaylistGenerator

PlaylistGenerator is a Python algorithm that utilizes a hybrid of content-based filtering and collaborative filtering to generate personalized playlists based on your music preferences. The algorithm includes a graphical user interface (GUI) for an enhanced user experience.

## How It Works

1. The algorithm connects to the Spotify API using the provided client ID, client secret, and redirect URI. It requests access to the required permissions via Spotify OAuth.

2. Once you run the application, you can input your credentials. Along with the number of songs you want in the playlist, the name of your playlist and how you want the recommendations to be generated (content-, collab- or hybrid-filtering).

3. Based on your choice, the algorithm generates recommendations using the selected filtering technique:

   - Content-based filtering: Generates recommendations based on the features of your top tracks.
   - Collaborative-filtering: Generates recommendations based on the listening history and similarity with other users.
   - Hybrid-filtering: Combines both content-based and collaborative filtering for more accurate recommendations.

4. The algorithm creates a new private playlist on your Spotify account with the generated recommended tracks.

## Customizing to Your Taste

You can customize the algorithm to better align with your own taste and preferences:

- Change the API credentials in `authenticate.py` to your own API credentials to make sure the playlist is created on your account. If not, you'll be provided with a link where you can see your new playlist!

- Adjust the parameters for content-based filtering and collaborative filtering in their respective functions (`content_based_filtering`, `collab_based_filtering`, `hybrid_filtering`). This allows you to modify the criteria and fine-tune the recommendations based on your preferences.

## Requirements

- Python 3.x
- Spotipy library (`pip install spotipy`)
- scikit-learn (`pip install scikit-learn`)
- Pandas (`pip install pandas`)
- Spotify API Keys

To install the requirements for this application, simply run 'pip install requirements.txt' in the terminal of your directory.

## Obtaining the Spotify API Keys

1. Log into the dashboard using your Spotify account.

2. Create an app. Once you have created your app, you will have access to the app credentials. These will be required for API authorization to obtain an access token.

3. Use the access token in your API requests.


## Usage of the Application (GUI)

1. Ensure you have Python and the required libraries installed.

2. Run the `gui.py` script, and the GUI window will open.

3. Use the GUI to input your Spotify API details: client ID, client secret, redirect URI. (The standard redirect URI = http://localhost:3000/)

4. Come up with an original name for your playlist and enter the amount of recommended tracks you want in your newly created playlist.

5. Click the "Generate Playlist" button, and the algorithm will generate a personalized playlist based on your preferences and Spotify data.

6. A new private playlist will be automatically created in your Spotify account with the generated recommended tracks.



## Sources
Main source for creating algorithms: 
- Spotify Developer. Web API, van https://developer.spotify.com/documentation/web-api/
- F.O. Isinkaye. Recommendation systems: Principles, methods and evaluation, van https://www.sciencedirect.com/science/article/pii/S1110866515000341#s0160
- Hucker Marius. Uncovering How the Spotify Algorithm Works, van https://towardsdatascience.com/uncovering-how-the-spotify-algorithm-works-4d3c021ebc0
- Medium. (2022). Collaborative Filtering for Music Recommendation, van https://medium.com/ @17it089/music-recommendation-system-3b0f2312192b.
- US Brand Colors. Spotify Colors, van https://usbrandcolors.com/spotify-colors/#:~:text=The%20official%20Spotify%20colors%20are,to%20visit%20the%20company%20website.
- Python, Tkinter Dialogs, van https://docs.python.org/3/library/dialog.html
- PythonProgramming.altervista.org. Nice GUI Graphic for Tkinter with TTK and Azure Theme, van https://pythonprogramming.altervista.org/nice-gui-graphic-for-tkinter-with-ttk-and-azure-theme-from-this-guy/
- Dane Hillard, Effective Python Testing with Pytest, van https://realpython.com/pytest-python-testing/

---

© 2023 Ruben Haisma. All rights reserved.
