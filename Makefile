fmt:
	isort --recursive .
	black .

test:
	black --check .
	flake8
	isort --recursive --check-only .
	mypy .