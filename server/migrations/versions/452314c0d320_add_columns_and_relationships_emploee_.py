"""add columns and relationships, emploee, client, medtimes, meds

Revision ID: 452314c0d320
Revises: 495671bae250
Create Date: 2023-09-25 10:42:19.319817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '452314c0d320'
down_revision = '495671bae250'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('username', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('_password_hash', sa.String(), nullable=False))
        batch_op.create_unique_constraint(None, ['username'])

    with op.batch_alter_table('med_times', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time_slot', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('amount', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('signed_off', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('client_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('medication_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_med_times_signed_off_employees'), 'employees', ['signed_off'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_med_times_medication_id_medications'), 'medications', ['medication_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_med_times_client_id_clients'), 'clients', ['client_id'], ['id'])

    with op.batch_alter_table('medications', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('medication_use', sa.String(), nullable=False))
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('medications', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('medication_use')
        batch_op.drop_column('name')

    with op.batch_alter_table('med_times', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_med_times_client_id_clients'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_med_times_medication_id_medications'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_med_times_signed_off_employees'), type_='foreignkey')
        batch_op.drop_column('medication_id')
        batch_op.drop_column('client_id')
        batch_op.drop_column('signed_off')
        batch_op.drop_column('amount')
        batch_op.drop_column('time_slot')

    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('_password_hash')
        batch_op.drop_column('username')
        batch_op.drop_column('name')

    # ### end Alembic commands ###