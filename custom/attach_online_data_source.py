from letta_client import Letta  
import httpx  
import requests  

def add_online_source_to_agent():  
    # Создаем клиент  
    my_token = "sk-let-ZGZmMzc5N2UtMmM3ZC00MTk4LTkyMzUtYjU1MTk4NDFkMzUwOjg5NTBkNWFmLTIxNDgtNDJlMS04NDYyLTNkZWM2ZTgzZTViOQ==" 

      
    offline_client = Letta(
        base_url="http://localhost:8283",  
        httpx_client=httpx.Client(  
            timeout=httpx.Timeout(  
                connect=30.0,  # Connection timeout  
                read=300.0,    # Read timeout (5 minutes)  
                write=60.0,    # Write timeout  
                pool=30.0      # Pool timeout  
            )  
        )  
    )
    
    online_client = Letta(
        base_url="https://app.letta.com/",
        token=my_token,
        httpx_client=httpx.Client(  
            timeout=httpx.Timeout(  
                connect=60.0,  # Connection timeout  
                read=300.0,    # Read timeout (5 minutes)  
                write=60.0,    # Write timeout  
                pool=60.0      # Pool timeout  
            )  
        )  
    )
    test_source_id = online_client.sources.retrieve_by_name(
        source_name="01-06-25-orthodox-texts-online-v3",
    )

    online_client.agents.sources.attach(
        agent_id="agent-e5ae82b3-83e9-4fc0-b822-98a45c055c70",
        # agent_id="agent-9f480f52-1c0d-4198-b026-18819a9af232",
        source_id=test_source_id
    )
    print(test_source_id)

    # headers = {
    #     # "accept": "application/json",  
    #     "Authorization": f"Bearer {my_token}",  # если используете токен  
    #     # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    #     "Content-Type": "application/json"  
    # }  
    # agent_id = "agent-9f480f52-1c0d-4198-b026-18819a9af232"  # Replace with your agent_id

    # response = requests.get(  
    #     f"http://localhost:8283/api/v1/agents/",  
    #     headers=headers,
    #     params={"agent_id": agent_id}  # This parameter is also required  
    # )
# Прямой HTTP вызов  
    # response = requests.patch(  
    #     f"http://localhost:8283/api/v1/agents/agent-9f480f52-1c0d-4198-b026-18819a9af232/sources/attach/{test_source_id}",  
    #     headers=headers,
    #     params={"agent_id": agent_id}  # This parameter is also required  
    # )
    # print(response.status_code)  
    # print(response.text)  

    # agent_state = offline_client.attach_source(
    #     agent_id=offline_client,  
    #     source_id=test_source_id  
    # )
    # 
    # offline_client.agents.sources.attach(agent_id= "agent-9f480f52-1c0d-4198-b026-18819a9af232", source_id=source.id)
  




add_online_source_to_agent()
    # Подключаем источник к агенту  
#     agent_state = offline_client.attach_source(  
#         agent_id=agent_id,  
#         source_id=source.id  
#     )  
      
#     print(f"Источник {source_name} успешно подключен к агенту {agent_id}")  
#     return agent_state  
  
# # Использование  
# agent_state = add_online_source_to_agent(  
#     agent_id="your_agent_id",  
#     source_name="my_knowledge_base",  
#     file_path="documents/knowledge.pdf"  
# )

# def add_online_source_to_agent(agent_id: str, source_name: str, file_path: str):  
#     # Создаем клиент  
#     client = create_client()  
      
#     # Создаем источник данных  
#     source = client.create_source(  
#         name=source_name,  
#         embedding_config=EmbeddingConfig.default_config(provider="openai")  
#     )  
      
#     # Загружаем файл в источник  
#     job = client.load_file_to_source(  
#         filename=file_path,  
#         source_id=source.id,  
#         blocking=True  
#     )  
      
#     # Подключаем источник к агенту  
#     agent_state = client.attach_source(  
#         agent_id=agent_id,  
#         source_id=source.id  
#     )  
      
#     print(f"Источник {source_name} успешно подключен к агенту {agent_id}")  
#     return agent_state  
  
# # Использование  
# agent_state = add_online_source_to_agent(  
#     agent_id="your_agent_id",  
#     source_name="my_knowledge_base",  
#     file_path="documents/knowledge.pdf"  
# )

# add_online_source_to_agent(agent_id="9f480f52-1c0d-4198-b026-18819a9af232", source_name="my_knowledge_base", file_path="documents/knowledge.pdf")
