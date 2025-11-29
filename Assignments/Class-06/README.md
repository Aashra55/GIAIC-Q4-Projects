# FastAPI Bank API

This is a simple banking API built with FastAPI. It allows users to authenticate, check their balance, and transfer money to other users.

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install "fastapi[all]"
    ```

2.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

*   `POST /authenticate`: Authenticate a user and get their bank balance.
*   `POST /bank-transfer`: Transfer money from one user to another.

## Project Structure

```
.
├── main.py
├── README.md
└── GEMINI.md
```
