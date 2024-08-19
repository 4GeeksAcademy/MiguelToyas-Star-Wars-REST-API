"""empty message

Revision ID: ec177c8dfc23
Revises: a5cffa318ac2
Create Date: 2024-08-19 18:36:39.710921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec177c8dfc23'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('People',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('url', sa.String(length=450), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_table('Person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('birth_year', sa.String(length=150), nullable=False),
    sa.Column('eye_color', sa.String(length=150), nullable=False),
    sa.Column('films', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('gender', sa.String(length=150), nullable=False),
    sa.Column('hair_color', sa.String(length=150), nullable=False),
    sa.Column('height', sa.String(length=150), nullable=False),
    sa.Column('homeworld', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('mass', sa.String(length=150), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('skin_color', sa.String(length=150), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('edited_at', sa.DateTime(), nullable=False),
    sa.Column('species', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('starships', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('url', sa.String(length=150), nullable=False),
    sa.Column('vehicles', sa.ARRAY(sa.String()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=150), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('edited_at', sa.DateTime(), nullable=False),
    sa.Column('diameter', sa.String(length=150), nullable=False),
    sa.Column('films', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('gravitiy', sa.String(length=150), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('orbital_period', sa.String(length=150), nullable=False),
    sa.Column('population', sa.String(length=150), nullable=False),
    sa.Column('residents', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('rotation_period', sa.String(length=150), nullable=False),
    sa.Column('surface_water', sa.String(length=150), nullable=False),
    sa.Column('terrain', sa.String(length=150), nullable=False),
    sa.Column('url', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('url', sa.String(length=450), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Planets')
    op.drop_table('Planet')
    op.drop_table('Person')
    op.drop_table('People')
    # ### end Alembic commands ###
