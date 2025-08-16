from app import app
from models.user import db
from models.account import Package, PaymentType

def seed_packages():
    packages = [
        {'name': 'MTN', 'description': 'MTN Mobile Money and Data Services', 'is_active': True},
        {'name': 'iShare', 'description': 'iShare Data and Airtime Services', 'is_active': True},
        {'name': 'Telicel', 'description': 'Telicel Mobile Services', 'is_active': True},
    ]
    for package_data in packages:
        existing = Package.query.filter_by(name=package_data['name']).first()
        if not existing:
            db.session.add(Package(**package_data))
            print(f"Added package: {package_data['name']}")
        else:
            print(f"Package {package_data['name']} already exists")

def seed_payment_types():
    payment_types = [
        {'name': 'Wallet', 'description': 'Internal wallet payment system', 'is_active': True},
        {'name': 'Paystack', 'description': 'Paystack payment gateway', 'is_active': True},
    ]
    for payment_data in payment_types:
        existing = PaymentType.query.filter_by(name=payment_data['name']).first()
        if not existing:
            db.session.add(PaymentType(**payment_data))
            print(f"Added payment type: {payment_data['name']}")
        else:
            print(f"Payment type {payment_data['name']} already exists")

def seed_all():
    with app.app_context():
        print("Starting data seeding...")
        seed_packages()
        seed_payment_types()
        try:
            db.session.commit()
            print("\n✅ Data seeding completed successfully!")
        except Exception as e:
            db.session.rollback()
            print(f"\n❌ Error during seeding: {e}")

if __name__ == "__main__":
    seed_all() 