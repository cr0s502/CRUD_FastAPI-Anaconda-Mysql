#FastAPI con ANACONDA-ENV y SQLALCHEMY

---

1-Install Anaconda
2-In the folder open terminal  
3-Install dependecies = pip install -r requirements.txt
4-Active Env = conda activate fastapi
5-Start Server = uvicorn app:app --reload

####endpoint

- GET "/users" : return all users from database
- GET "/users/{id}" : return a user by id from database
- POST "/users" : create a user in the database
- PUT "/users/{id}" : update a user by id in the database
- DELETE "/users/{id}" : delete a user by id in the database
