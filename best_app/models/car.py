# encoding: utf-8


from best_app.database import db
from best_app.models.user import User
from sqlalchemy import ForeignKeyConstraint



class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)     
    model = db.Column(db.String(), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)    

    
    __table_args__ = (        
        ForeignKeyConstraint([owner_id], [User.id], ondelete='NO ACTION'),        
    )

    

    def __init__(self, model, owner_id):
        self.model = model
        self.owner_id = owner_id      
    

    def to_dict(self):
        return {
            'model': self.model,
            'owner': self.owner_id            
        }
    


    def buy_car(self):
        record = Car.query.filter(Car.id == self.id).first()
        if not record:
            db.session.add(self)
            db.session.commit()
        
        return True



    def get_user_cars(user_id):
        records = Car.query.filter(Car.owner_id == user_id).all()
        return [record.to_dict() for record in records] 



    def __repr__(self):
        return f"<Car {self.model}>"