"""removed start stop and end stop

Revision ID: 88e13c77de77
Revises: e621476d4cf6
Create Date: 2024-09-27 17:57:17.735231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88e13c77de77'
down_revision = 'e621476d4cf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('routes', schema=None) as batch_op:
        batch_op.drop_constraint('fk_routes_end_stop_id_stations', type_='foreignkey')
        batch_op.drop_constraint('fk_routes_start_stop_id_stations', type_='foreignkey')
        batch_op.drop_column('start_stop_id')
        batch_op.drop_column('end_stop_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('routes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('end_stop_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('start_stop_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_routes_start_stop_id_stations', 'stations', ['start_stop_id'], ['id'])
        batch_op.create_foreign_key('fk_routes_end_stop_id_stations', 'stations', ['end_stop_id'], ['id'])

    # ### end Alembic commands ###
