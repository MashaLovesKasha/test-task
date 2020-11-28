
ALLURE_DIR := ./allure-results

test:
	pytest

allure:
	allure serve $(ALLURE_DIR)

all: test allure