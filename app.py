from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.errorhandler(404)
def internal_server_error(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html',e=e), 500

if __name__ == '__main__':
    app.run(port=9000) 