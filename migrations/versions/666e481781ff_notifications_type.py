"""notifications -type

Revision ID: 666e481781ff
Revises: 21bcde59cf13
Create Date: 2019-02-19 17:29:46.656106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '666e481781ff'
down_revision = '21bcde59cf13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_notification_type'), ['type'], unique=False)
        batch_op.drop_index('ix_notification_name')
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notification', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=128), nullable=True))
        batch_op.create_index('ix_notification_name', ['name'], unique=False)
        batch_op.drop_index(batch_op.f('ix_notification_type'))

    # ### end Alembic commands ###
