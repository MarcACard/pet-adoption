"""Seed File to make sample data for db"""

from models import adopt, db
from app import app

db.drop_all()
db.create_all()

p1 = adopt(name="Mia", species="dog", age="3", notes="Ridgeback")
p2 = adopt(
    name="Spooky", species="dog", age="14", notes="Bichon Frise", availability=False
)
p3 = adopt(name="Bingo", species="dog", age="6", notes="Shih Tzu")
p4 = adopt(name="Charlie", species="dog", age="8", notes="Cocker Spaniel")

db.session.add_all([p1, p2, p3, p4])
db.session.commit()
