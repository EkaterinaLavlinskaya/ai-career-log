import json
from datetime import datetime
import os

LOG_FILE = "data/interactions.jsonl"

def log_interaction(topic, note="", update_state=None):
    """
    Добавляет запись в лог.
    
    topic: тема (например, "project", "application", "test")
    note: текстовое примечание
    update_state: словарь с обновлёнными метриками (если меняются)
    """
    # Базовая запись
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "topic": topic,
        "note": note
    }
    
    # Если переданы новые метрики — добавляем
    if update_state:
        entry.update(update_state)
    
    # Создаём папку, если нет
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    # Добавляем запись
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    
    print(f"✅ Запись добавлена: {entry['timestamp']} — {topic}")

# Примеры использования:
if __name__ == "__main__":
    # Когда сделала новый проект
    # log_interaction("project", "Завершила проект по трансформеру", {"projects": 10})
    
    # Когда откликнулась на вакансию
    # log_interaction("application", "Отклик в Яндекс", {"applications": 8})
    
    # Когда получила результат
    # log_interaction("test_result", "Тест в Сбере пройден", {"tests_passed": 1})
    
    print("Скрипт готов. Раскомментируй нужную строку и запусти.")
