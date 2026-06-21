from mc_postgres_db.testing.utilities import postgres_test_harness
import pytest


@pytest.fixture(scope="session", autouse=True)
def engine():
    with postgres_test_harness(use_prefect=False) as engine:
        yield engine
