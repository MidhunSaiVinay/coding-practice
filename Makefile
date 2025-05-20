.PHONY: dev build test lint clean

dev:
	docker-compose up

build:
	docker-compose build

test:
	docker-compose run backend pytest
	docker-compose run frontend npm test

lint:
	docker-compose run backend black . && docker-compose run backend ruff check .
	docker-compose run frontend npm run lint

clean:
	docker-compose down -v
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name "node_modules" -exec rm -r {} + 