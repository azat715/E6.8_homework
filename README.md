Сервис должен по GET запросу с параметром k возвращать k-ое число Фибоначчи. Необходимо реализовать кеширование, то есть, если число уже было запрошено, результат должен браться из кеша, а не пересчитываться.

Кеширование необходимо реализовать с помощью memcached (или redis), фреймворк для веб-сервиса используйте на ваше усмотрение, однако для такого небольшого проекта брать Django скорее перебор.

Приложение должно запускаться в Docker. Код приложения должен быть выложен на github, вместе с файлами Dockerfile и docker-compose.yml. В репозитории в README.md вам нужно поместить инструкцию по запуску приложения.

Дополнительно можно задеплоить это приложение в облачный сервис, например, Яндекс.Облако или mail.ru cloud solutions.

#### Запуск
```
sudo docker-compose up --build
```

#### Использование 
```
http GET 'http://localhost:8000/fib/?k=55'
```

#### Тесты
```
make test
```

#### Ошибки
при сохранение в redis тип становится str, а должен быть int


#### TODO
добавить проверку кеширование в test_app.py