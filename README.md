# 🤖 AI Career Log — Отслеживание карьерного роста в Data Science

**Репозиторий для сбора, анализа и визуализации данных о моём прогрессе в обучении и поиске работы в сфере ML/AI.**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EkaterinaLavlinskaya/ai-career-log/blob/main/ai_career_logger.ipynb)

---

## 📌 Зачем это?

Этот проект — **живой датасет** моего пути в Data Science. Здесь фиксируются:
- новые проекты
- отклики на вакансии
- тестовые задания
- сертификаты
- и другие события

Данные собираются автоматически, а дашборд показывает динамику и прогресс.

---

## 📊 Что отслеживается

| Метрика | Описание |
|---------|----------|
| `projects` | Количество завершённых проектов на GitHub |
| `certificates` | Сертификаты (Kaggle, Stepik и др.) |
| `applications` | Отклики на вакансии |
| `positive_responses` | Положительные ответы / приглашения |
| `tests` | Пройденные тестовые задания |
| `days_continuous` | Дней подряд без пропусков в обучении |

---

## 🗂️ Структура репозитория
ai-career-log/
├── README.md # этот файл
├── data/
│ └── interactions.jsonl # сырые данные (логи)
├── scripts/
│ └── log_parser.ipynb # анализ данных
├── viz/
│ └── dashboard.ipynb # дашборд с графиками
├── ai_career_logger.ipynb # ноутбук с функциями API
└── log_interaction.py # консольный скрипт для логирования

---

## ⚙️ Как добавлять новые записи

### 🔹 Через Python-скрипт (рекомендуется)

```bash
python log_interaction.py project "Название проекта"
python log_interaction.py apply "Компания / вакансия"
python log_interaction.py test "Описание теста"
python log_interaction.py certificate "Название курса"
python log_interaction.py day
python log_interaction.py positive "Комментарий"

🔹 Через ноутбук ai_career_logger.ipynb
открываешь в Colab

запускаешь ячейку с add_record

запись автоматически уходит на GitHub

📈 Дашборд
Запусти viz/dashboard.ipynb в Colab или локально, чтобы увидеть:

📈 рост проектов во времени

📬 динамику откликов

✅ сравнение положительных ответов и тестов

🔮 прогноз достижения целей

https://colab.research.google.com/assets/colab-badge.svg

🧠 Как это работает
Данные хранятся в формате JSONL (data/interactions.jsonl)

Каждая запись содержит временную метку и текущие значения метрик

Скрипты и ноутбуки читают эти данные, строят графики и прогнозы

GitHub API используется для автоматического обновления файла

🚀 Планы по развитию
добавить метрику interviews (количество собеседований)

построить график «воронки откликов»

сравнивать с целевыми показателями

автоматические уведомления при достижении целей

👤 Автор
Екатерина Лавлинская
Junior Data Scientist / ML Engineer
GitHub: @EkaterinaLavlinskaya

Проект создан для системного отслеживания прогресса и как демонстрация навыков работы с данными, автоматизацией и визуализацией.

📄 Лицензия
MIT — свободно используйте, адаптируйте, улучшайте.
      
