.ONESHELL:

test:
	sudo docker start redis || sudo docker run --name test-redis -p 6379:6379 -d redis --dir /tmp
	cd src/
	poetry run pytest
	sudo docker stop test-redis
	sudo docker rm test-redis

