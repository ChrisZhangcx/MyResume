"""initial migration

Revision ID: 542c9a49b249
Revises: 19e6cbc521f7
Create Date: 2017-01-05 13:03:23.671995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '542c9a49b249'
down_revision = '19e6cbc521f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'f3', 'cer', type_='foreignkey')
    op.drop_constraint(u'f2', 'cer', type_='foreignkey')
    op.drop_constraint(u'f4', 'count_result', type_='foreignkey')
    op.drop_constraint(u'f5', 'cr', type_='foreignkey')
    op.drop_constraint(u'f1', 'cs', type_='foreignkey')
    op.drop_index('password', table_name='users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('password', 'users', ['password'], unique=True)
    op.create_foreign_key(u'f1', 'cs', 'class_info', ['Class'], ['Class'], onupdate=u'CASCADE', ondelete=u'CASCADE')
    op.create_foreign_key(u'f5', 'cr', 'class_info', ['Class'], ['Class'], onupdate=u'CASCADE', ondelete=u'CASCADE')
    op.create_foreign_key(u'f4', 'count_result', 'class_info', ['Class'], ['Class'], onupdate=u'CASCADE', ondelete=u'CASCADE')
    op.create_foreign_key(u'f2', 'cer', 'class_info', ['Class'], ['Class'], onupdate=u'CASCADE', ondelete=u'CASCADE')
    op.create_foreign_key(u'f3', 'cer', 'ce', ['Eno'], ['Eno'], onupdate=u'CASCADE', ondelete=u'CASCADE')
    # ### end Alembic commands ###
