"""Drop package_id, package_item_id, and topup_for from transaction

Revision ID: drop_package_fields_from_transaction
Revises: <put_previous_revision_id_here>
Create Date: 2024-07-17 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'drop_package_fields_from_transaction'
down_revision = '4c0467c1c0ee'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        # Remove foreign key constraint if it exists
        try:
            batch_op.drop_constraint('fk_transaction_package_item_id', type_='foreignkey')
        except Exception:
            pass
        # Drop columns
        for col in ['package_id', 'package_item_id', 'topup_for']:
            try:
                batch_op.drop_column(col)
            except Exception:
                pass

def downgrade():
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.add_column(sa.Column('package_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('package_item_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('topup_for', sa.String(length=20), nullable=True))
        batch_op.create_foreign_key('fk_transaction_package_item_id', 'package_item', ['package_item_id'], ['id']) 