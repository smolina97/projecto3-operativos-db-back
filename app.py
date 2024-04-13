from flask import Flask
from flask_cors import CORS
from routes.home import home_bp

app = Flask(__name__)
CORS(app)  # Esto permite solicitudes desde cualquier origen


app.register_blueprint(home_bp)


if __name__ == '__main__':
    app.run(debug=True)
