.PHONY start_db stop_db:
# TODO: Use docker-compose instead of docker run

start_db:
# docker-compose up -d
	docker run --name grocery-postgres -e POSTGRES_PASSWORD=password -v /home/blackbms/workspace/groceries/data:/var/lib/postgresql/data -p 5432:5432 -d postgres:latest
stop_db:
# docker-compose down
	docker stop grocery-postgres
	docker rm grocery-postgres