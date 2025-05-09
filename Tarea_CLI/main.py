"""
Click usage example
"""

import click
from datetime import date
from random import randint

@click.group()
def cli():
    pass


@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        print(f"Hello, {name}!")

@cli.command()
@click.option("-m", default="Nothing happened", help="Message for today's journal.")
def journal(m):
    print(f"{date.today()}: {m}")

@cli.command()
@click.option("-h", is_flag=True, help="Pick heads.")
@click.option("-t", is_flag=True, help="Pick tails.")
def cf(h, t):
    """Flip a coin and guess heads or tails."""
    if h and t:
        print("You can't pick both heads and tails!")
        return
    elif not h and not t:
        print("You must pick either heads (-h) or tails (-t)!")
        return

    choice = 0 if h else 1  # 0: heads, 1: tails
    result = randint(0, 1)

    print(f"The coin landed on: {'heads' if result == 0 else 'tails'}")

    if result == choice:
        print("You win!")
    else:
        print("You lost...")
    


if __name__ == '__main__':
    cli()
