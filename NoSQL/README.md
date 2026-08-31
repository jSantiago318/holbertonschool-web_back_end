# NoSQL

Project on MongoDB: querying, inserting, updating and deleting documents from
the `mongo` shell and from Python with PyMongo.

## Learning objectives

- What NoSQL means and how it differs from SQL.
- What ACID is.
- What document storage is.
- What the NoSQL types and their benefits are.
- How to query information from a NoSQL database.
- How to insert, update and delete information from a NoSQL database.
- How to use MongoDB.

## Requirements

### MongoDB command files

- All files are interpreted/compiled on Ubuntu 20.04 LTS using MongoDB (version 4.4).
- All files end with a new line.
- The first line of all files is a comment: `// my comment`.

### Python scripts

- All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3`
  (version 3.9) and PyMongo (version 4.8.0).
- All files end with a new line.
- The first line of all files is exactly `#!/usr/bin/env python3`.
- Code uses the `pycodestyle` style (version 2.5.x).
- All modules and functions have documentation.
- Code is not executed when imported, by using `if __name__ == "__main__":`.

## Files

| File | Description |
| ---- | ----------- |
| `0-list_databases` | Script that lists all the databases of the MongoDB instance. |
| `1-use_or_create_database` | Script that creates or switches to the database `my_db`. |
| `2-insert` | Script that inserts a document with `name: "Holberton school"` in the collection `school` of the database passed to `mongo`. |
| `3-all` | Script that lists all the documents of the collection `school`. |
| `4-match` | Script that lists the documents of the collection `school` whose `name` is `"Holberton school"`. |
