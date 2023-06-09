"""ADD task.completed

Revision ID: ca62e12f1c30
Revises: ea5258f0e5fd
Create Date: 2023-05-12 20:05:03.815102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca62e12f1c30'
down_revision = 'ea5258f0e5fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('completed', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'completed')
    # ### end Alembic commands ###
