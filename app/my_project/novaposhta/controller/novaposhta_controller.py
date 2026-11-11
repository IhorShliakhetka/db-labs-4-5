from flask import jsonify, request
from app.my_project.novaposhta.service.novaposhta_service import NovaPoshtaService

service = NovaPoshtaService()

class NovaPoshtaController:
    @staticmethod
    def get_cities():
        return jsonify([c.put_into_dto() for c in service.get_all_cities()]), 200

    @staticmethod
    def create_city():
        city = service.create_city(request.get_json())
        return jsonify(city.put_into_dto()), 201

    @staticmethod
    def update_city(city_id):
        city = service.update_city(city_id, request.get_json())
        return jsonify(city.put_into_dto()) if city else ("Not found", 404)

    @staticmethod
    def delete_city(city_id):
        success = service.delete_city(city_id)
        return ("", 204) if success else ("Not found", 404)

    @staticmethod
    def get_branches_m1(city_id):
        branches = service.get_city_branches(city_id)
        return jsonify([b.put_into_dto() for b in branches]), 200

    @staticmethod
    def get_services_mm(package_id):
        services = service.get_package_services(package_id)
        return jsonify([s.put_into_dto() for s in services]), 200

    @staticmethod
    def create_city_procedure():
        data = request.get_json()
        result = service.create_city_via_procedure(data)
        return jsonify(result), 201

    @staticmethod
    def get_clients():
        return jsonify([c.put_into_dto() for c in service.get_all_clients()]), 200

    @staticmethod
    def create_client():
        client = service.create_client(request.get_json())
        return jsonify(client.put_into_dto()), 201

    @staticmethod
    def update_client(client_id):
        client = service.update_client(client_id, request.get_json())
        return jsonify(client.put_into_dto()) if client else ("Not found", 404)

    @staticmethod
    def delete_client(client_id):
        success = service.delete_client(client_id)
        return ("", 204) if success else ("Not found", 404)

    @staticmethod
    def create_package():
        service.create_package(request.get_json())
        return jsonify({"message": "Package created"}), 201

    @staticmethod
    def create_employee():
        service.create_employee(request.get_json())
        return jsonify({"message": "Employee created"}), 201

    @staticmethod
    def delete_branch(branch_id):
        service.delete_branch(branch_id)
        return "", 204