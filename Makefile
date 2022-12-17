launch-scraper:
	 python3 ./src/hello.py

install-packages:
	pipenv install -e src

init:
	./scripts/init.sh