import os
from flask import Flask, render_template, request, url_for, redirect, flash, Markup, abort

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

site = {
    'name': 'myMDB'
}

# declare user dictionary
user = {
    'username': 'Python Web',
    'bio': 'We love Python.',
}

# declare list of movies
movies = [
    {'title': 'V for Vendetta', 'year': 2005, 'rating': 8.2, 'description': 'In a future British tyranny, a shadowy freedom fighter, known only by the alias of "V", plots to overthrow it with the help of a young woman.',
        'imdb_url': 'https://www.imdb.com/title/tt0434409/', 'image_url': 'https://m.media-amazon.com/images/M/MV5BOTI5ODc3NzExNV5BMl5BanBnXkFtZTcwNzYxNzQzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg'},
    {'title': 'Memento', 'year': 2000, 'rating': 8.4, 'description': 'A man with short-term memory loss attempts to track down his wife\'s murderer.', 'imdb_url': 'https://www.imdb.com/title/tt0209144/',
        'image_url': 'https://m.media-amazon.com/images/M/MV5BZTcyNjk1MjgtOWI3Mi00YzQwLWI5MTktMzY4ZmI2NDAyNzYzXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY268_CR0,0,182,268_AL_.jpg'},
    {'title': 'Coco', 'year': 2017, 'rating': 8.4, 'description': 'Aspiring musician Miguel, confronted with his family\'s ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.',
        'imdb_url': 'https://www.imdb.com/title/tt2380307/', 'image_url': 'https://m.media-amazon.com/images/M/MV5BYjQ5NjM0Y2YtNjZkNC00ZDhkLWJjMWItN2QyNzFkMDE3ZjAxXkEyXkFqcGdeQXVyODIxMzk5NjA@._V1_UY268_CR3,0,182,268_AL_.jpg'},
    {'title': 'The Lion King', 'year': 1994, 'rating': 8.0, 'description': 'To survive and grow into a powerful adult lion, Simba must perfect his savage pounce and master fighting with all four paws. Scrap with hyenas, dash through an elephant graveyard, defeat your evil uncle Scar and recapture the Pridelands.',
        'imdb_url': 'https://www.imdb.com/title/tt0323073/', 'image_url': 'https://m.media-amazon.com/images/M/MV5BNzVmNzQ2ZmYtMmUzNy00MzhjLTg4ODUtMTQ0MjMzYTdkMDg5XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR5,0,182,268_AL_.jpg'},
    {'title': 'The Matrix', 'year': 1999, 'rating': 8.7, 'description': 'When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.',
        'imdb_url': 'https://www.imdb.com/title/tt0133093/', 'image_url': 'https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg'},
    {'title': 'The Hitchhiker\'s Guide to the Galaxy', 'year': 2005, 'rating': 6.8, 'description': 'Mere seconds before the Earth is to be demolished by an alien construction crew, journeyman Arthur Dent is swept off the planet by his friend Ford Prefect, a researcher penning a new edition of \"The Hitchhiker\'s Guide to the Galaxy.\"',
        'imdb_url': 'https://www.imdb.com/title/tt0371724', 'image_url': 'https://m.media-amazon.com/images/M/MV5BZmU5MGU4MjctNjA2OC00N2FhLWFhNWQtMzQyMGI2ZmQ0Y2YyL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg'}
]

top_rated_movies = [
    {'title': 'The Shawshank Redemption', 'year': 1994, 'rating': 9.2,
        'imdb_url': 'https://www.imdb.com/title/tt0111161/'},
    {'title': 'The Godfather', 'year': 1972, 'rating': 9.1,
        'imdb_url': 'https://www.imdb.com/title/tt0068646/'},
    {'title': 'The Godfather: Part II', 'year': 1974, 'rating': 9.0,
        'imdb_url': 'https://www.imdb.com/title/tt0071562/'},
    {'title': 'The Dark Knight', 'year': 2008, 'rating': 9.0,
        'imdb_url': 'https://www.imdb.com/title/tt0468569/'},
    {'title': 'Angry Men', 'year': 1957, 'rating': 8.9,
        'imdb_url': 'https://www.imdb.com/title/tt0050083/'}
]


@app.route('/')
def index():
    return render_template('index.html', site=site)


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', movies=movies, site=site)


@app.route('/top_rated')
def top_rated():
    return render_template('top-rated.html', top_rated_movies=top_rated_movies, site=site)


@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'GET':
        return render_template('add-movie.html', site=site)
    else:
        # Read values from form
        title = request.form['title']
        year = request.form['year']
        rating = request.form['rating']
        description = request.form['description']
        imdb_url = request.form['imdbURL']
        image_url = request.form['imageURL']

        # Create a dictionary with the values from the form
        my_movie = {'title': title, 'year': year, 'rating': rating, 'description': description,
            'imdb_url': imdb_url, 'image_url': image_url}

        # Add movie to our list of movies
        movies.append(my_movie)

        return redirect(url_for('watchlist'))


@app.route('/raise_500')
def raise_500():
    abort(500)

# register template global function


@app.template_global()
def global_message():
    return 'I am global message.'

# register template filter


@app.template_filter()
def musical(s):
    return s + Markup(' &#9835;')

# message flashing


@app.route('/flash')
def just_flash():
    flash('I am Flash, who is looking for me?')
    # flash('I am Flash, again.')

    return redirect(url_for('index'))


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html', site=site), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html', site=site), 500
