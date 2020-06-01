from com.pysys.db.app import db


class Uf(db.Model):
    """ This is the ORM IBGE Jurisdiction class """

    __tablename__ = "uf"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    city = db.Column(db.Text, nullable=False)
    city_code = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        """ The representation method of class """
        return '<City %r>' % (self.id + ' - ' + self.city)


if __name__ == '__main__':
    db.create_all()
