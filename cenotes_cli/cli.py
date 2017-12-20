# -*- coding: utf-8 -*-

"""Console script for cenotes_cli."""

import click
import requests
import json
from urllib import parse


from cenotes_lib import exceptions
from cenotes_cli.crypto import encrypt as encrypter, decrypt as decrypter
from cenotes_cli.remote import uploader, fetch as fetcher


@click.command()
@click.option('--decrypt', '-d', is_flag=True, default=False,
              help="Choose this option to decrypt a note")
@click.option('--encrypt', '-e', is_flag=True, default=False,
              help="Choose this option to encrypt a note")
@click.option('--fetch', '-f', is_flag=True, default=False,
              help="Choose this option to fetch an uploaded note")
@click.option('--upload', '-u', is_flag=True, default=False,
              help="Choose this option to upload a note")
@click.option('--server', '-s', type=str, help="URL to cenotes server",
              default="https://cenot.es/")
@click.option('--text', '-t',
              help="The ciphertext for decryption mode "
                   "or the cleartext for encryption mode")
@click.option('--password', '-p',
              help="The password to generate a encryption/decryption key")
@click.option('--key', '-k',
              help="The key to decrypt")
def main(decrypt, encrypt, fetch, upload, server, text, password, key):
    """Console script for cenotes_cli."""
    try:
        if decrypt:
            print("Decryption was successful!\nDecrypted note: {0}"
                  .format(decrypter(key, text)))
        elif encrypt:
            print("Encryption was successful!\nEncrypted payload: {0}\n"
                  "Key to decrypt: {1}".format(*encrypter(password, text)))
        elif fetch:
            plaintext = fetcher(server).get("plaintext")
            print(
                "\nFetching was successful!\n"
                "Plaintext: {0}".format(plaintext)
            )
        elif upload:
            response = uploader(server)
            payload, key, dkey = map(lambda x: response.get(x, ""),
                                     ("payload", "key", "duress_key"))
            decrypt_url = "{0}{1}".format(
                parse.urljoin(server, "/decrypt/"), payload)
            print(
                "\nUploading successful!\n"
                "Link to decrypt:\n{link}\n"
                "Link to delete note:\n{dlink}\n\n"
                "-------ADVANCED INFO-------\n"
                "Payload: {payload}\n"
                "Decryption key: {key}\n"
                "Duress key: {dkey}".format(
                    link="{0}/{1}".format(decrypt_url, key),
                    dlink="{0}/{1}".format(decrypt_url, dkey),
                    payload=payload, key=key, dkey=dkey
                )
            )
    except exceptions.CenotesError as err:
        print("Error: {0}".format(err))
    except requests.RequestException as err:
        print_cenotes_error(err)


def print_cenotes_error(err):
    print("Error: {0}".format(err))
    try:
        print(json.loads(err.response.text).get("error", ""))
    except json.JSONDecodeError:
        pass


if __name__ == "__main__":
    main()
