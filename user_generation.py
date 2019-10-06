"""
This Python program generates random robots, monsters, advanced robots and kittens from 2 APIs.
The first API is for the generation of user names from uinames.com.
The second one is from Robohash.org.
It exports the results to a json file.
"""

import random
import requests
import json


# a list of regions in prep for the uinames API
regions = ['australia', 'canada', 'denmark', 'england', 'ireland', 'sweden', 'switzerland', 'united states']

# a dict of race in prep of Robohash
race = {
    "robots": "set1",
    "monsters": "set2",
    "advanced_robots": "set3",
    "kittens": "set4"
}


def main():
    region = random_region(regions)
    race = random_race(race)


def generate_users_and_photo(region: str, ROBOHASH_URL: str):
    """
    :param region: a string representing a region
    :param race: a string representing a race of the person
    """
    res = requests.get("https://uinames.com/api", params={"region": region})
    res = res.json()


def random_region(list: list):
    region = random.choice(list)
    return region


def random_race(race: dict):
    race = random.choice(race.values())
    return race


def robohash_url_generator(name: str, race: str):
    ROBOHASH_URL =  f"https://robohash.org/{name}.png?set={race}"
    return ROBOHASH_URL


def save_json_file(string_of_users: str):
    pass


if __name__ == "__main__":
    main()
