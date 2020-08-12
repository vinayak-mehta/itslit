# -*- coding: utf-8 -*-

import os
import random
import webbrowser

import click


@click.command("itslit")
@click.pass_context
def cli(*args, **kwargs):
    """Watch a random conference lightning talk in a browser near you."""
    cwd = os.path.dirname(__file__)

    with open(os.path.join(cwd, "data/lightning_talks"), "r") as f:
        lightning_talks = f.read().splitlines()

    webbrowser.open(random.choice(lightning_talks), new=2)
