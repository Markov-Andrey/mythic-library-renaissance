"""create_organizations_table

Revision ID: 1ef7ace89622
Revises: f14cd938e624
Create Date: 2025-04-30 12:02:14.050353

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# Batch mode for SQLite
from alembic.operations import Operations
from alembic import context

# revision identifiers, used by Alembic.
revision: str = '1ef7ace89622'
down_revision: Union[str, None] = 'f14cd938e624'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Use batch mode for SQLite
    with op.batch_alter_table('organizations', schema=None) as batch_op:
        batch_op.create_foreign_key(
            'fk_organizations_world_id',  # name for the constraint
            'worlds',  # target table
            ['world_id'],  # column in organizations table
            ['id'],  # column in worlds table
        )


def downgrade() -> None:
    """Downgrade schema."""
    # Use batch mode for SQLite
    with op.batch_alter_table('organizations', schema=None) as batch_op:
        batch_op.drop_constraint('fk_organizations_world_id', type_='foreignkey')
