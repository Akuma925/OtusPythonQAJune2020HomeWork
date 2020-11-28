# Test OpenCart

Реализация автоматических тестов OpenCart
с использование паттерна PageObject
Можно использовать как selenoid так и локально
работает ан Chrome, FF, Opera
Проекте поддерживаются allure отчеты

##Page Object
How To config env-t for deploy this project
```bash
python3 -m venv env && 
source env/bin/activate && 
pip3 install -U pip3 && 
pip3 install -r requirements.txt

```
##Опции для запуска
"--browser", "-B" Выбор браузера нужно передать название chrome firefox или opera
"--url", "-U" Указать точку входа на которой работает opencart
"--run", "-R" Выбор способа запуска локально или через selenoid (local/remote)
