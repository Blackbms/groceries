.PHONY start_db stop_db clean_db:

start_db:
	docker compose up  -d
stop_db:
	docker compose down
clean_db:
	docker compose down  -v