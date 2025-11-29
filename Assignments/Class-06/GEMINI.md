Make a FastAPI backend with two API routes:

1. /authenticate  (POST)
   - Ask for: name, pin_number
   - Validate the user by checking name and pin_number
   - Return the current bank_balance of that user
   - If wrong pin or user not found, return an error

2. /bank-transfer  (POST)
   - Ask for: sender, pin_number, recipients_name, amount
   - Check sender’s credentials
   - Check if receiver exists
   - Deduct amount from sender’s account
   - Add the same amount to the receiver’s account
   - Return updated balances for sender and receiver

After creating the backend, follow this flow:
- Call /authenticate for the sender
- Call /bank-transfer to transfer money
- Call /authenticate for the receiver to verify updated balance

Create a complete FastAPI project including:
- Models using Pydantic
- In-memory database (dictionary)
- Error handling
- Instructions on how to run using uvicorn
