## Тестовый практический проект.
### Краткая информация: 
    Бакенд для интернет-магазина

### Для начала работы и тестирования проекта в "продакшн-режиме" понадобятся:
 1. Настроить виртуальное окружение
 2. Установить Docker 
    
####  Для установки, запуска и настроек сервиса необходимо открыть терминал в директории проекта выполнить:
    
    docker-compose -f docker-compose.prod.yaml 
#### Для тестирования без Prometheus и Grafana вместо команды сверху выполните
    docker-compose -f docker-compose.yaml 
    
###### Для вывода логов можно ввести команду: 
    docker-compose -f docker-compose.prod.yaml logs

#### Далее для применения миграций в терминале:
    docker-compose exec django_backend python3 manage.py migrate

#### Создайте суперпользователя:
    docker-compose exec django_backend python3 manage.py createsuperuser

#### Для полноценного тестирования необходимо настроить планировщик задач Celery. Выполните команду:
     docker-compose exec django_backend celery -A online_store worker -l info

Проект запущен и готов к работе.

    





