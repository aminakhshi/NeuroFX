import os
import sys
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, session, render_template_string)
import plotly.express as px
import plotly.io as pio
import subprocess

app = Flask(__name__)
app.secret_key = "some_secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    python_path = sys.executable
    # Run the game script externally
    result = subprocess.run(
        [python_path, os.path.join(app.root_path, 'game_stimuli.py')],
        capture_output=True, text=True
    )

    # Print the output for debugging
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    # Fetch the results (assuming they are stored in a file)
    with open("game_results.txt", "r") as f:
        results = eval(f.read())  # Using eval with caution

    session['results'] = results
    return redirect(url_for('show_results'))

@app.route('/show_results')
def show_results():
    results = session.get('results', {})

    # Generate plots
    fig1 = px.bar(x=['Correct', 'Wrong'], y=[results.get('correct_clicks', 0), results.get('incorrect_clicks', 0)], title="Correct vs Wrong Answers")
    fig2 = px.histogram(results.get('correct_latencies', []), nbins=20, title="Latency Times for Correct Answers")
    fig3 = px.histogram(results.get('incorrect_latencies', []), nbins=20, title="Latency Times for Incorrect Answers")

    bar_html = pio.to_html(fig1, full_html=False)
    correct_hist_html = pio.to_html(fig2, full_html=False)
    incorrect_hist_html = pio.to_html(fig3, full_html=False)

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Game Analysis Results</title>
    </head>
    <body>
        <div>{{ bar_html|safe }}</div>
        <div>{{ correct_hist_html|safe }}</div>
        <div>{{ incorrect_hist_html|safe }}</div>
    </body>
    </html>
    """, bar_html=bar_html, correct_hist_html=correct_hist_html, incorrect_hist_html=incorrect_hist_html)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


