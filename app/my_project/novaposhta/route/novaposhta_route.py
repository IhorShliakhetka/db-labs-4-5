from flask import Blueprint
from app.my_project.novaposhta.controller.novaposhta_controller import NovaPoshtaController

np_bp = Blueprint('np_bp', __name__)

np_bp.route('/cities', methods=['GET'])(NovaPoshtaController.get_cities)
np_bp.route('/cities', methods=['POST'])(NovaPoshtaController.create_city)
np_bp.route('/cities/<int:city_id>', methods=['PUT'])(NovaPoshtaController.update_city)
np_bp.route('/cities/<int:city_id>', methods=['DELETE'])(NovaPoshtaController.delete_city)

np_bp.route('/cities/<int:city_id>/branches', methods=['GET'])(NovaPoshtaController.get_branches_m1)
np_bp.route('/packages/<int:package_id>/services', methods=['GET'])(NovaPoshtaController.get_services_mm)
np_bp.route('/cities/procedure', methods=['POST'])(NovaPoshtaController.create_city_procedure)

np_bp.route('/clients', methods=['GET'])(NovaPoshtaController.get_clients)
np_bp.route('/clients', methods=['POST'])(NovaPoshtaController.create_client)
np_bp.route('/clients/<int:client_id>', methods=['PUT'])(NovaPoshtaController.update_client)
np_bp.route('/clients/<int:client_id>', methods=['DELETE'])(NovaPoshtaController.delete_client)
np_bp.route('/packages', methods=['POST'])(NovaPoshtaController.create_package)
np_bp.route('/employees', methods=['POST'])(NovaPoshtaController.create_employee)
np_bp.route('/branches/<int:branch_id>', methods=['DELETE'])(NovaPoshtaController.delete_branch)