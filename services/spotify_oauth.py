import spotipy
from spotipy.oauth2 import SpotifyOAuth

#le tue credenziali le trovi nella dashboard di prima

SPOTIFY_CLIENT_ID = "51bf99209e3f4414af0328439b291c23"
SPOTIFY_CLIENT_SECRET = "1355c56f1fa24cc0964580c2df0d3839"
SPOTIFY_REDIRECT_URI = "https://5000-samuel281020-spotifyapi-si6z4qrwax9.ws-eu117.gitpod.io/callback" #dopo il login andiamo qui
#config SpotifyOAuth per l'autenticazione e redirect uri
#config SpotifyOAuth per l'autenticazione e redirect uri


#config SpotifyOAuth per l'autenticazione e redirect uri
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private", #permessi x informazioni dell'utente
    show_dialog=True #forziamo la richiesta di inserire new credenziali
)

def get_spotify_object (token_info):
    return spotipy.Spotify(auth=token_info['access_token'])