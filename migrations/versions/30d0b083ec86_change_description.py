"""change description

Revision ID: 30d0b083ec86
Revises: 4d24e58ec8a1
Create Date: 2023-09-01 14:25:55.131899
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30d0b083ec86'
down_revision: Union[str, None] = '4d24e58ec8a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'product', 'description', existing_type=sa.VARCHAR(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'product', 'description', existing_type=sa.VARCHAR(), nullable=False
    )
    # ### end Alembic commands ###