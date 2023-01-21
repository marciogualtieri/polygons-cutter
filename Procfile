service: python ./manage.py migrate && python ./manage.py collectstatic --noinput && uwsgi --ini ./uwsgi.ini
format: autoflake -i -r --remove-all-unused-imports . && black . & isort .
check: black --check . && isort --check-only . && mypy .
test: pytest -s -v --log-cli-level=DEBUG
coverage: pytest --cov=. --cov-report=html
runserver: python ./manage.py collectstatic --no-input && python ./manage.py runserver
migrate: python ./manage.py migrate
