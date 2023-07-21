import db.model as models
from sqlalchemy.orm import Session


def get_users(db: Session):
    return db.query(models.Users).all()


def get_post(db: Session, user_id, post_id):
    return db.query(models.Post).filter_by(user_id=user_id, id=post_id).first()
