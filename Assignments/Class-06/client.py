import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def authenticate(name, pin_number):
    print(f"Authenticating {name}...")
    response = requests.post(
        f"{BASE_URL}/authenticate",
        json={"name": name, "pin_number": pin_number}
    )
    if response.status_code == 200:
        print(f"Authentication successful. Balance: {response.json()['bank_balance']}")
    else:
        print(f"Authentication failed: {response.json()['detail']}")
    print("-" * 20)
    return response

def bank_transfer(sender, pin_number, recipients_name, amount):
    print(f"Transferring {amount} from {sender} to {recipients_name}...")
    response = requests.post(
        f"{BASE_URL}/bank-transfer",
        json={
            "sender": sender,
            "pin_number": pin_number,
            "recipients_name": recipients_name,
            "amount": amount,
        },
    )
    if response.status_code == 200:
        print("Transfer successful.")
        print(f"Sender's new balance: {response.json()['sender_balance']}")
        print(f"Receiver's new balance: {response.json()['receiver_balance']}")
    else:
        print(f"Transfer failed: {response.json()['detail']}")
    print("-" * 20)
    return response

if __name__ == "__main__":
    # 1. Call /authenticate for the sender
    authenticate("ali", "1234")

    # 2. Call /bank-transfer to transfer money
    bank_transfer("ali", "1234", "ahmed", 200)

    # 3. Call /authenticate for the receiver to verify updated balance
    authenticate("ahmed", "5678")

    # 4. Call /authenticate for the sender to verify updated balance
    authenticate("ali", "1234")
