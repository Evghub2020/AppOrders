python 3.11.0

В консоле git bash не в powershell!

python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

/swagger/
/admin/
