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
    user = generate_users_and_photo(region)
    print(user)


def generate_users_and_photo(region: str):
    """
    Generates users and avatars from two different APIs.

    :param region: a string representing a region
    :return: returns a list of dictionaries
    """

    res = requests.get("https://uinames.com/api", params={"region": region})
    res = res.json()

    full_name = res['name'] + " " + res['surname']
    print("Full name:", full_name)

    species = random_race(race)
    print("Species:", species)

    # get the url from the name and species
    url = robohash_url_generator(full_name, species)

    # now add the url to the dictionary
    res['avatar'] = url
    return res


def random_region(regions: list):
    """
    Picks a random item (a region) from a list.

    :param regions: a list
    :return: returns a string
    """

    region = random.choice(regions)
    return region


def random_race(race: dict):
    """
    Chooses a random value from a dictionary

    :param: race: a dictionary
    :return: returns a string (the value of the chosen key)
    """

    # race = random.choice(race.values()) NOT WORKING!!! I'm getting -> TypeError: 'dict_values' object is not subscriptable
    list_of_species = []
    for i in race.values():
        list_of_species.append(i)
    # print(list_of_species)
    return random.choice(list_of_species)


def robohash_url_generator(name: str, race: str):
    """
    Generates a URL from the given parameters. The URL represents an image.

    :param: name: the name of the person
    :param: race: the race of the person
    :return: a string/url representing an image
    """

    ROBOHASH_URL =  f"https://robohash.org/{name}.png?set={race}"
    return ROBOHASH_URL


def save_json_file(string_of_users: str):
    pass


if __name__ == "__main__":
    main()
