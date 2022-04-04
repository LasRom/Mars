from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/countdown')
def countdown():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/training/<prof>')
def greeting(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('list_prof.html', list=list, sp=['Пилот',
                                                   'Строитель',
                                                   'Врач',
                                                   'Инженер',
                                                   'Штурман',
                                                   'Пилот дронов',
                                                   'Климатолог',
                                                   'Штурман'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
