from letta_client import Letta  
from letta_client import Letta, MessageCreate, TextContent

client = Letta(base_url="http://localhost:8283")  
# client = Letta(base_url="https://app.letta.com:8283")  
online_client = Letta(  
    # base_url="http://localhost:8283",  
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
for agent in client.agents.list():
    print(agent.name)
    print("ID:", agent.id)

# messages=[
#     MessageCreate(
#         role="user",
#         content=[
#             TextContent(
#                 text="Привет, не помнишь, кто написал слово о Вознесении?",
#             )
#         ],
#     )
# ],
# print(messages)

response = client.agents.messages.create(
    agent_id=agent.id,
    messages=[
        MessageCreate(
            role="user",
            content=[
                TextContent(
                    text="Почему в христианстве животных убивать можно, а человека нельзя? Search archival.",
                )
            ],
        )
    ],
)
print(response)


# response = client.agents.messages.create_stream(
#     agent_id=agent.id,
#     messages=[
#         MessageCreate(
#             role="user",
#             content=[
#                 TextContent(
#                     text="Привет, не помнишь, кто написал слово о Вознесении?",
#                 )
#             ],
#         )
#     ],
# )

# print(response)