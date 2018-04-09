export $(egrep -v '^#' .env | xargs)

cd base_site

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata db.json

cd ..

honcho start