"""first revision

Revision ID: 16468450b245
Revises: 
Create Date: 2024-08-06 17:22:04.385596

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16468450b245'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('fuel_type', sa.Enum('gasoline', 'diesel', 'electric', 'hybrid', name='fueltype'), nullable=False),
    sa.Column('transmission_type', sa.Enum('manual', 'automatic', 'cvt', 'robot', name='transmissiontype'), nullable=False),
    sa.Column('mileage', sa.Float(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cars_brand'), 'cars', ['brand'], unique=False)
    op.create_index(op.f('ix_cars_fuel_type'), 'cars', ['fuel_type'], unique=False)
    op.create_index(op.f('ix_cars_id'), 'cars', ['id'], unique=False)
    op.create_index(op.f('ix_cars_mileage'), 'cars', ['mileage'], unique=False)
    op.create_index(op.f('ix_cars_model'), 'cars', ['model'], unique=False)
    op.create_index(op.f('ix_cars_price'), 'cars', ['price'], unique=False)
    op.create_index(op.f('ix_cars_transmission_type'), 'cars', ['transmission_type'], unique=False)
    op.create_index(op.f('ix_cars_year'), 'cars', ['year'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cars_year'), table_name='cars')
    op.drop_index(op.f('ix_cars_transmission_type'), table_name='cars')
    op.drop_index(op.f('ix_cars_price'), table_name='cars')
    op.drop_index(op.f('ix_cars_model'), table_name='cars')
    op.drop_index(op.f('ix_cars_mileage'), table_name='cars')
    op.drop_index(op.f('ix_cars_id'), table_name='cars')
    op.drop_index(op.f('ix_cars_fuel_type'), table_name='cars')
    op.drop_index(op.f('ix_cars_brand'), table_name='cars')
    op.drop_table('cars')
    # ### end Alembic commands ###
