from config.index import db

####TAB WEBSITES
class Websites(db.Model):
    __tablename__ = 'websites'
    id_website = db.Column(db.Integer, primary_key = True)
    name_website = db.Column(db.String(150), nullable=False)

    informations = db.relationship('informations', backref ='websites')

    def __repr__(self):
        return '<Albums %r>' % self.name_website




####TAB INFORMATIONS
class Informations(db.Model):
    __tablename__ = 'informations'
    id_info = db.Column(db.Integer, primary_key = True)
    name_info = db.Column(db.String(250), nullable=False)
    prix_info = db.Column(db.Integer, nullable=False)
    poids_info = db.Column(db.Float(), nullable=False)
    image_info = db.Column(db.String(250), nullable=False)

    id_website_info = db.Column(db.Integer, db.ForeignKey('websites.id_website'))


    def __repr__(self):
        return '<Photos %r>' % self.name_info



def create_all_tables():
    db.create_all()