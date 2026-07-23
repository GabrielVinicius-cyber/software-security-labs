from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return jsonify({"message": "Lab-01-Flask rodando com sucesso!"})


@main_bp.route('/status')
def status():
    return jsonify({"status": "ok"})
