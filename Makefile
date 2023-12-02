requirements:
	poetry lock
	poetry export --without-hashes --format=requirements.txt > requirements.txt
	poetry export --without-hashes --format=requirements.txt --dev > requirements-dev.txt
	poetry export --without-hashes --format=requirements.txt --with examples > requirements-examples.txt

build:
	poetry build

publish: 
	poetry publish
