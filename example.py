from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route and its handler
@app.route('/')
def hello():
    return 'Hello, Flask!'

# Run the application
if __name__ == '__main__':
    app.run()
