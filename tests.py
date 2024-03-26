import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize("name", ['t', 'Элегантность ежика', 'Сказка о спящей царевне и семи богатырях'])
    def test_add_new_book_correct_symbol_quantity(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_real_genre(self):
        collector = BooksCollector()
        name = 'Смилла и её чувство снега'
        genre = 'Детективы'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_new_book(self):
        collector = BooksCollector()
        name = 'Чапаев и пустота'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    def test_get_books_with_specific_genre_real_genre(self):
        collector = BooksCollector()
        name = 'История одного города'
        genre = 'Комедии'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_genre(self):
        collector = BooksCollector()
        name = 'История одного города'
        genre = 'Комедии'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == collector.books_genre

    @pytest.mark.parametrize('name,genre', [['1984','Фантастика'], ['Маугли','Мультфильмы'], ['12 стульев', 'Комедии']])
    def test_get_books_for_children_allowed_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == [name]

    def test_add_book_in_favorites_repeat_book(self):
        collector = BooksCollector()
        name = 'Чапаев и пустота'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_real_book(self):
        collector = BooksCollector()
        name = 'Чапаев и пустота'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        name = 'Элегантность ежика'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]

    def test_default_value_books_genre(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}
