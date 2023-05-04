# tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
#                       "On the Other Side": "Samara"},
#           "Cure": {"Disintegration": "Lovesong",
#                    "Wish": "Friday I'm in love"}}

def tracklist(**tracks):
    for artist, albums in tracks.items():
        print(artist)
        for album, track in albums.items():
            print('ALBUM:', album, 'TRACK:', track)

# tracklist(tracks)