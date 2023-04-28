"""task.stage

Revision ID: a65162fe063c
Revises: 4b1ef3ff19cd
Create Date: 2023-04-18 11:10:11.214390

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a65162fe063c'
down_revision = '4b1ef3ff19cd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('stage', sa.Enum(name='stage'), nullable=True))
    op.add_column('tasks', sa.Column('stage', sa.Enum('Dev', 'Qa', 'Review', 'Release', 'Done', name='stage'), nullable=True))
    op.alter_column('tasks', 'board',
               existing_type=postgresql.ENUM('Actual', 'Complete', 'Plans', 'Release', name='board'),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'board',
               existing_type=postgresql.ENUM('Actual', 'Complete', 'Plans', 'Release', name='board'),
               nullable=True)
    op.drop_column('tasks', 'stage')
    op.drop_column('history', 'stage')
    # ### end Alembic commands ###
