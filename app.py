from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from werkzeug.utils import secure_filename
from flask_session import Session
import os

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.secret_key = 'password21354'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 60 * 60 * 24 * 7

Session(app)

@app.before_request
def make_session_permanent():
    session.permanent = True

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    games = session.get('games', [])
    return render_template('index.html', games=games)

@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    error = None

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        platform = request.form.get('platform', '').strip()
        release_year_raw = request.form.get('release_year', '').strip()
        file = request.files.get('game_file')
        filename = None

        current_year = datetime.now().year

        if not name or not platform:
            error = "Name and platform are required."
        elif not release_year_raw.isdigit():
            error = "Release year must be a number."
        else:
            release_year = int(release_year_raw)
            if release_year < 1950 or release_year > current_year:
                error = f"Release year must be between 1950 and {current_year}."

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        if error:
            return render_template('add_game.html', error=error)

        game = {
            'name': name,
            'platform': platform,
            'release_year': release_year,
            'filename': filename
        }

        games = session.get('games', [])
        games.append(game)
        session['games'] = games

        return redirect(url_for('home'))

    return render_template('add_game.html', error=error)

@app.route('/clear')
def clear():
    session.pop('games', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)