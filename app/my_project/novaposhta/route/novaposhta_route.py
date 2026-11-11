from flask import Blueprint
from app.my_project.novaposhta.controller.novaposhta_controller import NovaPoshtaController

np_bp = Blueprint('np_bp', __name__)

np_bp.route('/cities', methods=['GET'])(NovaPoshtaController.get_cities)
np_bp.route('/cities', methods=['POST'])(NovaPoshtaController.create_city)
np_bp.route('/cities/<int:city_id>', methods=['PUT'])(NovaPoshtaController.update_city)
np_bp.route('/cities/<int:city_id>', methods=['DELETE'])(NovaPoshtaController.delete_city)

np_bp.route('/cities/<int:city_id>/branches', methods=['GET'])(NovaPoshtaController.get_branches_m1)
np_bp.route('/packages/<int:package_id>/services', methods=['GET'])(NovaPoshtaController.get_services_mm)