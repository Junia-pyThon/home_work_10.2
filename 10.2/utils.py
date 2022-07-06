import requests
import json
from setings import PATCH_CANDIDATES_JSON


def load_candidates():
    with open(PATCH_CANDIDATES_JSON, encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def get_all():
    pass


def get_by_pk(pk):
    pass


def get_by_skill(skill_name):
    pass

