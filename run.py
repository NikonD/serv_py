#!rate_system/bin/python

from app import app
# from app.auth import app

if __name__ == "__main__":
    app.run(debug = True , host='127.0.0.1')