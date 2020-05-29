from com.pysys.db.app import db
from com.pysys.orm.person import Person


class Vendor(db.Model):
    """ This is the ORM Vendor class """

    __tablename__ = "vendors"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.String(18), nullable=False, unique=True)
    legal_date = db.Column(db.DateTime, nullable=False)

    person_fk = db.Column(db.BigInteger, db.ForeignKey("persons.id"), nullable=True)
    person = db.relationship(Person)

    def __repr__(self):
        """ The representation method of class """

        return '<Vendor %r>' % self.cnpj


if __name__ == '__main__':
    db.create_all()
