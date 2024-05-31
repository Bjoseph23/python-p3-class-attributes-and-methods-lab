class Song:
    genres = []
    artists = []
    count = 0
    genre_counts = {}  
    artist_counts = {}  

    def __init__(self, name, artist, genre):
        self.name = name
        self.genre = genre
        self.artist = artist
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def show_genres(cls):
        print(cls.genres)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_counts[genre] = cls.genre_counts.get(genre, 0) + 1

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)
        if artist not in cls.artist_counts:
            cls.artist_counts[artist] = 0

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_counts[artist] += 1

    @classmethod
    def show_artists(cls):
        print(cls.artists)

ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
bohemian_rhapsody = Song("Bohemian Rhapsody", "Queen", "Rock")
basket_case = Song("Basket Case", "Green Day", "Punk Rock")

print(ninety_nine_problems.name, ninety_nine_problems.artist, ninety_nine_problems.genre)
print(f"Total Songs: {Song.count}")
print(f"Total genres: {Song.genre_counts}")
print(f"Total artsts: {Song.artist_counts}")

Song.show_genres()
Song.show_artists()
