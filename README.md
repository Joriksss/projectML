<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8" />
    <title>Who are you? - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
        }
        h1, h2 {
            color: #2c3e50;
        }
        code {
            background-color: #eee;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: Consolas, monospace;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }
        hr {
            margin: 30px 0;
        }
    </style>
</head>
<body>
    <h1>Who are you?</h1>

    <p>Проект <strong>Who are you?</strong> предназначен для того, чтобы определить, кто вы из сериала <em>The Boys</em> по фотографии. На текущем этапе доступна работа с фотографиями, в будущем планируется добавить возможность определения персонажа по ответам на вопросы.</p>

    <hr />

    <h2>О проекте</h2>
    <ul>
        <li>Веб-приложение с фронтендом на чистом HTML и бэкендом на Flask.</li>
        <li>Сверточная нейронная сеть (CNN) на базе Keras для классификации фотографий.</li>
        <li>Логирование запросов и результатов работы модели.</li>
        <li>Скрипт для проверки логов.</li>
    </ul>

    <hr />

    <h2>Используемые технологии</h2>
    <ul>
        <li>Python 3</li>
        <li>Flask</li>
        <li>Keras (TensorFlow backend)</li>
        <li>HTML (фронтенд)</li>
    </ul>

    <hr />

    <h2>Структура проекта</h2>
    <ul>
        <li><code>app.py</code> — основной сервер Flask, фронтенд и API (порт 3000)</li>
        <li><code>modelka.py</code> — загрузка и запуск модели, логирование</li>
        <li><code>check.py</code> — проверка и анализ логов</li>
    </ul>

    <hr />

    <h2>Запуск проекта локально</h2>
    <ol>
        <li>Клонируйте репозиторий:
            <pre><code>git clone &lt;URL_репозитория&gt;
cd &lt;название_папки&gt;</code></pre>
        </li>
        <li>Создайте и активируйте виртуальное окружение, затем установите зависимости:
            <pre><code>python3 -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt</code></pre>
        </li>
        <li>Запустите сервер:
            <pre><code>python3 app.py</code></pre>
        </li>
        <li>Откройте браузер по адресу:
            <p><code>http://localhost:3000</code></p>
        </li>
        <li>Загрузите фотографию и узнайте, кто вы из сериала <em>The Boys</em>!</li>
    </ol>

    <hr />

    <h2>Работа с моделью</h2>
    <p>Модель принимает фотографии на вход и возвращает результат классификации, который выводится на фронтенде. Все запросы и результаты логируются.</p>

    <hr />

    <h2>Проверка логов</h2>
    <p>Для проверки логов используйте команду:</p>
    <pre><code>python3 check.py</code></pre>

    <hr />

    <h2>Планы по развитию</h2>
    <ul>
        <li>Добавить определение персонажа по ответам на вопросы.</li>
        <li>Улучшить интерфейс фронтенда.</li>
        <li>Оптимизировать и дообучить модель.</li>
    </ul>

    <hr />

    <h2>Лицензия</h2>
    <p>Проект доступен под лицензией MIT.</p>

    <p>Если есть вопросы или предложения — пишите!</p>
</body>
</html>
