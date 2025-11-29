from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory database
db = {
    "ali": {"pin_number": "1234", "bank_balance": 1000.0},
    "ahmed": {"pin_number": "5678", "bank_balance": 500.0},
    "usman": {"pin_number": "9876", "bank_balance": 2000.0},
}

# Pydantic Models
class User(BaseModel):
    name: str
    pin_number: str

class Transfer(BaseModel):
    sender: str
    pin_number: str
    recipients_name: str
    amount: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bank API"}

@app.post("/authenticate")
def authenticate(user: User):
    if user.name not in db:
        raise HTTPException(status_code=404, detail="User not found")
    if db[user.name]["pin_number"] != user.pin_number:
        raise HTTPException(status_code=401, detail="Invalid PIN")
    return {"bank_balance": db[user.name]["bank_balance"]}

@app.post("/bank-transfer")
def bank_transfer(transfer: Transfer):
    if transfer.sender not in db:
        raise HTTPException(status_code=404, detail="Sender not found")
    if db[transfer.sender]["pin_number"] != transfer.pin_number:
        raise HTTPException(status_code=401, detail="Invalid PIN for sender")
    if transfer.recipients_name not in db:
        raise HTTPException(status_code=404, detail="Recipient not found")
    if db[transfer.sender]["bank_balance"] < transfer.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    db[transfer.sender]["bank_balance"] -= transfer.amount
    db[transfer.recipients_name]["bank_balance"] += transfer.amount

    return {
        "sender_balance": db[transfer.sender]["bank_balance"],
        "receiver_balance": db[transfer.recipients_name]["bank_balance"],
    }
