# Scraping
### В проекте использованы:
    * Django-3.2.2 
    * DRF
    * Bootstrap
    * Html
    * CSS
    * JS
    * Selenium
    * Celery / Redis
    * Sqlite3
 ### Приложение состоит из двух основных частей:
  * webapp - тут реализована логика для извлечения данных с сайта и модели для работы с базой:  
  * api-v1 - api для возвращения JSON данных. 

 ## Точка входа для сбора данных с сайта:
 * http://localhost:8000
 ## Точка входа для API:
 ### Получение списка компаний с данными:
 * http://localhost:8000/api-v1/company/
 ### Получение данных для конкретной компании (в данных json всех компаний есть url на получене данных отдельной компании):
 * http://localhost:8000/api-v1/company/(id компании)

 ----------------------------------------------------

# Установка.
 1. Cклонировать проект с GitHub:
 2. * $ git clone https://github.com/Illarionov81/Scraping.git
 3. Cоздайте виртуальное окружение:
   * ```$ cd Scraping/```
   * ```Scraping$ python3 -m venv venv```
 4. Активируйте его:
   * ```Scraping$ . venv/bin/activate```
 5. Устанавите окружение:
   * ```(venv)Scraping$ pip install -r requirements.txt```
 6. Проведите Мигрирацию БД:
   * ```Scraping$ cd source/```
   * ```(venv)Scraping/source$ python manage.py migrate```
 7. Для работы Selenium установить драйвер. 
   Ссылки на драйвера для  браузеров есть в документации по установке Selenium: https://selenium-python.readthedocs.io/installation.html.
   В корневом каталоге пакета проекта - sourse, содержится драйвер для версии браузера chrome 90.0.4430.
 7. Для запуска redis можно использовать docer:
   * ```docker run -p 6379:6379 --name some-redis -d redis```
 8. Для запуска celery - В терминале, с активным экземпляром виртуальной среды Python, установленным ранее, в корневом каталоге пакета проекта
   (тот же, что содержит модуль manage.py), запустить программу celery:
   * ```celery -A main worker --loglevel=info```
 9. Запустить сервер:
   * ```./manage.py runserver```
