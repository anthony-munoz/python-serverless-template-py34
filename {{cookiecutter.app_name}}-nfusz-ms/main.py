
from app.flask_factory import app
from app.router import configure_api

configure_api(app)


if __name__ == '__main__':
    app.run(debug=True)
