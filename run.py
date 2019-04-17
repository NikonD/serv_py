#!rate_system/Scripts/python.exe

from app import app
# from app.auth import app

if __name__ == "__main__":
    app.run(host='0.0.0.0')