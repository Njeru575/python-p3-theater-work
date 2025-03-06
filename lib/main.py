from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Role, Audition, Base


engine = create_engine('sqlite:///:memory:') 
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


role = Role(character_name='Romeo')
session.add(role)
session.commit()


audition_1 = Audition(actor='Juliet', location='Moi Theatre', phone='0712238042', role_id=role.id)
audition_2 = Audition(actor='Hamlet', location='Kenyatta Theatre', phone='0798765432', role_id=role.id)
audition_3 = Audition(actor='Othello', location='Njeru Theatre', phone='0796536698', role_id=role.id)

session.add_all([audition_1, audition_2, audition_3])
session.commit()


audition_1.call_back()


role = session.query(Role).first()

print(f"Role: {role.character_name}")  
print(f"Actors: {role.actors()}")  
print(f"Locations: {role.locations()}")  
print(f"Lead: {role.lead()}")  
print(f"Understudy: {role.understudy()}")  

session.close()
