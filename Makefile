docker-clean:
    sudo docker system prune -af --volumes

container-dump-db:
    sudo docker exec -it mysql bash -c "mysqldump -uroot -pSysControlaPet2018 Morumbichos < app/dump-de-testes-08-2018.sql && mysql -uroot -pSysControlaPet2018 Morumbichos -e 'source /app/dump-de-testes-08-2018.sql'"

container-createsuperuser:
    sudo docker exec -it app bash -c "python manage.py createsuperuser"

container-drop-db:
    mysqladmin -uroot -pSysControlaPet2018 drop Morumbichos

