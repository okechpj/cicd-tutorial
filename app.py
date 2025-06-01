from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from GitHub Actions + Flask! and the entire community'

if __name__ == '__main__':
    app.run(debug=True)
