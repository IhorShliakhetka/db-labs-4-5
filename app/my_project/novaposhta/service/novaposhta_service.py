from app.my_project.novaposhta.dao.novaposhta_dao import NovaPoshtaDAO
from app.my_project.novaposhta.domain.models import City, Client

class NovaPoshtaService:
    def __init__(self):
        self.dao = NovaPoshtaDAO()

    def get_all_cities(self): return self.dao.get_all_cities()
    def get_city(self, city_id): return self.dao.get_city_by_id(city_id)
    def create_city(self, data): return self.dao.create_city(City(name=data['name']))
    def update_city(self, city_id, data): return self.dao.update_city(city_id, data['name'])
    def delete_city(self, city_id): return self.dao.delete_city(city_id)
    
    def get_city_branches(self, city_id): return self.dao.get_branches_by_city(city_id)
    def get_package_services(self, pkg_id): return self.dao.get_services_for_package(pkg_id)

    def get_all_clients(self): return self.dao.get_all_clients()
    def get_client(self, client_id): return self.dao.get_client_by_id(client_id)
    def create_client(self, data): return self.dao.create_client(Client(full_name=data['full_name'], phone=data.get('phone')))
    def update_client(self, client_id, data): return self.dao.update_client(client_id, data['full_name'], data.get('phone'))
    def delete_client(self, client_id): return self.dao.delete_client(client_id)

    def create_city_via_procedure(self, data):
        self.dao.create_city_via_procedure(data['name'])
        return {"message": "Місто успішно додано через SQL-процедуру!"}

    def create_package(self, data):
        from app.my_project.novaposhta.domain.models import Package
        new_package = Package(
            tracking_number=data.get('tracking_number'),
            description=data.get('description'),
            weight=data.get('weight'),
            sender_id=data.get('sender_id'),
            receiver_id=data.get('receiver_id'),
            sender_branch_id=data.get('sender_branch_id'),
            delivery_type_id=data.get('delivery_type_id')
        )
        return self.dao.create_package(new_package)

    def create_employee(self, data):
        from app.my_project.novaposhta.domain.models import Employee
        new_emp = Employee(
        full_name=data.get('full_name'),
        position=data.get('position'),
        branch_id=data.get('branch_id')
        )
        return self.dao.create_employee(new_emp)

    def delete_branch(self, branch_id):
        self.dao.delete_branch(branch_id)