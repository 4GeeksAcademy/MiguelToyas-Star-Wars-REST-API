"""empty message

Revision ID: 146e881cde5a
Revises: 4a83b5b1eac8
Create Date: 2024-08-21 14:08:36.731435

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '146e881cde5a'
down_revision = '4a83b5b1eac8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('birth_year', sa.String(length=150), nullable=False),
    sa.Column('eye_color', sa.String(length=150), nullable=False),
    sa.Column('films', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('gender', sa.String(length=150), nullable=False),
    sa.Column('hair_color', sa.String(length=150), nullable=False),
    sa.Column('height', sa.String(length=150), nullable=False),
    sa.Column('homeworld', sa.String(length=150), nullable=False),
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
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=150), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('edited_at', sa.DateTime(), nullable=False),
    sa.Column('diameter', sa.String(length=150), nullable=False),
    sa.Column('films', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('gravity', sa.String(length=150), nullable=False),
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
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('url', sa.String(length=450), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('url', sa.String(length=450), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
    op.drop_constraint('favorite_user_id_fkey', 'favorite', type_='foreignkey')
    op.drop_table('user')
    op.drop_table('favorite')
    op.drop_table('Planet')
    op.drop_table('Person')
    op.drop_table('People')
    op.drop_table('Planets')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Planets',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Planets_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(length=450), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Planets_pkey'),
    sa.UniqueConstraint('name', name='Planets_name_key'),
    sa.UniqueConstraint('url', name='Planets_url_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('People',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"People_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(length=450), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='People_pkey'),
    sa.UniqueConstraint('name', name='People_name_key'),
    sa.UniqueConstraint('url', name='People_url_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Person',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Person_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('birth_year', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('eye_color', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('films', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False),
    sa.Column('gender', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('hair_color', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('height', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('homeworld', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False),
    sa.Column('mass', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('skin_color', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('edited_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('species', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False),
    sa.Column('starships', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('vehicles', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Person_pkey')
    )
    op.create_table('Planet',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Planet_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('climate', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('edited_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('diameter', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('films', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False),
    sa.Column('gravitiy', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('orbital_period', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('population', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('residents', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=False),
    sa.Column('rotation_period', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('surface_water', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('terrain', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Planet_pkey')
    )
    op.create_table('favorite',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('planet_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('people_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['people_id'], ['People.id'], name='favorite_people_id_fkey'),
    sa.ForeignKeyConstraint(['planet_id'], ['Planets.id'], name='favorite_planet_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favorite_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='favorite_pkey')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('favorites')
    op.drop_table('planets')
    op.drop_table('people')
    op.drop_table('users')
    op.drop_table('planet')
    op.drop_table('person')
    # ### end Alembic commands ###
