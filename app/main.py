from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from the AI-deployed Butler!"

if __name__ == '__main__':
    # This is the crucial part. It must listen on 0.0.0.0 to be
    # accessible from outside the container.
    app.run(host='0.0.0.0', port=8000)
