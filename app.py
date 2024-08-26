from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/transform", methods=["POST"])
def transform():
    rd = request.data
    from xyz_util.mediautils import Transformer
    tf = Transformer()
    func = getattr(tf, rd.pop('function'))
    rs = func(*rd.get('args', []), **rd.get('kwargs', {}))
    return jsonify({"result": rs})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
