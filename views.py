import psycopg2

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')
