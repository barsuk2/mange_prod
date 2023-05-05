"""add column task.commitns

Revision ID: 84489f117599
Revises: 52c107105452
Create Date: 2023-05-04 12:47:01.997016

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '84489f117599'
down_revision = '52c107105452'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('comments', postgresql.ARRAY(sa.String(length=32), zero_indexes=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'comments')
    # ### end Alembic commands ###
