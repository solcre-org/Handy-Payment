from pydantic import BaseModel
from typing import List, Optional


class Product(BaseModel):
    Name: str
    Quantity: float
    Amount: float
    TaxedAmount: float


class Cart(BaseModel):
    InvoiceNumber: int
    Currency: int
    TaxedAmount: float
    TotalAmount: float
    Products: List[Product]
    LinkImageUrl: str
    TransactionExternalId: str


class Client(BaseModel):
    CommerceName: str
    SiteUrl: str


class Payment(BaseModel):
    CallbackUrl: str
    ResponseType: str
    Cart: Cart
    Client: Client


class PurchaseData(BaseModel):
    Status: int
    Created: str
    Products: List[Product]
    TotalAmount: float
    TaxedAmount: float
    Currency: int


class InstrumentData(BaseModel):
    Expiration: str = None


class Callback(BaseModel):
    TransactionExternalId: str
    PurchaseData: PurchaseData
    InstrumentData: InstrumentData
