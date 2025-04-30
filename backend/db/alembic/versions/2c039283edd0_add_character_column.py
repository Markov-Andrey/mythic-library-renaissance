"""add_character_column

Revision ID: 2c039283edd0
Revises: 86eb82e8327c
Create Date: 2025-04-30 15:55:20.407201

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2c039283edd0'
down_revision: Union[str, None] = '86eb82e8327c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Полный ребилд таблицы characters с добавлением внешнего ключа — SQLite-стиль
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.create_foreign_key(
            'fk_characters_world_id', 'worlds', ['world_id'], ['id']
        )


def downgrade():
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_constraint('fk_characters_world_id', type_='foreignkey')
