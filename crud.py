""""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(
        title=title,
        overview=overview,
        release_date=release_date,
        poster_path=poster_path,
    )

    return movie


def get_movies():
    """Returns all movies."""

    return Movie.query.all()


def get_movie_by_id(movie_id):
    # we ended hereeee
    return Movie.query.get(movie_id)


def get_users():
    """Returns all users."""
    return User.query.all()


def get_user_by_id(user_id):
    """Returns user."""

    return User.query.get(user_id)


def get_user_by_email(user_email):
    """Returns user by email."""

    return User.query.get.filter(User.email == email).first()


# def show_movie():
#     """Returns movie details."""

#     return Movie.query.get(1)


def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    return rating


# for n in range(10):
#     email = f'user{n}@test.com'  # Voila! A unique email!
#     password = 'test'

#     user =

    # TODO: create a user here

    # TODO: create 10 ratings for the user


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
