import json
from setings import PATCH_CANDIDATES_JSON
from flask import Flask

app = Flask(__name__)


def load_candidates():
    """
    Загружаем список кандидатов и информацию о них из файла
    :return:
    """
    with open(PATCH_CANDIDATES_JSON, encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates

@app.route('/')
def get_all():
    return 'Hello'


@app.route('/candidates/<x>')
def get_by_pk(pk: str):
    pass


@app.route('/skills/<x>')
def get_by_skill(skill_name: str):
    pass

app.run()