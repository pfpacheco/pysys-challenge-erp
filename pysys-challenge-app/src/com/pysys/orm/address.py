from com.pysys.db.app import db
from com.pysys.orm.zip import Zip


class Address(db.Model):
    """ This is the ORM Address class """

    __tablename__ = "addresses"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    public_place = db.Column(db.Text, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    complement = db.Column(db.String(50), nullable=False)
    neighbor = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    uf = db.Column(db.String(2), nullable=False)

    zip_fk = db.Column(db.BigInteger, db.ForeignKey("zip.id"), nullable=True)
    zip = db.relationship(Zip)



    def __repr__(self):
        """ The representation method of class """
        return '<Address %r>' % (self.id + ' - ' + self.zip_fk)


if __name__ == '__main__':
    db.create_all()
