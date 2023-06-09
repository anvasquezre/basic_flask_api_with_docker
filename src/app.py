from flask import Flask
from views import router

app = Flask(__name__)
app.secret_key = "secret key"
app.register_blueprint(router)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
