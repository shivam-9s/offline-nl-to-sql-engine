# 🧠 Offline Natural Language to SQL Engine

An **Offline Natural Language to SQL Engine** that converts human language queries into SQL statements using a custom rule-based NLP pipeline.

This system processes natural language input, understands the user's intent, maps words to database schema, and generates a valid SQL query — all **without using external APIs or online LLMs**.

---

# 🚀 Project Overview

Many users struggle to write SQL queries to retrieve information from databases. This project bridges that gap by allowing users to interact with databases using **natural language**.

Example:

Natural Language Query:

```
show employees with salary greater than 50000
```

Generated SQL Query:

```
SELECT * FROM employees WHERE salary > 50000;
```

The system converts user queries into SQL using a modular pipeline consisting of preprocessing, intent detection, parsing, schema mapping, and SQL generation.

---

# 🏗️ System Architecture

The system follows a multi-stage processing pipeline:

```
User Query
     │
     ▼
Query Normalization
     │
     ▼
Intent Detection
     │
     ▼
Query Parsing
     │
     ▼
Schema Mapping
     │
     ▼
SQL Query Builder
     │
     ▼
Generated SQL Query
```

---

# 📂 Project Structure

```
nl_sql_engine
│
├── builder
│   ├── schema.py
│   ├── relations.py
│   └── synonyms.py
│
├── intent
│   └── classifier.py
│
├── mapper
│   └── schema_mapper.py
│
├── parser
│   ├── ast.py
│   └── grammar.py
│
├── preprocessing
│   └── normalizer.py
│
├── tests
│   ├── test_intent.py
│   ├── test_mapper.py
│   ├── test_normalizer.py
│   ├── test_parser.py
│   ├── test_pipeline.py
│   └── test_sql_builder.py
│
├── api.py
├── main.py
└── README.md
```

---

# ⚙️ How the System Works

## 1️⃣ Query Preprocessing

The input query is cleaned and normalized.

Example:

```
Show me all employees
```

Normalized:

```
show employees
```

Tasks performed:

* Lowercasing
* Removing unnecessary words
* Standardizing terms

---

## 2️⃣ Intent Detection

The system identifies the **type of query**.

Examples:

| Query                               | Intent    |
| ----------------------------------- | --------- |
| show employees                      | SELECT    |
| count employees                     | COUNT     |
| average salary                      | AGGREGATE |
| employees salary greater than 50000 | FILTER    |

This step determines how the SQL query should be constructed.

---

## 3️⃣ Query Parsing

The query is converted into a structured representation (AST).

Example:

Input:

```
employees with salary greater than 50000
```

Parsed Structure:

```
ACTION: SELECT
TABLE: employees
CONDITION: salary > 50000
```

---

## 4️⃣ Schema Mapping

The system maps natural language words to database schema.

Example:

| Natural Word | Database Element |
| ------------ | ---------------- |
| employees    | employees table  |
| salary       | salary column    |

This ensures the generated SQL uses correct table and column names.

---

## 5️⃣ SQL Query Generation

The SQL builder constructs the final query.

Example Output:

```
SELECT *
FROM employees
WHERE salary > 50000;
```

---

# 🧪 Example Queries

### Example 1

Input:

```
show employees
```

Output:

```
SELECT * FROM employees;
```

---

### Example 2

Input:

```
count employees
```

Output:

```
SELECT COUNT(*) FROM employees;
```

---

### Example 3

Input:

```
employees with salary greater than 70000
```

Output:

```
SELECT * FROM employees WHERE salary > 70000;
```

---

# 🖥️ Running the Project

## 1️⃣ Clone the Repository

```
git clone https://github.com/shivam-9s/offline-nl-to-sql-engine.git
```

```
cd offline-nl-to-sql-engine
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```
pip install fastapi uvicorn pydantic
```

---

## 4️⃣ Run the API Server

```
uvicorn api:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 5️⃣ Open API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

You can test the **NL → SQL conversion API** directly from the Swagger interface.

---

# 🔌 API Usage

### Endpoint

```
POST /nl-to-sql/
```

### Request

```
{
  "query": "show employees with salary greater than 50000"
}
```

### Response

```
{
  "sql": "SELECT * FROM employees WHERE salary > 50000;"
}
```

---

# 🧪 Running Unit Tests

```
pytest tests
```

This validates individual components including:

* Intent detection
* Parser
* Schema mapping
* SQL generation
* Pipeline flow

---

# 🛠️ Technologies Used

* Python
* FastAPI
* Rule-based NLP
* Abstract Syntax Tree Parsing
* REST API Development

---

# 📌 Key Features

✔ Natural Language Query Processing
✔ Offline NLP Pipeline
✔ SQL Query Generation
✔ Modular Architecture
✔ FastAPI Backend
✔ Unit Testing Support

---

# 🚀 Future Improvements

Potential enhancements include:

• Database query execution (SQLite/MySQL)
• Chat-style interface for queries
• Automatic schema discovery
• Machine learning based intent detection
• Multi-table query support with joins

---

# 👨‍💻 Author

**Shivam Kumar**

GitHub:
https://github.com/shivam-9s

---

# ⭐ If you found this project useful, consider giving it a star!
