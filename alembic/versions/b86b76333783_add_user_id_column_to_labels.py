"""add user_id column to labels

Revision ID: b86b76333783
Revises: 7ab9cef18c65
Create Date: 2023-03-22 00:53:39.653371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b86b76333783'
down_revision = '7ab9cef18c65'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("ALTER TABLE label ADD COLUMN user_id INTEGER REFERENCES user(id) ON DELETE CASCADE ON UPDATE CASCADE DEFAULT 0")


def downgrade() -> None:
    op.execute("ALTER TABLE label DROP COLUMN user_id")
