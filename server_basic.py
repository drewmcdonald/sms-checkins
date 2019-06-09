from flask import Flask, request, redirect
from twilio.twiml.messaging_response import Message, MessagingResponse


app = Flask(__name__)


def process_message(message: str) -> None:
    pass


@app.route("/response", methods=["POST"])
def inbound_sms():
    message = request.values.get("Body", None)

    if message == "pause":
        resp = MessagingResponse()
        resp.message("okay, okay...")
        return str(resp)

    return process_message(message)


if __name__ == "__main__":
    app.run(debug=True)
