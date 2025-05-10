import pytest
import data
from main import BooksCollector

@pytest.fixture
def collector_whith_books():
    collector = BooksCollector()
    collector.books_genre = {
        data.books_name[0]:'',
        data.books_name[1]: collector.genre[4], 
        data.books_name[2]: collector.genre[1],
        data.books_name[3]: collector.genre[3],
        data.books_name[4]: collector.genre[3],
        data.books_name[5]: collector.genre[3],
        data.books_name[6]: collector.genre[2],
        data.books_name[7]: collector.genre[0],
    }
    collector.favorites = [data.books_name[7], data.books_name[0]]
    return collector
