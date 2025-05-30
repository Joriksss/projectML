
<h1>Who are you?</h1>

<p>Проект <strong>Who are you?</strong> позволяет определить, кто вы из сериала <em>The Boys</em> по фотографии. Сейчас работает только с фотографиями, в будущем планируется добавить ответы на вопросы.</p>

<hr>

<h2>О проекте</h2>
<ul>
  <li>Фронтенд на HTML</li>
  <li>Бэкенд на Flask</li>
  <li>Модель — сверточная нейронная сеть (CNN) на Keras</li>
  <li>Добавлено логирование запросов и результатов</li>
  <li>Скрипт для проверки логов</li>
</ul>

<hr>

<h2>Структура проекта</h2>
<ul>
  <li><code>app.py</code> — запуск сервера Flask (порт 3000)</li>
  <li><code>modelka.py</code> — работа с моделью и логированием (Порт 5000)</li>
  <li><code>check.py</code> — скрипт для проверки логов</li>
</ul>

<hr>

<h2>Запуск проекта</h2>
<ol>
  <li>Клонируйте репозиторий:<br>
    <pre><code>git clone &lt;https://github.com/Joriksss/projectML.git&gt;
cd &lt;ProjectML&gt;</code></pre>
  </li>
  <li>Создайте и активируйте виртуальное окружение, установите зависимости:<br>
    <pre><code>python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt</code></pre>
  </li>
  <li>Запустите сервер:<br>
    <pre><code>python3 app.py</code></pre>
  </li>
  <li>Откройте браузер по адресу <code>http://localhost:3000</code></li>
  <li>Загрузите фотографию и узнайте, кто вы из сериала <em>The Boys</em></li>
</ol>

<hr>

<h2>Проверка логов</h2>
<p>Для проверки логов используйте:</p>
<pre><code>python3 check.py</code></pre>

<hr>

<h2>Планы по развитию</h2>
<ul>
  <li>Добавить определение персонажа по ответам на вопросы</li>
  <li>Улучшить интерфейс фронтенда</li>
  <li>Оптимизировать и дообучить модель</li>
</ul>

<hr>

<h2>Лицензия</h2>
<p>Проект доступен под лицензией MIT.</p>

