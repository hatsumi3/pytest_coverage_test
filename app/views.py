from app import app
from app.greets import greet

@app.route('/')
def index():
    name = greet("world")
    return name