import requests
from bs4 import BeautifulSoup

def get_movie_info(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find('span', attrs={'data-testid': 'hero__primary-text'})
        title = title_tag.text if title_tag else 'Название не найдено'

        description_tag = soup.find('span', attrs={'data-testid': 'plot-xl'})
        description = description_tag.text if description_tag else 'Описание не найдено'

        return {
            'title': title,
            'description': description
        }
    except Exception as e:
        print(f'Ошибка при получении данных с сайта: {e}')
        return None

def get_movie_url(title):

    title = title.replace(" ", "+")
    url = f"https://www.imdb.com/find?q={title}&s=tt&exact=true&ref_=fn_tt_ex"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        movie_link = soup.find('a', href=True, attrs={'class': "ipc-metadata-list-summary-item__t"})
        if movie_link:
            return f"https://www.imdb.com{movie_link['href']}"
        else:
            print("Фильм не найден.")
            return None
    except Exception as e:
        print(f"Ошибка при поиске фильма: {e}")
        return None
if __name__ == "__main__":
    movie_title = input("Введите название фильма: ")
    movie_url = get_movie_url(movie_title)

    if movie_url:
        print(f"URL найденного фильма: {movie_url}")

        movie_info = get_movie_info(movie_url)
        if movie_info:
            print(f"Название: {movie_info['title']}")
            print(f"Описание: {movie_info['description']}")
