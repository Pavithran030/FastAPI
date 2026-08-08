# FastAPI Learning Repository

This repository is a hands-on FastAPI learning project that incrementally demonstrates:

- basic API creation
- Pydantic request/response validation
- GET/POST/PUT/DELETE operations
- SQLAlchemy database integration

Each folder is a standalone example app that you can run independently.

## Repository Structure

- `initialtest/`  
  Minimal FastAPI app with a health-style route.

- `pydantic_data_validation/`  
  Introduces a `Products` Pydantic model and typed response data.

- `fetch_post/`  
  Adds route parameters and POST request handling.

- `delete_put/`  
  Demonstrates PUT and DELETE operations on in-memory data.

- `db_connection/`  
  Adds SQLAlchemy setup and seed-to-database logic.

- `fetch_from_db/`  
  Continues database-backed CRUD flow.

- `db_CRUD/`  
  Database CRUD-oriented variation of the same learning flow.

## Tech Stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Uvicorn
- PostgreSQL (expected by current DB configuration)

## Prerequisites

- Python 3.9+ (recommended)
- `pip`
- (For DB modules) a running PostgreSQL instance

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Pavithran030/FastAPI.git
   cd FastAPI
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
   On Windows (PowerShell):
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic psycopg2-binary
   ```

## Database Configuration

For modules that use SQLAlchemy (`db_connection`, `fetch_from_db`, `db_CRUD`), update `dbconfig.py` with a real PostgreSQL connection string.

The current placeholder value is:

```python
db_url="******localhost:5432/learn"
```

Replace it with a valid URL, for example:

```python
db_url="postgresql://<username>:<password>@localhost:5432/learn"
```

## Running the Apps

Run any module by changing into its directory and starting Uvicorn:

```bash
cd <module_name>
uvicorn main:app --reload
```

Examples:

```bash
cd initialtest
uvicorn main:app --reload
```

```bash
cd delete_put
uvicorn main:app --reload
```

FastAPI docs will be available at:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Sample Endpoints

Depending on the module, available routes include:

- `GET /`
- `GET /pro`
- `GET /{i}`
- `POST /adding`
- `PUT /update/{id}`
- `DELETE /del/{id}`
- `GET /dbs`

## Notes

- This repository is intentionally educational and organized as multiple small examples.
- Several modules share similar code to show progression by feature.
- You can use these apps as a base for building a more structured production FastAPI project.

## License

No license file is currently included in this repository.