import random
from .questions import GK_QUESTIONS

def get_all():
    """Returns the full list of questions."""
    return GK_QUESTIONS

def get_random(count=1):
    """Returns a list of random questions. Default is 1."""
    if count > len(GK_QUESTIONS):
        count = len(GK_QUESTIONS)
    return random.sample(GK_QUESTIONS, count)

def search(keyword):
    """Search for questions containing a specific word."""
    return [q for q in GK_QUESTIONS if keyword in q['question']]