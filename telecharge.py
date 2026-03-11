import yt_dlp
import os

def telecharger_media():
    # 1. Demander le lien à l'utilisateur
    url = input("Colle l'URL de la vidéo YouTube : ")
    
    # 2. Demander le format
    print("\nQue veux-tu faire ?")
    print("1. Télécharger l'AUDIO (MP3)")
    print("2. Télécharger la VIDÉO (MP4)")
    choix = input("Choisis 1 ou 2 : ")

    # 3. Configuration des options yt-dlp
    if choix == '1':
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'Telechargements/Musique/%(title)s.%(ext)s', # Dossier spécifique
        }
    else:
        ydl_opts = {
            # On demande un format qui contient DEJA la vidéo et l'audio ensemble
            'format': 'best[ext=mp4]/best', 
            'outtmpl': 'Telechargements/Videos/%(title)s.%(ext)s',
        }

    # 4. Exécution du téléchargement
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("\nInitialisation... (ça peut prendre quelques secondes)")
            ydl.download([url])
            print("\nTerminé ! Ton fichier est dans le dossier 'Telechargements'.")
    except Exception as e:
        print(f"Oups, une erreur est survenue : {e}")

if __name__ == "__main__":
    # Créer les dossiers s'ils n'existent pas
    if not os.path.exists('Telechargements'):
        os.makedirs('Telechargements/Musique')
        os.makedirs('Telechargements/Videos')
        
    telecharger_media()