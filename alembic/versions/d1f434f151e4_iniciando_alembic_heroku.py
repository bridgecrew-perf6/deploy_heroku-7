"""Iniciando alembic heroku

Revision ID: d1f434f151e4
Revises: 
Create Date: 2022-02-02 23:05:20.574949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1f434f151e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('picture', sa.String(length=800), nullable=True),
    sa.Column('stars', sa.Integer(), nullable=True),
    sa.Column('cellphone', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('activate', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cellphone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
