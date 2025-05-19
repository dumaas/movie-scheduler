build:
	docker build -t movie-scheduler .

main:
	docker run --rm -it -v $(PWD)/src:/app/src movie-scheduler python -m src.main

test:
	docker run --rm -v $(PWD)/src:/app/src -v $(PWD)/tests:/app/tests movie-scheduler python -m unittest discover -s tests