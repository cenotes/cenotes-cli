import click
from cenotes_lib import crypto


def encrypt(password="", text=""):
    text = text or click.prompt("Enter cleartext")
    password = password or click.prompt(
        "Enter a password to generate the key (press enter to "
        "autogenerate one)", default="")
    return crypto.encrypt_note(text, password)


def decrypt(key="", text=""):
    text = text or click.prompt("Enter payload")
    key = key or click.prompt("Enter your decryption key")
    return crypto.decrypt_note(text, key).decode()
