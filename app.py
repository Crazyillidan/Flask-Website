from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

games = []

@app.route('/')
def home():
    return render_template('index.html', games=games)

@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        name = request.form['name']
        platform = request.form['platform']
        release_year = request.form['release_year']

        games.append({
            'name': name,
            'platform': platform,
            'release_year': release_year
        })

        return redirect(url_for('home'))
    return render_template('add_game.html')

if __name__ == '__main__':
    app.run(debug=True)
