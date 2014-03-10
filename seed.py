import model
import csv, codecs, cStringIO
import datetime
import sqlalchemy

"""open a file
read a line
parse a line
create an object
add the object to a session
commit
repeat until done
Each of the files is formatted slightly differently, so you'll need to write
slightly different functions for each."""

#Parsing titles (removing year of release) Parsing datetimes


def load_users(session):
    with open('seed_data/u.user', 'rb') as f:
        reader = csv.reader(f)
        #iterate over lines in the csvfile, Each row read from
        # the csv file is returned as a list of strings
        for row in reader:
        # setting row info from file as an object to go into the database
        # split the rows on | 
            row_data = row[0].split('|')
            u_id = row_data[0]
            u_age = row_data[1]
            u_password = row_data[3]
            u_zipcode = row_data[4]
            # Making the object
            u = model.User(password=u_password, age=u_age, zipcode=u_zipcode)
            u.id = u_id
            session.add(u)
        session.commit()


def load_movies(session):
    # Using the open() function with mode rt to read a text file, LIKE A BOSS!
    with open('seed_data/u.item', 'rb') as f:
        # creates the reader object, cause I said so!
        reader = csv.reader(f, delimiter=" ", quotechar='|') 
        # iterates the rows of the file in order because being disorganized
        # gives the code the creeps.
        for row_data in reader: 
            id = row_data[0]
            name = row_data[1].decode("latin-1")
            if len(row_data[2]) > 0:
                # using the datetime module to timestamp, then adding strptime
                # to create a string representing the time. BAM!
                released_at = datetime.datetime.strptime(row_data[2], "%d-%b-%Y")
            imdb_url = row_data[4]
            if released_at:
                m = model.Movie(name=name, released_at=released_at, imdb_url=imdb_url)
            m.id=id
            session.add(m)
        try:
            session.commit()
        except sqlalchemy.exc.IntegrityError, m:
            session.rollback()


def load_ratings(session):
    # use u.data
    with open('seed_data/u.data', 'rb') as f:
        reader = csv.reader(f, delimiter="\t")
        for row_data in reader:
            user_id = row_data[0]
            movie_id = row_data[1]
            rating = row_data[2]
            r = model.Rating(movie_id=movie_id, rating=rating, user_id=user_id)
            session.add(r)
    session.commit()



def main(session):
    load_users(session)
    load_movies(session)
    load_ratings(session)


if __name__ == "__main__":
    s= model.connect()
    main(s)