
# URL Shortner

URL Shortner - это приложение для сокращения ссылок. При введение ссылки выдается короткий варинт имени ссылки который можно кастомизировать под свое название.



## Deployment

Установка на локальном компьютере

1. Клонируйте репозиторий:

```bash
  git clone git@github.com:Talantino/python-4-url-shortener.git
```
2. Установите и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate  - для Windows
source venv/bin/activate - для Linux
```
3. Установите зависимости:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Перейдите в папку url-shortener и выполните миграции:
```bash
cd url-shortener
python manage.py migrate
```
5. Создайте суперпользователя:
```bash
python manage.py 
```
6. Запустите проект:
```bash
python manage.py runserver
```

## Технологии:

![Alt text for Logo1](https://camo.githubusercontent.com/0562f16a4ae7e35dae6087bf8b7805fb7e664a9e7e20ae6d163d94e56b94f32d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534)
![Alt text for Logo2](https://camo.githubusercontent.com/81d983188c1409436c9b1aef31b601b63bfa3c3d55ec681d07df4cdcb64fa446/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f444a414e474f2d524553542d6666313730393f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d776869746526636f6c6f723d666631373039266c6162656c436f6c6f723d67726179) 

![Alt text for Logo2](https://github.com/yurijserrano/Github-Profile-Readme-Logos/blob/master/databases/postgresql.svg) 
