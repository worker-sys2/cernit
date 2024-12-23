from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ceoforum')
def ceoforum():
    return render_template('ceo.html')

@app.route('/ceoform')
def ceofrum():
    return render_template('form.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
