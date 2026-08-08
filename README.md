# FastAPI Learning Playground

A curated collection of small FastAPI examples that progressively build from the basics of routing to Pydantic validation, HTTP methods, and SQLAlchemy-backed CRUD operations.

This repository is designed as a hands-on learning reference and a quick cheat sheet for revisiting FastAPI concepts fast.

---

## Table of Contents

- [About This Repository](#about-this-repository)
- [Project Structure](#project-structure)
- [Learning Path](#learning-path)
- [Topics Covered](#topics-covered)
- [Cheat Sheet](#cheat-sheet)
- [How to Use the Examples](#how-to-use-the-examples)
- [Suggested Workflow](#suggested-workflow)
- [Key FastAPI Concepts Recap](#key-fastapi-concepts-recap)
- [Notes](#notes)

---

## About This Repository

This repo contains multiple small FastAPI practice projects, each focused on one concept. The examples are intentionally separated so you can study one topic at a time and compare how APIs evolve from simple routes to database-driven applications.

The main learning areas include:

- Creating your first FastAPI route
- Request and response handling
- Pydantic model validation
- GET, POST, PUT, and DELETE endpoints
- Working with SQLAlchemy
- Connecting FastAPI to a database
- Performing CRUD operations with persistence

---

## Project Structure

The repository is organized into topic-based folders:

- `initialtest` — basic route setup
- `pydantic_data_validation` — Pydantic model validation
- `fetch_post` — GET and POST usage
- `delete_put` — PUT and DELETE operations
- `db_connection` — SQLAlchemy database connection
- `fetch_from_db` — reading data from the database
- `db_CRUD` — full CRUD persistence example

> Tip: Each folder is meant to be read independently, but they also form a natural progression from beginner to intermediate FastAPI concepts.

---

## Learning Path

Follow the folders in this order for the smoothest learning experience:

1. **`initialtest`**
   - Understand app creation and a basic route.
2. **`pydantic_data_validation`**
   - Learn how FastAPI validates incoming JSON automatically.
3. **`fetch_post`**
   - Practice reading query/path data and sending request bodies.
4. **`delete_put`**
   - Learn update and delete flows.
5. **`db_connection`**
   - Connect FastAPI to a SQL database using SQLAlchemy.
6. **`fetch_from_db`**
   - Fetch records from persistent storage.
7. **`db_CRUD`**
   - Combine all core ideas into a full CRUD workflow.

---

## Topics Covered

| Topic | What You Learn |
|---|---|
| FastAPI setup | Creating an app instance and route definitions |
| Routing | Handling HTTP endpoints and paths |
| Request handling | Reading data from requests |
| Pydantic | Defining schemas and validating input |
| GET | Retrieving data from an API |
| POST | Creating new data |
| PUT | Updating existing data |
| DELETE | Removing data |
| SQLAlchemy | Database engine, sessions, and ORM basics |
| CRUD | Create, Read, Update, Delete workflows |

---

## Cheat Sheet

### 1) FastAPI basics

- Create an application with `FastAPI()`.
- Define routes with decorators like `@app.get()`.
- Return Python dictionaries, and FastAPI converts them to JSON automatically.

### 2) Common HTTP methods

- **GET**: read data
- **POST**: create data
- **PUT**: update data
- **DELETE**: remove data

### 3) Pydantic models

Use Pydantic to:

- validate request bodies
- define schema structure
- ensure data types are correct
- keep API input clean and predictable

### 4) Validation benefits

- prevents malformed input
- reduces manual checking
- gives automatic error responses
- improves API reliability

### 5) Database integration

With SQLAlchemy, you can:

- connect to a database
- define ORM models
- create sessions
- query records
- persist changes

### 6) CRUD flow

- **Create**: add new records
- **Read**: fetch records
- **Update**: modify records
- **Delete**: remove records

---

## How to Use the Examples

Each folder can be explored as a separate mini-project.

Recommended approach:

1. Open one folder at a time.
2. Read the main Python file(s).
3. Run the app for that topic.
4. Test the endpoints using:
   - browser
   - `curl`
   - Postman
   - Swagger UI (`/docs`)

FastAPI automatically provides interactive API documentation, which makes it easy to inspect and test endpoints.

---

## Suggested Workflow

If you are learning FastAPI from this repo, use this workflow:

- Start with the route examples
- Move to Pydantic validation
- Practice request methods
- Add update/delete operations
- Introduce SQLAlchemy
- Finish with CRUD persistence

This order helps you build confidence before moving to database-backed APIs.

---

## Key FastAPI Concepts Recap

### App
The main FastAPI application object coordinates routes and request handling.

### Routes
Routes map URLs and HTTP methods to Python functions.

### Schemas
Schemas define the shape of the data your API expects or returns.

### Automatic docs
FastAPI generates interactive docs automatically.

### Dependency on data models
As your app grows, data models keep input and database logic structured.

### Database sessions
Database sessions are used to communicate with the database safely and efficiently.

---

## Notes

- This repository is a learning playground, not a production template.
- Folder names reflect each topic and can be used as a quick reference index.
- The repo is best understood by reading it in sequence from top to bottom.

---

## Quick Recap

If you need a one-line summary:

> This repository is a FastAPI learning sheet that covers routing, Pydantic validation, HTTP methods, SQLAlchemy integration, and CRUD operations in a step-by-step format.
