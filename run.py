from src.main.server.server import app #os inits facilitam pra importação ocorrer desse jeito

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
