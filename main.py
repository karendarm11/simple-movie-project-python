
def add_movie():
    movie_title = input('Insert the movie name: ')
    movie_director = input('Insert the movie director name: ')
    movie_release_year = input('Insert the movie release year: ')
    new_movie = {
        'title': movie_title,
        'director': movie_director,
        'release_year': movie_release_year
    }
    movie_list.append(new_movie)


def list_movies():
    for movie in movie_list:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['release_year']}")


def find_movie_by_title():
    movie_title = input('Enter the name of the movie you want to find: ')
    for movie in movie_list:
        if movie['title'].upper() == movie_title.upper():
            print_movie(movie)
        else:
            print('There is not such a movie in your list')


if __name__ == '__main__':
    INPUT_PROMPT = 'Enter a to add a movie, l to list the current movie list, f to find a movie by name, or q to quite: '
    option = input(INPUT_PROMPT)
    user_options = {
        'a': add_movie,
        'l': list_movies,
        'f': find_movie_by_title
    }
    movie_list = []
    while option != 'q':
        if option in user_options:
            selected_function = user_options[option]
            selected_function()
        else:
            print('Invalid option')
        option = input(INPUT_PROMPT)
