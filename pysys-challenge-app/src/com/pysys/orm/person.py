from com.pysys.db.app import db


class Person(db.Model):
    """ This is the ORM Person class """

    __tablename__ = "persons"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        """ The representation method of class """
        return '<Person %r>' % self.name


if __name__ == '__main__':
    db.create_all()
