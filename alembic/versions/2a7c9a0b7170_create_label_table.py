"""create label table

Revision ID: 2a7c9a0b7170
Revises: 
Create Date: 2023-03-04 22:52:06.104638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a7c9a0b7170'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    label = op.create_table(
        "label",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False)
        )

    op.bulk_insert(label, 
        [
            {
                "id": 1,
                "name": "default"
            }
        ])


def downgrade() -> None:
    op.drop_table('label')