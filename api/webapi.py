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

