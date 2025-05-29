from letta_client import Letta  
from letta_client import Letta, MessageCreate, TextContent

client = Letta(base_url="http://localhost:8283")  

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
                    text="Найди в архивной памяти информацию о Диадохе Блаженном",
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