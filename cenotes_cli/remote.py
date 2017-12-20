from urllib import parse

import click
import requests
from dateutil import parser

from cenotes_cli.crypto import encrypt


def parse_date(some_date):
    try:
        date = parser.parse(some_date)
    except (ValueError, OverflowError):
        raise click.BadParameter("Couldn't understand date.", param=some_date)
    return date.isoformat()


def parse_decrypt_link(link):
    try:
        parsed_url = parse.urlparse(link)
        server = "{0}://{1}".format(parsed_url.scheme, parsed_url.netloc)
        payload, key = parsed_url.path.strip("/decrypt/").split("/")

    except (ValueError, AttributeError):
        raise click.BadParameter("Couldn't extract payload & key from link",
                                 param=link)
    return server, payload, key


def craft_upload_params(text=""):
    text = text or click.prompt("Enter cleartext")
    password = click.prompt(
        "Enter a password to generate the key (press enter to "
        "autogenerate one)", default="")
    end_date = click.prompt("Enter an expiration date", value_proc=parse_date)
    max_visits = click.prompt("Enter maximum visits count",
                              type=int, default=1)
    return dict(plaintext=text, key=password, expiration_date=end_date,
                max_visits=max_visits, no_store=False)


def uploader(server):
    payload, key = "", ""
    if click.confirm("Do you want to locally encrypt the note?"):
        payload, key = encrypt()
        print("--------------------------\n"
              "Encryption was successful!\nEncrypted payload: {0}\n"
              "Key to decrypt: {1}\n"
              "--------------------------\n".format(payload, key))

    params = craft_upload_params(payload)
    response = requests.post(parse.urljoin(server, "/notes/encrypt/"),
                             json=params)
    response.raise_for_status()
    return response.json()


def fetch(server):
    if click.confirm("Do you have a direct link to the note?"):
        server, payload, key = click.prompt("Enter link to note",
                                            value_proc=parse_decrypt_link)
    else:
        payload, key = click.prompt("Enter payload"), click.prompt("Enter key")

    response = requests.post(parse.urljoin(server, "/notes/"),
                             json=dict(payload=payload, key=key))
    response.raise_for_status()
    return response.json()
