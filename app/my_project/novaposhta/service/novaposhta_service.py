from app.my_project.novaposhta.dao.novaposhta_dao import NovaPoshtaDAO
from app.my_project.novaposhta.domain.models import City

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