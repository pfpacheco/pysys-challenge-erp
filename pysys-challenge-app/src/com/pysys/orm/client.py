from com.pysys.db.app import db
from com.pysys.orm.person import Person


class Client(db.Model):
    """ This is the ORM Client class """

    __tablename__ = "clients"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(14), nullable=False, unique=True)
    birth_date = db.Column(db.DateTime, nullable=False)

    person_fk = db.Column(db.BigInteger, db.ForeignKey("persons.id"), nullable=True)
    person = db.relationship(Person)

    def __repr__(self):
        """ The representation method of class """
        return '<Client %r>' % self.cpf


if __name__ == '__main__':
    db.create_all()
