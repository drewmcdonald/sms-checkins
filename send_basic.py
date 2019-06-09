from twilio.rest import Client
from dotenv import load_dotenv
from os import getenv

import click


@click.command()
@click.argument("message", required=True)
def main(message: str) -> None:
    client = Client(getenv("TWILIO_LIVE_ACCOUNT_SID"), getenv("TWILIO_LIVE_AUTH_TOKEN"))

    client.messages.create(
        to=getenv("TO_SMS_NUMBER"), from_=getenv("TWILIO_SMS_NUMBER"), body=message
    )


if __name__ == "__main__":
    load_dotenv()
    main()
