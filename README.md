# Simple Trivia Getter

Bewise.ai

## Установка

```sh
git clone https://github.com/staffluck/bewise_test.git
nano app/.env ( по шаблону app/.env.template, при изменении данных - изменить docker-compose.yaml )
docker-compose up -d --build
```

## Основной запрос
```sh
[POST] http://127.0.0.1:5001/trivia/
    body:
        {
            "questions_num": <int>
        }
```

