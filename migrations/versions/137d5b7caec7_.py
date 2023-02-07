"""empty message

Revision ID: 137d5b7caec7
Revises: 
Create Date: 2023-02-06 12:22:14.751451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '137d5b7caec7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_utilisateur', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'utilisateurs', ['id_utilisateur'], ['id'])

    with op.batch_alter_table('produits', schema=None) as batch_op:
        batch_op.add_column(sa.Column('prix', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produits', schema=None) as batch_op:
        batch_op.drop_column('prix')

    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('id_utilisateur')

    # ### end Alembic commands ###
