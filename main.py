from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form  = """
<!DOCTYPE html>

<html>
    <head>
    <form method = 'post'>
        <label for = 'rotation'>Rotate by:</label>      
        <input type = 'text' name = 'rot' id = 'rotation' value = '0'></input>  
       
        <textarea name = 'text'>{0}</textarea>
        <input type = 'submit' value = "Submit Query" />

    </form action = '/', method = 'post'>
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
      <!-- create your form here -->
    </body>
</html>


"""
@app.route('/', methods = ['post'])
def encrypt():
    rotation = request.form['rot']
    rotation_to_int = int(rotation)
    text = request.form['text']
    rotated_string =  rotate_string(text,rotation_to_int)
    return form.format(rotated_string)

@app.route('/')
def index():
    return form.format("")

app.run()