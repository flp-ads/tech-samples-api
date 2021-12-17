"""deleted table user_analyst to create one table named users, fix column name unit, remove unique constraint from name in types table

Revision ID: 28e5525b33e2
Revises: 
Create Date: 2021-12-08 10:18:41.217947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28e5525b33e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('analysis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('batch', sa.String(), nullable=False),
    sa.Column('made', sa.DateTime(), nullable=True),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('is_concluded', sa.Boolean(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('analyst_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['analyst_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('batch')
    )
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parameters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('unit', sa.String(), nullable=False),
    sa.Column('min', sa.String(), nullable=False),
    sa.Column('max', sa.String(), nullable=False),
    sa.Column('result', sa.String(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['type_id'], ['types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parameters')
    op.drop_table('types')
    op.drop_table('analysis')
    op.drop_table('classes')
    op.drop_table('users')
    # ### end Alembic commands ###
