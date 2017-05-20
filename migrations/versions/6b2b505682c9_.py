"""empty message

Revision ID: 6b2b505682c9
Revises: 8d0606357a80
Create Date: 2017-05-20 19:25:24.287704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b2b505682c9'
down_revision = '8d0606357a80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meta_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('artist_familiarity', sa.Float(), nullable=False),
    sa.Column('artist_hotttnesss', sa.Float(), nullable=False),
    sa.Column('artist_latitude', sa.Float(), nullable=False),
    sa.Column('artist_longitude', sa.Float(), nullable=False),
    sa.Column('duration', sa.Float(), nullable=False),
    sa.Column('end_of_fade_in', sa.Float(), nullable=False),
    sa.Column('key', sa.Integer(), nullable=False),
    sa.Column('key_confidence', sa.Float(), nullable=False),
    sa.Column('loudness', sa.Float(), nullable=False),
    sa.Column('mode', sa.Integer(), nullable=False),
    sa.Column('mode_confidence', sa.Float(), nullable=False),
    sa.Column('song_hotttnesss', sa.Float(), nullable=False),
    sa.Column('start_of_fade_out', sa.Float(), nullable=False),
    sa.Column('tempo', sa.Float(), nullable=False),
    sa.Column('time_signature', sa.Integer(), nullable=False),
    sa.Column('time_signature_confidence', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['track_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_meta_data_track_id'), 'meta_data', ['track_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_meta_data_track_id'), table_name='meta_data')
    op.drop_table('meta_data')
    # ### end Alembic commands ###