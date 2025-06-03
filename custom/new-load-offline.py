from letta_client import Letta    
import os    
from pathlib import Path  
import httpx    
import json  
import time  
from typing import Optional, Dict, List  
  
from letta.log import get_logger    
    
logger = get_logger(__name__)    
  
# Конфигурация  
STATE_FILE = "upload_state.json"  
MAX_RETRIES = 3  
  
def load_state() -> Dict:  
    """Загружает состояние загрузки"""  
    if Path(STATE_FILE).exists():  
        with open(STATE_FILE, 'r', encoding='utf-8') as f:  
            return json.load(f)  
    return {"uploaded_files": [], "failed_files": []}  
  
def save_state(state: Dict):  
    """Сохраняет состояние загрузки"""  
    with open(STATE_FILE, 'w', encoding='utf-8') as f:  
        json.dump(state, f, ensure_ascii=False, indent=2)  
  
def upload_file_with_retry(client, source_id: str, file_path: Path, max_retries: int = MAX_RETRIES) -> Optional[str]:  
    """Загружает файл с повторными попытками (упрощенная версия)"""  
    for attempt in range(max_retries):  
        try:  
            with open(file_path, "rb") as f:  
                print(f"Попытка {attempt + 1}: Загружается файл {file_path.name}")  
                job = client.sources.files.upload(source_id=source_id, file=f)  
                print(f"✅ Файл отправлен на загрузку: {file_path.name}")  
                return job.id  
                      
        except Exception as e:  
            logger.error(f"❌ Попытка {attempt + 1} неудачна для {file_path.name}: {e}")  
            if attempt == max_retries - 1:  
                logger.error(f"🚫 Все попытки исчерпаны для {file_path.name}")  
                return None  
            time.sleep(2 ** attempt)  
      
    return None
 
def main():  
    # Инициализация клиента  
    my_token = "sk-let-ZGZmMzc5N2UtMmM3ZC00MTk4LTkyMzUtYjU1MTk4NDFkMzUwOjg5NTBkNWFmLTIxNDgtNDJlMS04NDYyLTNkZWM2ZTgzZTViOQ=="  
      
    online_client = Letta(    
        base_url="http://localhost:8283",  
        # token=my_token,  
        httpx_client=httpx.Client(    
            timeout=httpx.Timeout(    
                connect=60.0,  
                read=300.0,  
                write=60.0,  
                pool=60.0        
            )    
        )    
    )  
  
    # Получаем источник данных  
    test_source_id = online_client.sources.retrieve_by_name(  
        source_name="test"  
    )  
  
    # Загружаем состояние  
    state = load_state()  
    uploaded_files = set(state["uploaded_files"])  
    failed_files = set(state["failed_files"])  
  
    # Получаем список файлов для загрузки  
    test_texts_dir = Path("svyatye-books-cleaned")  
    all_files = list(test_texts_dir.iterdir())  
      
    print(f"📁 Найдено файлов: {len(all_files)}")  
    print(f"✅ Уже загружено: {len(uploaded_files)}")  
    print(f"❌ Ранее неудачных: {len(failed_files)}")  
  
    # Загружаем файлы  
    for file_path in all_files:  
        if not file_path.is_file():  
            continue  
              
        file_name = file_path.name  
          
        # Пропускаем уже загруженные файлы  
        if file_name in uploaded_files:  
            print(f"⏭️  Пропускаем уже загруженный: {file_name}")  
            continue  
              
        # Пытаемся загрузить файл  
        job_id = upload_file_with_retry(online_client, test_source_id, file_path)  
          
        if job_id:  
            uploaded_files.add(file_name)  
            # Удаляем из неудачных, если был там  
            failed_files.discard(file_name)  
        else:  
            failed_files.add(file_name)  
          
        # Сохраняем состояние после каждого файла  
        state["uploaded_files"] = list(uploaded_files)  
        state["failed_files"] = list(failed_files)  
        save_state(state)  
          
        print(f"📊 Прогресс: {len(uploaded_files)}/{len(all_files)} загружено")  
  
    print(f"\n🎉 Загрузка завершена!")  
    print(f"✅ Успешно загружено: {len(uploaded_files)}")  
    print(f"❌ Неудачных загрузок: {len(failed_files)}")  
      
    if failed_files:  
        print(f"🔄 Неудачные файлы: {list(failed_files)}")  
  
if __name__ == "__main__":  
    main()
