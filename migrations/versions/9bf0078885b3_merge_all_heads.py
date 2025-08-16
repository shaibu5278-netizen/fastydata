"""Merge all heads

Revision ID: 9bf0078885b3
Revises: 6264419d159f, 675dbcc09c4f, 8d364317e6a8, a8d1406562ee, drop_package_fields_from_transaction, fe55c261fe86
Create Date: 2025-07-19 13:18:29.893354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bf0078885b3'
down_revision = ('6264419d159f', '675dbcc09c4f', '8d364317e6a8', 'a8d1406562ee', 'drop_package_fields_from_transaction', 'fe55c261fe86')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
