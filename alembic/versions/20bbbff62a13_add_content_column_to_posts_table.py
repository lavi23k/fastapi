"""add content column to posts table

Revision ID: 20bbbff62a13
Revises: 04fa87b7fa5d
Create Date: 2024-07-07 15:02:54.759036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20bbbff62a13'
down_revision: Union[str, None] = '04fa87b7fa5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass