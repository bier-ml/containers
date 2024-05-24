# HW2. Docker-compose

### Задача 
Создать docker-compose.yml из минимум трех сервисов


## Структура docker-compose

1. init-service
> Одноразовая служба инициализации с использованием простого образа busybox, ожидает готовности БД.
2. jupyterhub
> Основная служба jupyterhub, созданная Dockerfile_good из 1 лабы. Зависит от инита и от БД. Jupyterhub поднимается на 8000 порту. 
3. db 
> Служба базы данных PostgreSQL, используется конфиг из .env.

## Можно ли ограничивать ресурсы (например, память или CPU) для сервисов в docker-compose.yml? Если нет, то почему, если да, то как?
Да, в docker можно задать лимиты ресурсов для сервиса в разделе deploy:
```yaml
version: '3.8'

services:
  foo-service:
    deploy:
      resources:
        limits:
          cpus: '0.01'
          memory: 512M
```

## Как можно запустить только определенный сервис из docker-compose.yml, не запуская остальные?

Можно указать название нужного сервиса(-ов) в командах docker-compose up / docker-compose start. 

```bash
docker-compose up -d foo-service
```

