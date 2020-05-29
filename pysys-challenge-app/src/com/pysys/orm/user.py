from com.pysys.db.app import db
from com.pysys.orm.person import Person


class User(db.Model):
    """ This is the ORM User class """

    __tablename__ = "users"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(10), nullable=False)
    token = db.Column(db.Text, nullable=False)
    last_login = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    person_fk = db.Column(db.BigInteger, db.ForeignKey("persons.id"), nullable=True)
    person = db.relationship(Person)

    def __repr__(self):
        """ The representation method of class """
        return '<User %r>' % (self.id + ' - ' + self.email)


if __name__ == '__main__':
    db.create_all()
