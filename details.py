from src.details.app import app

HOST = '0.0.0.0'
DEBUG = True
PORT = 8000

if __name__ == "__main__":  # Prevents duplicate execution issues
    app.run(host=HOST, debug=DEBUG, port=PORT)