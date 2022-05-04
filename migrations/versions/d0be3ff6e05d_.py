"""empty message

Revision ID: d0be3ff6e05d
Revises: 074f27c81842
Create Date: 2022-02-28 14:34:59.986067

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd0be3ff6e05d'
down_revision = '074f27c81842'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'environmentconfig',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('day_h_sp', sa.Float(), nullable=False),
        sa.Column('day_l_sp', sa.Float(), nullable=False),
        sa.Column('night_h_sp', sa.Float(), nullable=False),
        sa.Column('night_l_sp', sa.Float(), nullable=False),
        sa.Column('lights_on_time', sa.Time(), nullable=False),
        sa.Column('lights_off_time', sa.Time(), nullable=False),
        sa.Column('humidity_h_sp', sa.Float(), nullable=False),
        sa.Column('humidity_l_sp', sa.Float(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=False),

        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table('environmentconfig')