from letta_client import Letta  
import os  
from pathlib import Path

# TODO: replace with your token 
# my_token = "sk-let-ZGZmMzc5N2UtMmM3ZC00MTk4LTkyMzUtYjU1MTk4NDFkMzUwOjg5NTBkNWFmLTIxNDgtNDJlMS04NDYyLTNkZWM2ZTgzZTViOQ==" 
# client = Letta(base_url="https://app.letta.com/", token=my_token)

client = Letta(base_url="http://localhost:8283")

# создали client через ui создания агента
sources = client.sources.list()

test_source_id = client.sources.retrieve_by_name(
    source_name="test-texts",
)

# загружаем файлы из папки
test_texts_dir = Path("test-texts")  
for file_path in test_texts_dir.iterdir():
    with open(file_path, "rb") as f:
        job_a = client.sources.files.upload(source_id=test_source_id, file=f)
        print(f"Загружен файл:", file_path.name)
