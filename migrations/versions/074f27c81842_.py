"""empty message

Revision ID: 074f27c81842
Revises: 
Create Date: 2022-02-28 01:25:48.511700

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '074f27c81842'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "reading",
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('temperature', sa.Float(), nullable=False),
        sa.Column('humidity', sa.Float(), nullable=False),
        sa.Column('time', sa.DateTime(), nullable=False),

        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reading')
    # ### end Alembic commands ###