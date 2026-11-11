from sqlalchemy import text
from app.my_project.novaposhta.domain.models import City, Branch, Package, Client, Employee
from app.utils.db import session

class NovaPoshtaDAO:
    def get_all_cities(self):
        return session.query(City).all()

    def get_city_by_id(self, city_id):
        return session.query(City).filter(City.id == city_id).first()

    def create_city(self, city: City):
        session.add(city)
        session.commit()
        return city

    def update_city(self, city_id, new_name):
        city = self.get_city_by_id(city_id)
        if city:
            city.name = new_name
            session.commit()
        return city

    def delete_city(self, city_id):
        city = self.get_city_by_id(city_id)
        if city:
            session.delete(city)
            session.commit()
            return True
        return False

    def get_branches_by_city(self, city_id):
        return session.query(Branch).filter(Branch.city_id == city_id).all()

    def get_services_for_package(self, package_id):
        package = session.query(Package).filter(Package.id == package_id).first()
        return package.services if package else []

    def create_city_via_procedure(self, city_name):
        session.execute(text("CALL InsertCity(:name)"), {'name': city_name})
        session.commit()

    def get_all_clients(self):
        return session.query(Client).all()

    def get_client_by_id(self, client_id):
        return session.query(Client).filter(Client.id == client_id).first()

    def create_client(self, client: Client):
        session.add(client)
        session.commit()
        return client

    def update_client(self, client_id, new_name, new_phone):
        client = self.get_client_by_id(client_id)
        if client:
            client.full_name = new_name
            client.phone = new_phone
            session.commit()
        return client

    def delete_client(self, client_id):
        client = self.get_client_by_id(client_id)
        if client:
            session.delete(client)
            session.commit()
            return True
        return False

    def create_package(self, package: Package):
        session.add(package)
        session.commit()
        return package

    def create_employee(self, employee):
        session.add(employee)
        session.commit()
        return employee

    def delete_branch(self, branch_id):
        from app.my_project.novaposhta.domain.models import Branch
        branch = session.query(Branch).filter(Branch.id == branch_id).first()
        if branch:
            session.delete(branch)
            session.commit()