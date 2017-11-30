# -*- coding: utf-8 -*-

"""Console script for cenotes_cli."""

import click

from cenotes_cli.cenotes_lib import exceptions, crypto


@click.command()
@click.option('--decrypt', '-d', is_flag=True, default=False,
              help="Choose this option to decrypt a note")
@click.option('--encrypt', '-e', is_flag=True, default=False,
              help="Choose this option to encrypt a note")
@click.option('--text', '-t', prompt="Enter payload or cleartext",
              help="The ciphertext for decryption mode "
                   "or the cleartext for encryption mode")
@click.option('--key', '-k',
              help="The key for decryption mode "
                   "or the password to generate key for encryption mode")
def main(decrypt, encrypt, text, key):
    """Console script for cenotes_cli."""
    if decrypt:
        key = key or input("Enter your decryption key:")
        print("Decryption was successful!\n"
              "Decrypted note: {0}"
              .format(crypto.decrypt_note(text, key).decode()))
    elif encrypt:
        print("Encryption was successful!\n"
              "Encrypted payload: {0}\n"
              "Key to decrypt: {1}"
              .format(*crypto.encrypt_note(text, key)))


if __name__ == "__main__":
    try:
        main()
    except exceptions.CenotesError as err:
        print("Error: {0}".format(err))
