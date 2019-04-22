#!rate_system/bin/python

from app import app
# from app.auth import app

if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)
