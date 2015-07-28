"""Utility file to seed ratings database from MovieLens data in seed_data/"""

from model import User, Rating, Movie, connect_to_db, db
from server import app

from flask_sqlalchemy import SQLAlchemy



# def load_users():
#     """Load users from u.user into database."""

#     lines = [line.rstrip('\n') for line in open("seed_data/u.user")]

#     for line in lines: 
#         column_data = line.split("|")
#         # print column_data[0], column_data[1], column_data[2], column_data[3], column_data[4]
#         line = User(user_id=column_data[0], email=column_data[1], password=column_data[2], age=column_data[3], zipcode=column_data[4])
#         db.session.add(line)
#         db.session.commit()
#     pass

        
def load_movies():
    """Load movies from u.item into database."""
    lines = [line.rstrip('\n') for line in open("seed_data/u.item")]    
    for line in lines: 
        column_data = line.split("|")
        #print column_data
        print column_data[0], column_data[1], column_data[2], column_data[4]
        line = Movie(movie_id=column_data[0], title=column_data[1], released_at=column_data[2], imdb_url=column_data[4])
        # db.session.add(line)
        # db.session.commit()
    pass



def load_ratings():
    """Load ratings from u.data into database."""
    pass


if __name__ == "__main__":
    connect_to_db(app)

#    load_users()
    load_movies()
    load_ratings()
