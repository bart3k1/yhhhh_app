"""create account table

Revision ID: cac36734ecc0
Revises: ce560ec81e07
Create Date: 2021-07-14 12:51:00.360025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cac36734ecc0'
down_revision = 'ce560ec81e07'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('text', sa.String(50), nullable=False),
        sa.Column('status', sa.Unicode(200)),
        sa.Column('checkedX', sa.Unicode(200)),
    )


def downgrade():
    pass