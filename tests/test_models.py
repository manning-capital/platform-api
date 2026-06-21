from typing import Any, Type
from sqlalchemy.engine import Engine
from sqlalchemy import inspect
import mc_postgres_db.models as models


def _get_python_type_name(python_type: Type[Any]) -> str:
    """Convert Python type to string name."""
    if hasattr(python_type, "__name__"):
        return python_type.__name__
    return str(python_type)


def test_schema_matches_expected(engine: Engine):
    # Get all assets from the database using SQLAlchemy inspector.
    inspector = inspect(engine)

    # Check the meta of the assets against the expected schema.
    expected = {
        column.name: _get_python_type_name(column.type.python_type)
        for column in models.Asset.__table__.columns
    }

    # Get the actual schema from the database using SQLAlchemy inspector.
    columns = inspector.get_columns(models.Asset.__tablename__)
    actual = {
        column["name"]: _get_python_type_name(column["type"].python_type)
        for column in columns
    }

    # Compare the expected and actual schemas.
    assert expected == actual
