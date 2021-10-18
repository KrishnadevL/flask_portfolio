import random

from flask import Blueprint, jsonify


api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

jokes = []
joke_list = [
    "The Notebook",
    "The Hate U Give",
    "Ferris Bueller's Day Off",
    "Dilwale Dulhania Le Jayenge",
    "Parasite",
    "Titanic",
    "Casablanca",
    "A Star Is Born",
    "The Farewell",
    "Rebel Without a Cause",
    "Carmen Jones",
    "Promising Young Woman",
    "Jaws",
    "The Shining",
    "Monty Python and the Holy Grail",
    "Life is Beautiful",
    "Dead Poets Society",
    "Jurassic Park (1993)",
    "Call Me By Your Name",
    "The Dark Knight",
    "To Kill a Mockingbird",
    "Legally Blonde",
    "Lady Bird",
    "Get Out",
    "Silver Linings Playbook",
    "Mean Girls",
    "Little Women (2019)",
    "10 Things I Hate About You",
    "Clueless",
    "Pulp Fiction",
    "The Shawshank Redemption"
]


def _find_next_id():
    return max(jokes["id"] for joke in jokes) + 1


def _init_jokes():
    id = 1
    for joke in joke_list:
        jokes.append({"id": id, "joke": joke, "haha": 0, "boohoo": 0})
        id += 1


@api_bp.route('/joke')
def get_joke():
    if len(jokes) == 0:
        _init_jokes()
    return jsonify(random.choice(jokes))


@api_bp.route('/jokes')
def get_jokes():
    if len(jokes) == 0:
        _init_jokes()
    return jsonify(jokes)


if __name__ == "__main__":
    print(random.choice(joke_list))