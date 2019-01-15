from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form action="/encrypt" method="POST">
                <label for="rot">Rotate by:
                    <input type="text" value=0 id="rot" name="rot">
                </label>
                <br>
                <br>
                <textarea name="text">{0}</textarea>
                <br>
                <br>
                <input type="submit" value="Submit Query">
            </form>
            </body>
    </html>

"""

@app.route("/")
def index():
    return form.format('')

@app.route("/encrypt", methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    user_text = request.form['text']

    result = rotate_string(user_text, rotate)

    return form.format(result)

app.run()