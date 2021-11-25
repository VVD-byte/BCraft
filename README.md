# BCraft

## Развертка
```docker-compose build```  
```docker-compose up```

## Документация api
```http://0.0.0.0:8000/api/docs/```

## Методы api
### Cоздание записи о статистике
#### Url
```http://0.0.0.0:8000/api/statistics/create```
#### Method
POST
#### Параметры
```
date - дата события
views - количество показов
clicks - количество кликов
cost - стоимость кликов (в рублях с точностью до копеек)
```
  
  
### Получение статистики
#### Url
```http://0.0.0.0:8000/api/statistics/list```
#### Method
GET
#### Query Params
```
from - дата начала периода (включительно)
to - дата окончания периода (включительно)
```
### Удаление всех данных
#### Url
```http://0.0.0.0:8000/api/statistics/drop```
#### Method
DELETE