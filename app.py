from flask import Flask, render_template
import data


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', data=data, tourslist=[4,5,3,2,7,9])

@app.route('/from/<direction>')
def fromdir(direction):
    return render_template('direction.html', data=data, direction=direction)

@app.route('/tours/<id>/')
def tours(id):
    return render_template('tour.html', data=data, id=int(id))


if __name__ == '__main__':
    app.run()