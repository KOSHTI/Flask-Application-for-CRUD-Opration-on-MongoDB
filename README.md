# Flask-Application-for-CRUD-Opration-on-MongoDB

## Set up & Installation.

### 1 .Create a virtual environment 
                    
```bash
python -m venv venv
```
### 2 .Activate the environment

``` venv\Scripts\activate```

### 3 .Install the requirements

```pip install -r requirements.txt```

### 4. Install Flask and also Docker from official website

```pip install flask```

### 5. Create the required files

Create two files; **app.py** and **Dockerfile**

### 6. Run the application

```python app.py```

### 7. Test application in Postman

**API Endpoints**
##### I.  **GET /users:** Retrieve a list of all items.
##### II. **GET /users/{id}:** Retrieve details of a specific item by ID.
##### III.**POST /users:** Create a new item.
##### IV. **PUT /users/{id}:** Update an existing item by ID.
##### V.  **DELETE /users/{id}:** Delete an item by ID.