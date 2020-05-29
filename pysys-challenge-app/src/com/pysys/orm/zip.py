from com.pysys.db.app import db
from com.pysys.orm.person import Person


class Zip(db.Model):
    """ This is the ORM Address class """

    __tablename__ = "zip"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    zip = db.Column(db.String(9), nullable=False)

    person_fk = db.Column(db.BigInteger, db.ForeignKey("persons.id"), nullable=True)
    person = db.relationship(Person)

    def __repr__(self):
        """ The representation method of class """
        return '<Zip %r>' % self.zip


if __name__ == '__main__':
    db.create_all()
