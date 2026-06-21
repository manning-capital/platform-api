"""
Transaction service layer for business logic and database operations.

TODO:
- Import transaction models from mc_postgres_db.models
  - from mc_postgres_db.models import Transaction, Account, Trade, etc.

- Import schemas
  - from ..schemas.transaction import TransactionCreate, TransactionUpdate, etc.

- Create TransactionService class
  - Initialize with database session dependency

- Implement CRUD operations:

  1. create_transaction()
     - Validate input data
     - Check account exists and has sufficient balance (if withdrawal)
     - Create transaction record
     - Update account balance if needed
     - Handle transaction rollback on errors
     - Return created transaction

  2. get_transaction_by_id()
     - Query transaction by ID
     - Include related data (account, trade) if needed
     - Handle not found errors
     - Return transaction or raise HTTPException

  3. get_transactions()
     - Apply filters from TransactionQuery schema
     - Implement pagination
     - Order by date (newest first)
     - Return paginated results

  4. update_transaction()
     - Validate update data
     - Check transaction exists
     - Check if transaction can be updated (e.g., completed transactions might be immutable)
     - Update transaction fields
     - Handle status changes (e.g., if status changes to completed, update account balance)
     - Return updated transaction

  5. delete_transaction()
     - Check if transaction can be deleted (business rules)
     - Revert account balance changes if needed
     - Delete transaction
     - Handle foreign key constraints

- Add business logic methods:
  - validate_transaction_amount()
  - calculate_balance_impact()
  - check_transaction_permissions()
  - process_transaction_status_change()

- Add error handling:
  - Custom exceptions for transaction errors
  - Database constraint violations
  - Validation errors
"""

from sqlalchemy.orm import Session

# TODO: Import transaction models
# from mc_postgres_db.models import Transaction, Account, Trade

# TODO: Import schemas
# from ..schemas.transaction import (
#     TransactionCreate,
#     TransactionUpdate,
#     TransactionQuery,
#     TransactionResponse,
# )


class TransactionService:
    """Service for transaction-related business logic."""

    def __init__(self, db: Session):
        """
        Initialize transaction service with database session.

        TODO: Store db session as instance variable
        """
        # TODO: self.db = db
        pass

    def create_transaction(self, transaction_data) -> dict:
        """
        Create a new transaction.

        TODO:
        - Validate transaction_data (TransactionCreate schema)
        - Check if account exists
        - For withdrawals: verify sufficient balance
        - Create transaction with status PENDING
        - Update account balance if needed
        - Commit transaction
        - Return TransactionResponse
        """
        # TODO: Implement transaction creation logic
        raise NotImplementedError("TODO: Implement create_transaction")

    def get_transaction_by_id(self, transaction_id: int) -> dict:
        """
        Get a transaction by ID.

        TODO:
        - Query Transaction by ID
        - Include related data (eager loading)
        - Raise 404 if not found
        - Return TransactionResponse
        """
        # TODO: Implement get transaction by ID
        raise NotImplementedError("TODO: Implement get_transaction_by_id")

    def get_transactions(
        self, query_params, limit: int = 100, offset: int = 0
    ) -> tuple[list[dict], int]:
        """
        Get filtered and paginated list of transactions.

        TODO:
        - Build query with filters from query_params (TransactionQuery)
        - Apply date range filters
        - Apply status/type filters
        - Apply account_id filter
        - Order by created_at DESC
        - Apply pagination (limit/offset)
        - Count total matching records
        - Return (list of TransactionSummary, total count)
        """
        # TODO: Implement get transactions with filters
        raise NotImplementedError("TODO: Implement get_transactions")

    def update_transaction(self, transaction_id: int, update_data) -> dict:
        """
        Update an existing transaction.

        TODO:
        - Get transaction by ID (raise 404 if not found)
        - Validate update_data (TransactionUpdate schema)
        - Check if transaction can be updated (business rules)
        - Update fields
        - Handle status changes (e.g., PENDING -> COMPLETED)
        - Update account balance if status changed to COMPLETED
        - Commit changes
        - Return TransactionResponse
        """
        # TODO: Implement update transaction
        raise NotImplementedError("TODO: Implement update_transaction")

    def delete_transaction(self, transaction_id: int) -> None:
        """
        Delete a transaction.

        TODO:
        - Get transaction by ID (raise 404 if not found)
        - Check if transaction can be deleted (business rules)
        - Revert account balance changes if needed
        - Delete transaction
        - Commit changes
        """
        # TODO: Implement delete transaction
        raise NotImplementedError("TODO: Implement delete_transaction")

    # TODO: Add helper methods

    def _validate_transaction_amount(self, amount, transaction_type: str) -> bool:
        """Validate transaction amount based on type."""
        # TODO: Implement validation logic
        pass

    def _calculate_balance_impact(self, amount, transaction_type: str) -> float:
        """Calculate how transaction affects account balance."""
        # TODO: Implement balance impact calculation
        pass

    def _check_transaction_permissions(self, transaction_id: int, user_id: int) -> bool:
        """Check if user has permission to modify transaction."""
        # TODO: Implement permission checking
        pass

