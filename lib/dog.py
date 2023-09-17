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
    return dogs

def find_by_name(session, name):
    # Query the database to find all Dog instances with the given name
    dogs = session.query(Dog).filter(Dog.name == name).first()
     # Return the list of Dog instances
    return dogs


    #"AttributeError: 'list' object has no attribute 'name'," bc you're returning a list of names instead of returning Dog instances in your find_by_name function. To fix this, you should modify your query to retrieve the Dog instances by name instead of just the names. Plus, I needed to change .all() to .first()


def find_by_id(session, id):
    dogs = session.query(Dog).filter(Dog.id == id).first()
    return dogs

def find_by_name_and_breed(session, name, breed):
    dogs = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dogs


def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()

