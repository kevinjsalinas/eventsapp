from app import app
from models import db, Attendee

with app.app_context():

    print("Deleting data...")
    Attendee.query.delete()

    print("Creating Attendee...")
    a1 = Attendee(email = "mike@gmail.com", name="Michael Roman")

    a1.password_hash = "test"

    # attendees = a1

    db.session.add(a1)
    db.session.commit()

    print("Seeding done!")

