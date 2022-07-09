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
    candidates = load_candidates()
    result = ''
    for candidate in candidates:
        result += f"""
               <pre>
               Имя кандидата: {candidate['name']}
               Позиция кандидата: {candidate['position']}
               Навыки кандидата: {candidate['skills'].lower()}
               </pre>
               \n\t
               """
    return result


@app.route('/candidates/<int:pk>')
def get_by_pk(pk: str, candidates=load_candidates()):
    for candidate in candidates:
        if candidate['pk'] == pk:
            return f"""
                    <pre>
                    <img src="({candidate['picture']})">
                    Имя кандидата: {candidate['name']}
                    Позиция кандидата: {candidate['position']}
                    Навыки кандидата: {candidate['skills'].lower()}
                    </pre>
                    """


@app.route('/skills/<skill>')
def get_by_skill(skill: str, candidates=load_candidates()):
    result = ''
    for candidate in candidates:
        if skill in candidate['skills']:
            result += f"""
                    <pre>
                    Имя кандидата: {candidate['name']}
                    Позиция кандидата: {candidate['position']}
                    Навыки кандидата: {candidate['skills'].lower()}
                    </pre>
                    \n\t
                    """
    return result


app.run()
