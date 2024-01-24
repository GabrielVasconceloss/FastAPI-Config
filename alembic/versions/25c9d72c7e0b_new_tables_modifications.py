"""New tables modifications

Revision ID: 25c9d72c7e0b
Revises: bebae4d5a894
Create Date: 2024-01-24 10:41:03.551737

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25c9d72c7e0b'
down_revision: Union[str, None] = 'bebae4d5a894'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('configuracao_cliente', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('configuracao_cliente', sa.Column('data_criacao', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('configuracao_cliente', 'data_criacao')
    op.drop_column('configuracao_cliente', 'active')
    # ### end Alembic commands ###