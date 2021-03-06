"""empty message

Revision ID: 74c773338d30
Revises: 032a6eb485f8
Create Date: 2019-05-17 11:24:27.056138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74c773338d30'
down_revision = '032a6eb485f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Country', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=2),
               existing_server_default=sa.text('nextval(\'"Country_id_seq"\'::regclass)'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Country', 'id',
               existing_type=sa.String(length=2),
               type_=sa.INTEGER(),
               existing_server_default=sa.text('nextval(\'"Country_id_seq"\'::regclass)'))
    # ### end Alembic commands ###
