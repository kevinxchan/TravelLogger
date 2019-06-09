"""empty message

Revision ID: bedb27d8c294
Revises: dc408c463ac1
Create Date: 2019-05-17 11:05:21.408438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bedb27d8c294'
down_revision = 'dc408c463ac1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Country', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=2),
               existing_server_default=sa.text('nextval(\'"Country_id_seq"\'::regclass)'))
    op.alter_column('Country', 'name',
               existing_type=sa.VARCHAR(),
               type_=sa.String(length=64),
               existing_nullable=False)
    op.alter_column('Visit', 'country_id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=2))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Visit', 'country_id',
               existing_type=sa.String(length=2),
               type_=sa.INTEGER())
    op.alter_column('Country', 'name',
               existing_type=sa.String(length=64),
               type_=sa.VARCHAR(),
               existing_nullable=False)
    op.alter_column('Country', 'id',
               existing_type=sa.String(length=2),
               type_=sa.INTEGER(),
               existing_server_default=sa.text('nextval(\'"Country_id_seq"\'::regclass)'))
    # ### end Alembic commands ###