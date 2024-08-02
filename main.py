from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def main_page():
    return render_template('index.html')
    

@app.route('/<user>_<refer>')
def ref_page(refer, user):
    return render_template('index.html', refer=refer, user=user)
    

if __name__ == '__main__':
    app.run(port=8000)