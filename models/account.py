from datetime import datetime
from models.user import db, User
import random

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = db.relationship(User, backref=db.backref('account', uselist=False))
    transactions = db.relationship('Transaction', backref='account', lazy=True)

    def __init__(self, *args, **kwargs):
        if 'account_number' not in kwargs or not kwargs['account_number']:
            kwargs['account_number'] = self.generate_unique_account_number()
        super().__init__(*args, **kwargs)

    @staticmethod
    def generate_unique_account_number():
        while True:
            number = str(random.randint(10**9, 10**10-1))  # 10-digit number
            if not Account.query.filter_by(account_number=number).first():
                return number

class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)  # MTN, iShare, Telicel
    description = db.Column(db.Text)
    image_filename = db.Column(db.String(255))  # New field for image file name
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    items = db.relationship('PackageItem', backref='package', lazy=True)

class PackageItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PaymentType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)  # Wallet, Paystack
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    transactions = db.relationship('Transaction', backref='payment_type', lazy=True)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    payment_type_id = db.Column(db.Integer, db.ForeignKey('payment_type.id'), nullable=False)  # Required

    # Transaction details
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)  # 'credit' or 'debit'
    reference_number = db.Column(db.String(50), unique=True, nullable=False)
    balance_after = db.Column(db.Float, nullable=False)  # Balance left after transaction
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='Pending')  # pending, completed, failed
    transaction_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Transaction {self.reference_number}: {self.amount} {self.transaction_type}>' 

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'), nullable=False)
    package_item_id = db.Column(db.Integer, db.ForeignKey('package_item.id'), nullable=True)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, completed, failed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    topup_for = db.Column(db.String(100), nullable=True)  # New column for top-up recipient

    # Relationships
    account = db.relationship('Account', backref=db.backref('orders', lazy=True))
    package = db.relationship('Package', backref=db.backref('orders', lazy=True))
    package_item = db.relationship('PackageItem', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f'<Order {self.id}: Account {self.account_id}, Package {self.package_id}, Amount {self.amount}, Topup For {self.topup_for}>' 