TEST           = pytest $(arg)
DC	           = docker compose
CODE 	       = bot tests
CONTAINER_NAME = megazord-tg-bot

.PHONY: build
build:
	$(DC) build

.PHONY: up
up:
	$(DC) up

.PHONY: down
down:
	$(DC) down --volumes

.PHONY install:
install:
	pip install -r requirements.txt -r requirements.tests.txt

.PHONY: format ## Auto-format python source files
format:
	ruff format $(CODE)
	ruff check --fix $(CODE)

.PHONY: lint ## Lint python source files
lint:
	ruff check $(CODE)
	ruff format --check $(CODE)

.PHONY: test-unit
test-unit:
	$(TEST) tests/unit --cov=./ --cov-append

.PHONY: test-integration
test-integration:
	docker exec -it $(CONTAINER_NAME) $(TEST) tests/integration --cov=./ --cov-append

.PHONY: test-e2e
test-e2e:
	docker exec -it $(CONTAINER_NAME) $(TEST) tests/e2e --cov=./ --cov-append

.PHONY: report
report:
	$(TEST) --cov=./ --cov-report html

.PHONY: ci
ci: lint test-unit
