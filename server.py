"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask,render_template, redirect, request, flash, session
from model import User, Rating, Movie, connect_to_db, db
from flask_debugtoolbar import DebugToolbarExtension




app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/sign_in", methods=["POST", "GET"])
def login():
    """Login."""
    if request.method == "POST":
        email = request.form.get("email")
        print "Email: ", email
        password = request.form.get("password")
        print "Password: ", password
        user = db.session.query(User).filter(User.email == email).one()
        print "Query: ", user
        print user.password
        if password != user.password: 
            # import pdb; pdb.set_trace()
            flash('Invalid credentials, try again')
            return render_template("login.html")
        else:    
            print "SUCCESS*******************"
            session['user_id'] = user.user_id
            flash('You were successfully logged in')
            return render_template("homepage.html")       
    else: 
        return render_template("login.html") 

@app.route("/sign_out")
def logout():
    """ LOGOUT."""
    if "user_id" in session: 
        session.pop('user_id', None)
        print session
        flash('You have been logged out')
        return render_template('homepage.html')
    else: 
        flash('Are you sure you logged in?')
        return render_template('login.html')

@app.route("/users/id=")
def users_details():
    """ USER DETAILS"""
    user_id = session['user_id']
    user1 = db.session.query(User).filter_by(User.user_id).one()
    print user1

    return render_template("user_details.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()