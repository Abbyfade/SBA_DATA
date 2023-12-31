"""empty message

Revision ID: 98c858be70ff
Revises: 
Create Date: 2023-07-25 09:54:16.648197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98c858be70ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("top_gainers", "percent_change", new_column_name="percent")
    op.add_column("percent_change", sa.Column("percent_change", sa.Float(precision=2, asdecimal=True)))
    op.execute("UPDATE top_gainers  SET percent_change = CAST(percent AS FLOAT(precision=2, asdecimal=True))")
    op.drop_column("top_gainers", "percent")

    op.alter_column("top_losers", "percent_change", new_column_name="percent")
    op.add_column("percent_change", sa.Column("percent_change", sa.Float(precision=2, asdecimal=True)))
    op.execute("UPDATE top_losers  SET percent_change = CAST(percent AS FLOAT(precision=2, asdecimal=True))")
    op.drop_column("top_losers", "percent")
    
    op.alter_column("indices", "percent_change", new_column_name="percent")
    op.add_column("percent_change", sa.Column("percent_change", sa.Float(precision=2, asdecimal=True)))
    op.execute("UPDATE indices  SET percent_change = CAST(percent AS FLOAT(precision=2, asdecimal=True))")
    op.drop_column("indices", "percent")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
