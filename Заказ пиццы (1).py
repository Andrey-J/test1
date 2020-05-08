{
  "meta": {
    "locale": "ru-RU",
    "timezone": "Europe/Moscow",
    "interfaces": {
      "screen": { },
      "account_linking": { }
    }
  },
  "request": {
    "command": "Закажи пиццу 'Четыре сыра' на Ленинградское шоссе 30 через 60 минут",
    "original_utterance": "закажи пиццу 'Четыре сыра' на Ленигнрадское шоссе, 30, через 60 минут",
    "type": "SimpleUtterance",
    "markup": {
      "dangerous_context": true
    },
    "payload": {},
    "nlu": {
      "tokens": [
        "закажи",
        "пиццу",
        "Четыре сыра",
        "на",
        "Ленинградское",
        "шоссе",
        "30",
        "через",
        "60",
        "минут"
      ],
      "entities": [
        {
          "tokens": {
            "start": 2,
            "end": 6
          },
          "type": "YANDEX.GEO",
          "value": {
            "house_number": "30",
            "street": "Ленинградское шоссе"
          }
        },
        {
          "tokens": {
            "start": 3,
            "end": 5
          },
          "type": "YANDEX.FIO",
          "value": {
            "first_name": "Ленинградское",
            "last_name": "шоссе"
          }
        },
        {
          "tokens": {
            "start": 5,
            "end": 6
          },
          "type": "YANDEX.NUMBER",
          "value": 16
        },
        {
          "tokens": {
            "start": 6,
            "end": 8
          },
          "type": "YANDEX.DATETIME",
          "value": {
            "day": 1,
            "day_is_relative": true
          }
        }
      ]
    }
  },
  "session": {
    "message_id": 0,
    "session_id": "",
    "skill_id": "",
    "user_id": "",
    "user": {
      "user_id": "",
      "access_token": ""
    },
    "application": {
      "application_id": ""
    },
    "new": true,
  },
  "version": "1.0"
}