from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """ User game decision"""
    game = request.args.get("game")
    if game == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    """ Story of the person"""
    # person = request.args['person]
    person = request.args.get("person", "Maddie")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    animals = request.args.getlist("animals")

    return render_template("madlib.html", the_person=person, color=color, noun=noun, adjective=adjective, animals=animals)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
