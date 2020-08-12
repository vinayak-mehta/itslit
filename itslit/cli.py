# -*- coding: utf-8 -*-

import random
import webbrowser

import click


@click.command("itslit")
@click.pass_context
def cli(*args, **kwargs):
    """Watch a random conference lightning talk in a browser near you."""
    with open("data/lightning_talks", "r") as f:
        lightning_talks = f.read().splitlines()

    webbrowser.open(random.choice(lightning_talks), new=2)
