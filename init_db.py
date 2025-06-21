# init_db.py

from app import app, db
from models import User, Patient

def init_db():
    with app.app_context():
        # 1. Create all tables under the Flask app context
        db.create_all()

        # 2. Seed users only if none exist
        if not User.query.first():
            u1 = User(username='alice')
            u1.set_password('password1')
            u2 = User(username='bob')
            u2.set_password('password2')
            db.session.add_all([u1, u2])
            db.session.commit()
            print("✅ Database initialized with two users.")
        else:
            print("⚠️  Users already exist; skipping seeding.")

if __name__ == '__main__':
    init_db()
