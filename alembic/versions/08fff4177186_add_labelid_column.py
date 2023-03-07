"""add labelid column 

Revision ID: 08fff4177186
Revises: 2a7c9a0b7170
Create Date: 2023-03-04 23:04:03.714673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08fff4177186'
down_revision = '2a7c9a0b7170'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE tasks ADD COLUMN label_id INTEGER REFERENCES label(id) ON DELETE CASCADE ON UPDATE CASCADE DEFAULT 1")


def downgrade() -> None:
    op.execute("ALTER TABLE tasks DROP COLUMN label_id")
