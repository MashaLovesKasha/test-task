
ALLURE_DIR := ./allure_result

test: clean
	pytest --alluredir=$(ALLURE_DIR) -v ./tests

allure:
	allure serve $(ALLURE_DIR)

clean:
	rm -rf $(ALLURE_DIR)

all: test allure