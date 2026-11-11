from app.my_project.novaposhta.domain.models import City, Branch, Package
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