run:
	python -m pytest test.py --alluredir allure_report
	allure serve allure_report