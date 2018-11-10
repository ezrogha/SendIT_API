from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hellooo... God Loves You"

if __name__ == "__main__":
    app.run()