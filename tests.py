from main import BooksCollector
import data
import pytest


class TestBooksCollector:

    def test_add_new_book_add_name_book_is_true(self, collector_whith_books):
        collector_whith_books.add_new_book('1984')

        assert '1984' in collector_whith_books.get_books_genre()

    @pytest.mark.parametrize(
            'name', 
            [ 
                (''), 
                ('Книга с самым длинным названием в вашей библиотеке') 
            ] 
    )
    def test_add_new_book_name_book_is_fail(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_set_genre_to_book(self, collector_whith_books):
        collector_whith_books.set_book_genre(data.books_name[0], collector_whith_books.genre[4])
        assert collector_whith_books.books_genre.get(data.books_name[0]) == collector_whith_books.genre[4]

    def test_get_book_genre_returne_book_genre_by_name(self, collector_whith_books):
        assert collector_whith_books.get_book_genre(data.books_name[2]) == collector_whith_books.genre[1]

    def test_get_books_with_specific_genre_list_books_by_genre(self, collector_whith_books):
        assert collector_whith_books.get_books_with_specific_genre(collector_whith_books.genre[3]) == [data.books_name[3], data.books_name[4], data.books_name[5]] #['Дети с Горластой улицы', 'Алиса в Зазеркалье', 'Винни-Пух идет в гости']

    def test_get_books_genre_return_dict_books_genre(self, collector_whith_books):
        assert collector_whith_books.get_books_genre() == data.books_genre_dict

    def test_get_books_for_children_list_children_book(self, collector_whith_books):
        assert collector_whith_books.get_books_for_children() == data.list_children_book

    def test_add_book_in_favorites_add_one_book(self, collector_whith_books):
        favorit_list_len = len(collector_whith_books.favorites)
        collector_whith_books.add_book_in_favorites(data.books_name[1])
        assert len(collector_whith_books.favorites) > favorit_list_len

    def test_delete_book_from_favorites_list_del_one_book(self, collector_whith_books):
        favorit_list_len = len(collector_whith_books.favorites)
        collector_whith_books.delete_book_from_favorites(data.books_name[7])
        assert len(collector_whith_books.favorites) == favorit_list_len-1

    def test_get_list_of_favorites_books_list_not_empty(self, collector_whith_books):
        assert collector_whith_books.get_list_of_favorites_books()
