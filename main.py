from flask import Flask, request, Response
from chess import Chess

app = Flask(__name__)


@app.route("/")
def root():
    return "Welcome to Chess!"


@app.route("/game", methods=['GET', 'PATCH', 'PUT'])
def game():
    if request.method == 'GET':
        return get_game()

    elif request.method == 'PUT':
        return reset_game()

    elif request.method == 'PATCH':
        return update_game()

    print(chess)


def get_game():
    return {'turn': chess.turn,
            'from': chess.orig,
            'to': chess.dest}


def reset_game() -> str:
    chess.turn = 0
    chess.dest = ""
    chess.orig = ""

    return {'turn': chess.turn,
            'from': chess.orig,
            'to': chess.dest}


def update_game() -> str:
    if request.args.get("turn") == chess.turn:
        return Response("Invalid move", status=400)

    chess.turn = request.args.get("turn")
    chess.orig = request.args.get("from")
    chess.dest = request.args.get("to")

    return {'turn': chess.turn,
            'from': chess.orig,
            'to': chess.dest}


if __name__ == "__main__":
    chess = Chess()
    app.run(debug=True)
