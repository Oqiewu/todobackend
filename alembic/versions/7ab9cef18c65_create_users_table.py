"""create users table

Revision ID: 7ab9cef18c65
Revises: 08fff4177186
Create Date: 2023-03-15 14:52:25.436245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ab9cef18c65'
down_revision = '08fff4177186'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        email TEXT UNIQUE,
        hashed_password TEXT UNIQUE,
        is_active BOOLEAN DEFAULT TRUE,
        is_superuser BOOLEAN DEFAULT FALSE,
        is_verified BOOLEAN DEFAULT TRUE)""")


def downgrade() -> None:
    op.drop_table('user')
