def make_album(artist_name,album_title):
    """Build a dictionary for an album"""
    album = {
        'artist':artist_name.title(),
        'album':album_title.title(),
        }
    return album
while True:
    print("Please enter the name of the artist and the album title")
    print("(Enter q at any point to quit)")
    artist = input('Artist: ')
    if artist=='q':
        break
    album_title = input('Album Title: ')
    if artist=='q':
        break
    album_details= make_album(artist,album_title)
    print(album_details)
print('\nThanks for responding')