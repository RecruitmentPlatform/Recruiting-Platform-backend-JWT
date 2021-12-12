import sqlite3

class User(object):

    tablename = "candidates"
    dbpath = "../../data/db2.sqlite"

    def __init__(self, email, hash, id=None, first=None, last=None, phone=None, description=None, location=None,\
                       headline=None, session=None, ethnicity_id=None, gender_id=None, pronoun_id=None):
        self.id = id
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone
        self.description = description
        self.location = location
        self.headline = headline
        self.hash = hash
        self.session = session
        self.ethnicity_id = ethnicity_id 
        self.gender_id = gender_id
        self.pronoun_id = pronoun_id

    def __str__(self):
        return "User(id='%s')" % self.id

    

    def insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""INSERT INTO {self.tablename}
                      (first, last, email, hash)
                      VALUES (?,?,?,?);"""
            data = (self.first, self.last, self.email, self.hash)
            cursor.execute(sql, data)

    @classmethod
    def get(cls, criteria, data):
        if criteria == "id":
            return cls.query(criteria, data)
        if criteria == "email":
            return cls.query(criteria, data)
            

    @classmethod
    def query(cls, criteria, data):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""SELECT *
                    FROM {cls.tablename}
                    WHERE {criteria} = ?"""
            cursor.execute(sql, (data,))
        user = cursor.fetchone()
        if user:
            return User(id=user[0], first=user[1], last=user[2], email=user[3], hash=user[8])
        return None