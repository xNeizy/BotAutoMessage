![shapka](https://github.com/xNeizy/BotAutoMessage/assets/89652352/324c46cd-55e2-42f6-ba89-2138267b8537)
# BotAutoMessage🤖

⚡ | __Нужно предупредить о миграции канала в другое место?__

Тогда, Данный бот вам поможет ***предупредить*** людей, о том, что канал устарел и скинет указания!
___

## Установка | Installation

Установите [Python 3.11](https://www.python.org/downloads/release/python-3110/)
```python
https://www.python.org/downloads/release/python-3110/
```

Установите все нужные библиотеки
```
pip install -r requarements.txt
```
**Готово!**
### 🚀 Запуск | Launch
___
Откройте корневую папку и найдите файл ***config.py***
### 1 шаг/step
1. Откройте файл config.py
  
2. В строчку token="" вставьте токен бота, который вы получили от BotFather
```python
config.py

token = "" # token here
```
### 2 шаг/step
1. Откройте корневую в папку с файлом ***main.py***
2. Откройте консоль и перейдите в корневую папку, введите: 
~~~
py main.py
~~~
Если в консоли отобразилась следующая строчка:
> INFO:aiogram.dispatcher:Run polling for bot ...

***Тогда все хорошо и бот запустился!***

### 📝Изменение текста | Text editing
___
Изменять текст можно прямо в коде, а именно в ***строчке 15***:
```python
main.py
...

await message.answer(f"⚡@{message.from_user.username}, мы переехали в новый канал: @channel\n по этому отменяй подписку от этого канала и подписывайся на новый!")
```

Все что находится в ковычках "" вы можете спокойно изменять под свой вкус и цвет.
В данной строчке используется имено юзернейм человека, который написал сообщение, а не его имя:

![Screenshot_1](https://github.com/xNeizy/BotAutoMessage/assets/89652352/f08f1d86-f1d8-405a-bb51-9be12c095922)

Вот пара примеров, на что вы можете заменить username:
```python
message.from_user.id - уникальный идентефикатор человека(айди)
```

```python
message.from_user.firstname - имя человека
```
