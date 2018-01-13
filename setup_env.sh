#!/bin/bash
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL="postgresql://admin:admin2017@localhost:5432/statlab"

echo "-------------------------ADDED VARIABLES----------------------------"

pip3 install -r requirements.txt
echo "-------------------------ADDED PACKAGES-----------------------------"

echo "******************************"
echo "*                            *"
echo "* SET PASSWORD TO: admin2017 *"
echo "*                            *"
echo "******************************"
psql -U postgres -tc "SELECT 1 FROM pg_user WHERE pg_user.usename = 'admin'" | grep -q 1 || psql -U postgres -c "CREATE USER admin WITH PASSWORD 'admin2017' CREATEDB"
psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'statlab'" | grep -q 1 || psql -U postgres -c "CREATE DATABASE statlab"

cd src
echo "-----running python3 manage.py db init-----"
python3 manage.py db init
echo "-----running python3 manage.py db migrate-----"
python3 manage.py db migrate
echo "-----running python3 manage.py db upgrade-----"
python3 manage.py db upgrade

echo "-----importing database-----"
psql statlab < statlab-db_dump -U postgres

echo "-------------------------COMPLETED SETUP----------------------------"

echo "RUN: python3 app.py"

echo "Open your preferred browser and go to 'http://localhost:5000/login'"
echo "Test users: (can log into some test accounts with these)"
echo "Student email: bravojohnny@grats.fam, password: lorsisthebest"
echo "Professor email: sohee@utsc.ca, password: sohee2017"
