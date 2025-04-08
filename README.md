# Проект 7 спринта "Тестирование API сервиса Яндекс Самокат"

Документация: [qa-scooter.praktikum-services.ru/docs/]().

## 1. Тестирование ручки /api/v1/courier Создание курьера:
* Успешное создание пользователя при заполнении всех полей, код ответа 201 Created;
* Получение ошибки при создании дубликата карточки, код ответа 409 Сonflict; 
* Получение ошибки в ответе при пропуске обязательного поля, код ответа 400 Bad Request; 

## 2. Тестирование ручки /api/v1/courier/login Логин курьера в системе:
* Успешная аутентификации курьера при вводе корректного логина и пароля, код ответа 200 OK, id: [.....];
* Возникновение ошибки при пропуске поля логин и/или пароль для аутентификации, код ответа 400 Bad Request;
* Возникновение ошибки при вводе несуществующего логина и/или пароля в форму аутентификации, код ответа 404 Not Found;

## 3. Тестирование ручки /api/v1/orders Создание заказа:
* Успешное оформление заказа при выборе цвета самоката BLACK и/или GREY, код ответа 201 Created, track [.....]; 
* Успешное оформление заказа при пропуске поля с выбором цвета, код ответа 201 Created, track [.....]; 

## 4. Тестирование ручки /api/v1/orders Получение списка заказов:
* Успешное получение списка заказов без указания id курьера, код ответа 200 OK;
* Успешное получение списка заказов с указанием id курьера, код ответа 200 OK;
* Получение ошибки при запросе списка с несуществующим id курьера, код ответа 404 Not Found;