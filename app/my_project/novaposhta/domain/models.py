from sqlalchemy import Column, Integer, String, ForeignKey, Table, DECIMAL, Text
from sqlalchemy.orm import relationship
from app.utils.db import Base

package_service = Table('package_service', Base.metadata,
    Column('package_id', Integer, ForeignKey('package.id'), primary_key=True),
    Column('extra_service_id', Integer, ForeignKey('extra_service.id'), primary_key=True)
)

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    branches = relationship('Branch', backref='city_ref')

    def put_into_dto(self):
        return {'id': self.id, 'name': self.name}

class Branch(Base):
    __tablename__ = 'branch'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(250), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'))

    def put_into_dto(self):
        return {'id': self.id, 'address': self.address, 'city_id': self.city_id}
    
class Package(Base):
    __tablename__ = 'package'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tracking_number = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
    weight = Column(DECIMAL(5,2), nullable=False)
    sender_id = Column(Integer, nullable=False)
    receiver_id = Column(Integer, nullable=False)
    sender_branch_id = Column(Integer, nullable=False)
    delivery_type_id = Column(Integer, nullable=False)
    
    services = relationship('ExtraService', secondary=package_service, backref='packages')

class ExtraService(Base):
    __tablename__ = 'extra_service'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    def put_into_dto(self):
        return {
            'id': self.id, 
            'name': self.name
        }

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(150), nullable=False, unique=True)
    phone = Column(String(20))

    def put_into_dto(self):
        return {'id': self.id, 'full_name': self.full_name, 'phone': self.phone}

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(150), nullable=False)
    position = Column(String(50), nullable=False)
    branch_id = Column(Integer, nullable=False)