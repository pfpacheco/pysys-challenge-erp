from com.pysys.db.app import db


class Uf(db.Model):
    """ This is the ORM IBGE UF class """

    __tablename__ = "uf"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    uf = db.Column(db.Text, length=2, nullable=False)
    uf_code = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        """ The representation method of class """
        return '<UF %r>' % (self.id + ' - ' + self.uf)


if __name__ == '__main__':
    db.create_all()
