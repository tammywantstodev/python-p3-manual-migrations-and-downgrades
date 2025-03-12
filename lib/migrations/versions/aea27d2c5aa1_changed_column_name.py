"""Changed column name

Revision ID: aea27d2c5aa1
Revises: 791279dd0760
Create Date: 2025-03-12 18:51:20.058584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aea27d2c5aa1'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('marks', sa.Integer(), nullable=True))
    op.drop_column('students', 'grade')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('grade', sa.INTEGER(), nullable=True))
    op.drop_column('students', 'marks')
    # ### end Alembic commands ###
