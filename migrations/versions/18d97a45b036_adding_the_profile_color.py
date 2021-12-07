"""adding the profile color

Revision ID: 18d97a45b036
Revises: b991f777c8dd
Create Date: 2021-11-28 13:23:07.923407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18d97a45b036'
down_revision = 'b991f777c8dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_color', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_color')
    # ### end Alembic commands ###
