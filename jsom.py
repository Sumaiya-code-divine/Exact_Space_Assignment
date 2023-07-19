from flask import Flask, render_template, request

jsom = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        json_data = request.form['json_data']
        return json_data

    return render_template('index.html')

if __name__ == '__main__':
    jsom.run()

