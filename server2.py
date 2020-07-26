from flask import Flask, request, jsonify
from flask_cors import CORS
import reservations
import pdf
import prices
import comments

api = Flask(__name__)
CORS(api)


@api.route('/')
def index():
    return


@api.route("/api/login", methods=['POST'])
def login():
    name = login.login(request.json)
    return jsonify({"name": name})


# RESERVATIONS ------------------------------------------


@api.route("/api/reservations/all", methods=['GET'])
def all_reservations():
    return jsonify(reservations.get_all())


@api.route("/api/reservations/allCal", methods=['GET'])
def all_cal_reservations():
    return jsonify(reservations.get_all())


@api.route("/api/reservations/add", methods=['POST'])
def add_reservation():
    reservations.add(request.json)
    return jsonify({"status": "success"})


@api.route("/api/reservations/edit", methods=['POST'])
def edit_reservation():
    reservations.edit(request.json)
    return jsonify({"status": "success"})


@api.route("/api/reservations/delete", methods=['POST'])
def delete_reservation():
    reservations.delete(request.json["id"])
    return jsonify({"status": "success"})


@api.route("/api/reservations/createForm", methods=['POST'])
def create_form():
    pdf.create_registration_form(request.json)
    return jsonify({"status": "success"})


@api.route("/api/reservations/createInvoice", methods=['POST'])
def create_invoice():
    pdf.create_invoice(request.json)
    return jsonify({"status": "success"})


# PRICES ------------------------------------------


@api.route("/api/prices/all", methods=['GET'])
def all_prices():
    ps = prices.get_all()
    return jsonify(ps)


@api.route("/api/prices/add", methods=['POST'])
def add_price():
    prices.add(request.json)
    return jsonify({"status": "success"})


@api.route("/api/prices/edit", methods=['POST'])
def edit_price():
    prices.edit(request.json)
    return jsonify({"status": "success"})


@api.route("/api/prices/delete", methods=['POST'])
def delete_price():
    prices.delete(request.json["id"])
    return jsonify({"status": "success"})


# COMMENTS ------------------------------------------


@api.route("/api/comments/all", methods=['GET'])
def all_comments():
    cs = comments.get_all()
    return jsonify(cs)


@api.route("/api/comments/add", methods=['POST'])
def add_comment():
    comments.add(request.json)
    return jsonify({"status": "success"})


@api.route("/api/comments/edit", methods=['POST'])
def edit_comment():
    comments.edit(request.json)
    return jsonify({"status": "success"})


@api.route("/api/comments/delete", methods=['POST'])
def delete_comment():
    comments.delete(request.json["id"])
    return jsonify({"status": "success"})


if __name__ == "__main__":
    api.run(port=56789)