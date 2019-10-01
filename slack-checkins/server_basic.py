from flask import Flask

app = Flask(__name__)


def process_message(message: str) -> str:
    return message


@app.route("/response", methods=["POST"])
def response():
    pass


if __name__ == "__main__":
    app.run(debug=True)
