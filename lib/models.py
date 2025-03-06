from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    character_name = Column(String)

    
    auditions = relationship("Audition", back_populates="role")

    def actors(self):
        
        return [audition.actor for audition in self.auditions]

    def locations(self):
        
        return [audition.location for audition in self.auditions]

    def lead(self):
        
        for audition in self.auditions:
            if audition.hired:
                return audition.actor
        return "No actor has been hired for this role"

    def understudy(self):
        
        hired_actors = [audition.actor for audition in self.auditions if audition.hired]
        if len(hired_actors) > 1:
            return hired_actors[1]
        return "No actor has been hired for understudy for this role"

class Audition(Base):
    __tablename__ = 'auditions'
    id = Column(Integer, primary_key=True)
    actor = Column(String)
    location = Column(String)
    phone = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    hired = Column(Boolean, default=False)  

    # Relationship with Role
    role = relationship("Role", back_populates="auditions")

    def call_back(self):
        
        self.hired = True
        session.commit()  




engine = create_engine('sqlite:///moringa_theater.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
