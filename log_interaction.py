import json
from datetime import datetime
import os
import sys

LOG_FILE = "data/interactions.jsonl"

def get_last_state():
    """Читает последнюю запись из лога и возвращает её счётчики"""
    if not os.path.exists(LOG_FILE):
        # Если файла нет — начальные значения
        return {
            "projects": 0,
            "certificates": 0,
            "days_continuous": 0,
            "applications": 0,
            "positive_responses": 0,
            "tests": 0
        }
    
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if not lines:
            return {
                "projects": 0,
                "certificates": 0,
                "days_continuous": 0,
                "applications": 0,
                "positive_responses": 0,
                "tests": 0
            }
        last_line = lines[-1].strip()
        last = json.loads(last_line)
        return {
            "projects": last.get("projects", 0),
            "certificates": last.get("certificates", 0),
            "days_continuous": last.get("days_continuous", 0),
            "applications": last.get("applications", 0),
            "positive_responses": last.get("positive_responses", 0),
            "tests": last.get("tests", 0)
        }

def log_interaction(topic, note="", increment=None):
    """
    Добавляет запись в лог, автоматически обновляя счётчики.
    
    topic: тема (например, "project", "application", "test")
    note: текстовое примечание
    increment: словарь с тем, что увеличиваем (например, {"projects": 1, "applications": 1})
    """
    # Берём текущее состояние
    state = get_last_state()
    
    # Увеличиваем счётчики
    if increment:
        for key, val in increment.items():
            state[key] = state.get(key, 0) + val
    
    # Базовая запись
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "topic": topic,
        "note": note,
        "projects": state["projects"],
        "certificates": state["certificates"],
        "days_continuous": state["days_continuous"],
        "applications": state["applications"],
        "positive_responses": state["positive_responses"],
        "tests": state["tests"]
    }
    
    # Создаём папку, если нет
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    # Добавляем запись
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    
    print(f"✅ Запись добавлена: {entry['timestamp']} — {topic}")
    print(f"   Теперь: projects={state['projects']}, applications={state['applications']}, tests={state['tests']}")
    return entry

def print_help():
    print("""
📋 ИСПОЛЬЗОВАНИЕ:
    python log_interaction.py project "название проекта"         # новый проект
    python log_interaction.py apply "куда откликнулась"         # новый отклик
    python log_interaction.py test "какой тест"                 # новый тест
    python log_interaction.py certificate "название сертификата" # новый сертификат
    python log_interaction.py day                                # новый день непрерывного обучения
    python log_interaction.py positive "комментарий"             # положительный ответ
    python log_interaction.py custom "тема" "примечание" --inc projects=1 applications=1  # своё
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)
    
    command = sys.argv[1]
    note = sys.argv[2] if len(sys.argv) > 2 else ""
    
    if command == "project":
        log_interaction("project", note, {"projects": 1})
    elif command == "apply":
        log_interaction("application", note, {"applications": 1})
    elif command == "test":
        log_interaction("test", note, {"tests": 1})
    elif command == "certificate":
        log_interaction("certificate", note, {"certificates": 1})
    elif command == "day":
        log_interaction("daily", "очередной день", {"days_continuous": 1})
    elif command == "positive":
        log_interaction("positive_response", note, {"positive_responses": 1})
    elif command == "custom":
        # Парсим дополнительные аргументы вида --inc projects=1 applications=1
        increment = {}
        for i in range(3, len(sys.argv)):
            if sys.argv[i].startswith("--inc"):
                for j in range(i+1, len(sys.argv)):
                    if "=" in sys.argv[j]:
                        key, val = sys.argv[j].split("=")
                        increment[key] = int(val)
        log_interaction(note, sys.argv[2] if len(sys.argv) > 2 else "", increment)
    else:
        print(f"❌ Неизвестная команда: {command}")
        print_help()
        sys.exit(1)
