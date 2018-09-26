clean:
	sudo find . -name '000*.py' -delete && sudo find . -name '*.pyc' -delete && sudo find . -name '__pycache__' -delete

mysql-docker:
	sudo docker exec -it mysql bash

app-docker:
	sudo docker exec -it sys_controla_pet bash

docker-admin-group:
	sudo groupadd docker && sudo usermod -aG docker $USER
	
create-docker-network:
	docker network create controlapet

docker-clean:
	sudo docker system prune -af --volumes 

container-dump-db:
	sudo docker exec -it mysql bash -c "mysqldump -uroot -pSysControlaPet2018 Morumbichos < app/dump-de-testes-09-2018.sql && mysql -uroot -pSysControlaPet2018 Morumbichos -e 'source /app/dump-de-testes-09-2018.sql'"

container-createsuperuser:
	sudo docker exec -it sys_controla_pet bash -c "python manage.py createsuperuser"

container-drop-db:
	sudo docker exec -it mysql bash -c "mysqladmin -uroot -pSysControlaPet2018 drop Morumbichos"

container-create-db:
	sudo docker exec -it mysql bash -c "mysqladmin -uroot -pSysControlaPet2018 create Morumbichos"
