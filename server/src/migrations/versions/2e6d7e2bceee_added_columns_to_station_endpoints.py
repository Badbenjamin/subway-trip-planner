"""added columns to station_endpoints

Revision ID: 2e6d7e2bceee
Revises: 6939f18112af
Create Date: 2024-09-27 15:06:39.733035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e6d7e2bceee'
down_revision = '6939f18112af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('station_endpoints', schema=None) as batch_op:
        batch_op.add_column(sa.Column('route', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('station_name', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('station_endpoints', schema=None) as batch_op:
        batch_op.drop_column('station_name')
        batch_op.drop_column('route')

    # ### end Alembic commands ###
