from src.app.pysys_app import db


class Person(db.Model):
    """ This is the ORM Person class """

    __tablename__ = "persons"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    group = db.Column(db.Integer, nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)

    person_client_fk = db.relationship("Person", backref='client')
    person_vendor_fk = db.relationship("Person", backref='vendor')
    person_user_fk = db.relationship("Person", backref='user')
    person_zip_code_fk = db.relationship("Person", backref='zip_code')

    def __repr__(self):
        """ The representation method of class """
        return '<Person %r>' % self.name


class Client(db.Model):
    """ This is the ORM Client class """

    __tablename__ = "clients"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(14), nullable=False, unique=True)
    birth_date = db.Column(db.DateTime, nullable=False)
    person_id = db.Column(db.BigInteger, db.ForeignKey("persons.id"), nullable=True)

    def __repr__(self):
        """ The representation method of class """
        return '<Client %r>' % self.cpf


class Vendor(db.Model):
    """ This is the ORM Vendor class """

    __tablename__ = "vendors"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.String(18), nullable=False, unique=True)
    legal_date = db.Column(db.DateTime, nullable=False)
    person_id = db.Column(db.BigInteger, db.ForeignKey("persons.id"), nullable=True)

    def __repr__(self):
        """ The representation method of class """

        return '<Vendor %r>' % self.cnpj


class User(db.Model):
    """ This is the ORM User class """

    __tablename__ = "users"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(10), nullable=False)
    token = db.Column(db.Text, nullable=False)
    last_login = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Integer, nullable=False)

    person_id = db.Column(db.BigInteger, db.ForeignKey("persons.id"), nullable=True)

    def __repr__(self):
        """ The representation method of class """
        return '<User %r>' % (self.id + ' - ' + self.email)


class ZipCode(db.Model):
    """ This is the ORM Address class """

    __tablename__ = "zip_codes"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    zip = db.Column(db.String(9), nullable=False)
    person_id = db.Column(db.BigInteger, db.ForeignKey("persons.id"), nullable=True)

    zip_code_address_fk = db.relationship('Address', backref='address')

    def __repr__(self):
        """ The representation method of class """
        return '<ZipCode %r>' % self.zip


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
    ibge_code = db.Column(db.String(7), nullable=False)
    zip_code_id = db.Column(db.BigInteger, db.ForeignKey("zip_codes.id"), nullable=True)

    def __repr__(self):
        """ The representation method of class """
        return '<Address %r>' % (self.id + ' - ' + self.zip_code_id)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
