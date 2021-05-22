from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True



@app.route('/')
def get_index():
    return 'hi'







if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)