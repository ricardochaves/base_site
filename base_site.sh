export $(egrep -v '^#' .env | xargs)

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata admin.json
python manage.py collectstatic --noinput

honcho start