def make_album(artist_name,album_title,song_no=None):
    """Build a dictionary for an album"""
    if song_no:
        album = {'artist':artist_name.title(),'album':album_title.title(),'number of songs':song_no}
    else:
        album = {'artist':artist_name.title(),'album':album_title.title()}
    return album
albums = make_album('wizkid','morayo')
print(albums)
albums = make_album('kendrick lamar','damn',14)
print(albums)
albums = make_album('show dem camp','clone war IV')
print(albums)
albums = make_album('nas',"king's disease II",15)
print(albums)
