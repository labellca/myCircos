from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(), index=True, unique=True)
  password = db.Column(db.String(12), index=True, unique=False)

  #return True unless user is not allowed to authenticate
  def is_authenticated(self):
    return True

  #return True unless user is inactive
  def is_active(self):
    return True

  #return True only for fake users(not supposed to log in system)
  def is_anonymous(self):
    return False

  #returnunique identifier for the user: unicode format
  #using unique id generated by database
  def get_id(self):
    try:
      return unicode(self.id)		#mostly for python 2
    except NameError:
      return str(self.id)		#mostly for python 3

  #debugging
  def __repr__(self):
    return '%s' % (self.email)

class Circos(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  svg = db.Column(db.String(), unique=True)
  user_id = db.Column(db.String(), unique=False) 
  
  #debugging
  def __repr__(self):
    return self.svg
    
