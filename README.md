# pythondocker

make sure you have python 3 installed 

Run your virtual environment:
    venv\Scripts\activate

Run the server with:
    (venv): $ flask run

Migrate data changes to app:    
    flask db migrate -m "posts table"
    flask db upgrade

