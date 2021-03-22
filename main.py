from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('page.html', title=title)


@app.route('/table/<gender>/<age>')
def colour(gender, age):
    return render_template('colour.html', gender=gender, age=int(age))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
