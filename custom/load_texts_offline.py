from letta_client import Letta  
import os  
from pathlib import Path
import httpx  
from letta.log import get_logger  

logger = get_logger(__name__)  

# TODO: replace with your token 
my_token = "sk-let-ZGZmMzc5N2UtMmM3ZC00MTk4LTkyMzUtYjU1MTk4NDFkMzUwOjg5NTBkNWFmLTIxNDgtNDJlMS04NDYyLTNkZWM2ZTgzZTViOQ==" 

# TODO: replace with your token 
# my_token = "sk-let-ZGZmMzc5N2UtMmM3ZC00MTk4LTkyMzUtYjU1MTk4NDFkMzUwOjg5NTBkNWFmLTIxNDgtNDJlMS04NDYyLTNkZWM2ZTgzZTViOQ==" 
# client = Letta(base_url="https://app.letta.com/", token=my_token)

# client = Letta(base_url="http://localhost:8283")


offline_client = Letta(  
    base_url="http://localhost:8283",  
    # base_url="https://app.letta.com/",
    # token=my_token,
    httpx_client=httpx.Client(  
        timeout=httpx.Timeout(  
            connect=30.0,  # Connection timeout  
            read=300.0,    # Read timeout (5 minutes)  
            write=60.0,    # Write timeout  
            pool=30.0      # Pool timeout  
        )  
    )  
)
# создали client через ui создания агента
sources = offline_client.sources.list()

test_source_id = offline_client.sources.retrieve_by_name(
    
    # source_name="orthodox-texts", # online
    # source_name="test-texts",
    source_name="31-05-25-orthodox-texts-offline-v3",
)

# загружаем файлы из папки
test_texts_dir = Path("svyatye-books")  
for file_path in test_texts_dir.iterdir():
    with open(file_path, "rb") as f:
        try:
            job_a = offline_client.sources.files.upload(source_id=test_source_id, file=f)
            logger.error(f"UPLOAD SUCCESS: {file_path.name}")  
            logger.error(f"UPLOAD SUCCESS: {file_path.name}")  
            logger.error(f"UPLOAD SUCCESS: {file_path.name}")  

            print(f"Загружен файл:", file_path.name)
        except Exception as e:
            logger.error(f"FILE OFFLINE-UPLOAD ERROR: {file_path.name}: {e}")  

            print("ОШИБКА ЗАГРУЗКИ ФАЙЛА ОФЛАЙН:")
            print("ОШИБКА ЗАГРУЗКИ ФАЙЛА ОФЛАЙН:")
            print("ОШИБКА ЗАГРУЗКИ ФАЙЛА ОФЛАЙН:")
            print(e)
            continue
