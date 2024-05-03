from flaskblog import create_app, db

app = create_app()

def create_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_db()
