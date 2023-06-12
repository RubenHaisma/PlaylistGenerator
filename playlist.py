import spotipy
from spotipy.oauth2 import SpotifyOAuth

def generate_playlist():
    # Spotify API credentials
    CLIENT_ID = '810c12f9f4614384a6dfab29953cd10a'
    CLIENT_SECRET = '6914cb404b4f456bbccae03f25c0189d'
    REDIRECT_URI = 'http://localhost:3000/'

    # Scope: de toegangsrechten die je wilt voor je applicatie
    SCOPE = 'playlist-modify-private'

    # Maak een instantie van de SpotifyOAuth-klasse
    sp_oauth = spotipy.oauth2.SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPE)

    # Genereer de autorisatie-URL
    auth_url = sp_oauth.get_authorize_url()

    # Vraag de gebruiker om toegang te verlenen via de gegenereerde URL
    print("Bezoek deze URL en geef toegang:")
    print(auth_url)
    response = input("Voer de volledige URL in die je na autorisatie hebt ontvangen: ")

    # Wissel de autorisatiecode in voor een toegangstoken
    code = sp_oauth.parse_response_code(response)
    token_info = sp_oauth.get_access_token(code)

    # Verkrijg het toegangstoken uit de tokeninformatie
    access_token = token_info['access_token']

    # Maak een Spotify-object met het toegangstoken
    sp = spotipy.Spotify(auth=access_token)

    # Nu kun je de Spotify API aanroepen
    user = sp.current_user()
    print(f"Gebruikersnaam: {user['display_name']}")
    print(sp.me())


    # Stap 1: Verzamel voorkeurskenmerken van de gebruiker
    danceability = float(input("Hoe belangrijk is danceability (0.0 - 1.0)? "))
    energy = float(input("Hoe belangrijk is energy (0.0 - 1.0)? "))
    valence = float(input("Hoe belangrijk is valence (0.0 - 1.0)? "))

    # Stap 2: Zoek nummers op basis van de voorkeurskenmerken
    recommendations = sp.recommendations(seed_genres=['pop', 'rock'], limit=10, target_danceability=danceability, target_energy=energy, target_valence=valence)

    # Stap 3: Maak een nieuwe privéafspeellijst
    playlist = sp.user_playlist_create('117189269', 'My Generated Playlist', public=False, description='Playlist generated by Playlistify')

    # Stap 4: Voeg de aanbevolen nummers toe aan de afspeellijst
    track_ids = [track['id'] for track in recommendations['tracks']]
    sp.playlist_add_items(playlist['id'], track_ids)

    print("Afspeellijst is gegenereerd en nummers zijn toegevoegd.")

# Roep de generate_playlist-functie aan om een afspeellijst te genereren
generate_playlist()
