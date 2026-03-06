class BookShelf:
    def __init__(self):
        self.books_by_genre = {
            "Sci-Fi": ["Dune", "Foundation", "The Fifth Season"],
            "Tech": ["Clean Code", "Pragmatic Programmer"]
        }

    def __iter__(self):
        return BookShelfIterator(self.books_by_genre)


class BookShelfIterator:
    def __init__(self, data):
        self._data = data
        self._genres = list(data.keys())
        self._genre_index = 0
        self._book_index = 0

    def __next__(self):
        # 1. Check if we've run out of genres
        if self._genre_index >= len(self._genres):
            raise StopIteration

        current_genre = self._genres[self._genre_index]
        books_in_genre = self._data[current_genre]

        # 2. Check if we have more books in the current genre
        if self._book_index < len(books_in_genre):
            book = books_in_genre[self._book_index]
            self._book_index += 1
            return book
        else:
            # 3. Move to the next genre and reset book index
            self._genre_index += 1
            self._book_index = 0
            # Recursively call next to find the first book of the next genre
            return self.__next__()
        
shelf = BookShelf()
for book in shelf:
    print(book)