"""
Pydantic schemas for transaction-related API requests and responses.

TODO:
- Review mc_postgres_db.models transaction tables to understand structure
  - Check Transaction model fields (id, amount, timestamp, status, type, etc.)
  - Check related models (Trade, Order, Account, etc.)
  - Identify relationships and foreign keys

- Create base transaction schema
  - TransactionBase: Common fields shared between create/update/response
  - Include all relevant fields from SQLAlchemy model

- Create request schemas
  - TransactionCreate: Fields required for creating a new transaction
  - TransactionUpdate: Optional fields for updating a transaction
  - TransactionQuery: Filters for querying transactions (date range, status, etc.)

- Create response schemas
  - TransactionResponse: Full transaction details for API responses
  - TransactionSummary: Lightweight transaction summary
  - TransactionList: Paginated list of transactions

- Add validation
  - Amount validation (positive/negative, decimal precision)
  - Status enum validation
  - Date/time validation
  - Foreign key validation (account_id, trade_id, etc.)
"""

from pydantic import BaseModel, ConfigDict


# TODO: Define TransactionStatus enum based on mc_postgres_db.models
# from enum import Enum
# class TransactionStatus(str, Enum):
#     PENDING = "pending"
#     COMPLETED = "completed"
#     FAILED = "failed"
#     CANCELLED = "cancelled"


# TODO: Define TransactionType enum based on mc_postgres_db.models
# class TransactionType(str, Enum):
#     DEPOSIT = "deposit"
#     WITHDRAWAL = "withdrawal"
#     TRADE = "trade"
#     FEE = "fee"


class TransactionBase(BaseModel):
    """Base transaction schema with common fields."""

    # TODO: Add fields based on mc_postgres_db.models.Transaction
    # amount: Decimal = Field(..., description="Transaction amount")
    # transaction_type: TransactionType = Field(..., description="Type of transaction")
    # status: TransactionStatus = Field(..., description="Transaction status")
    # description: Optional[str] = Field(None, description="Transaction description")
    # account_id: int = Field(..., description="Associated account ID")
    # trade_id: Optional[int] = Field(None, description="Associated trade ID if applicable")
    pass


class TransactionCreate(TransactionBase):
    """Schema for creating a new transaction."""

    # TODO: Add fields required for creation
    # May include additional fields not in base if needed
    pass


class TransactionUpdate(BaseModel):
    """Schema for updating a transaction."""

    # TODO: Add optional fields that can be updated
    # amount: Optional[Decimal] = None
    # status: Optional[TransactionStatus] = None
    # description: Optional[str] = None
    pass


class TransactionResponse(TransactionBase):
    """Schema for transaction API responses."""

    # TODO: Add response-specific fields
    # id: int = Field(..., description="Transaction ID")
    # created_at: datetime = Field(..., description="Transaction creation timestamp")
    # updated_at: Optional[datetime] = Field(None, description="Last update timestamp")

    model_config = ConfigDict(from_attributes=True)  # Enable ORM mode for SQLAlchemy


class TransactionSummary(BaseModel):
    """Lightweight transaction summary for list views."""

    # TODO: Add minimal fields for summary
    # id: int
    # amount: Decimal
    # transaction_type: TransactionType
    # status: TransactionStatus
    # created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TransactionQuery(BaseModel):
    """Schema for querying/filtering transactions."""

    # TODO: Add query parameters
    # account_id: Optional[int] = None
    # status: Optional[TransactionStatus] = None
    # transaction_type: Optional[TransactionType] = None
    # start_date: Optional[datetime] = None
    # end_date: Optional[datetime] = None
    # limit: int = Field(100, ge=1, le=1000)
    # offset: int = Field(0, ge=0)
    pass


class TransactionListResponse(BaseModel):
    """Paginated list of transactions."""

    # TODO: Add pagination fields
    # transactions: list[TransactionSummary]
    # total: int
    # limit: int
    # offset: int
    pass

