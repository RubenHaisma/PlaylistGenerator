import spotipy
from spotipy.oauth2 import SpotifyOAuth

def authenticate():
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

    return sp

authenticate()
