from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__, static_folder='static')

games = []

@app.route('/')
def home():
    return render_template('index.html', games=games)

@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    error = None

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        platform = request.form.get('platform', '').strip()
        release_year_raw = request.form.get('release_year', '').strip()

        current_year = datetime.now().year

        if not name or not platform:
            error = "Name and platform are required."
        elif not release_year_raw.isdigit():
            error = "Release year must be a number."
        else:
            release_year = int(release_year_raw)
            if release_year < 1950 or release_year > current_year:
                error = f"Release year must be between 1950 and {current_year}."

        if error:
            return render_template('add_game.html', error=error)

        games.append({
            'name': name,
            'platform': platform,
            'release_year': release_year
        })
        return redirect(url_for('home'))

    return render_template('add_game.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)