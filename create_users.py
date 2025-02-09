from app import app, db, User, bcrypt

# Buat konteks aplikasi
with app.app_context():
    # Create admin user
    admin = User(username='admin', password_hash=bcrypt.generate_password_hash('12345678').decode('utf-8'), role='admin')
    db.session.add(admin)

    # Create regular user
    regular_user = User(username='user', password_hash=bcrypt.generate_password_hash('12345678').decode('utf-8'), role='user')
    db.session.add(regular_user)

    # Commit changes to the database
    db.session.commit()

    print("Users created successfully!")
