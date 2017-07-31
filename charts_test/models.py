from charts_test import db


class Regions(db.Model):
    """Regions model."""

    __tablename__ = "regions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Cities(db.Model):
    """Cities model."""

    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.Integer, db.ForeignKey("regions.id"))
    name = db.Column(db.String)



class Values(db.Model):
    """Values model."""

    __tablename__ = "values"

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    city = db.Column(db.Integer, db.ForeignKey("cities.id"))


