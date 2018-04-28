export $(egrep -v '^#' .env | xargs)

cd base_site/base_site

python manage.py makemigrations
python manage.py migrate
# python manage.py loaddata db.json
python manage.py collectstatic --noinput

cd ..
cd ..

honcho start