from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Define a single route for the homepage
@app.route('/')
def hello_world():
    return '<h1>Hello from your AI-Deployed Application!</h1><p>The DevOps Butler did its job.</p>'

# This is the most important part for Docker
if __name__ == '__main__':
    # This starts a web server that runs forever
    # and listens on all network interfaces (0.0.0.0) inside the container.
    app.run(host='0.0.0.0', port=8000)
