from models import Dog

def create_table(base, engine):
    Dog.metadata.create_all(engine)

def save(session, dog):
    #add the dog object to session
    session.add(dog)
    #commit the transaction save dog to DB
    session.commit()

def get_all(session):
    # Query the database to retrieve all Dog records
    dogs = session.query(Dog).all()
    return(dogs)

def find_by_name(session, name):
    pass

def find_by_id(session, id):
    pass

def find_by_name_and_breed(session, name, breed):
    pass

def update_breed(session, dog, breed):
    pass