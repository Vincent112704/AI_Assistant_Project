Create a README.md documentation file for my school assistant agent. Here are the specifications:

1. Functional requirements:
   1. The system should be able to understand and communicate with the user through Telegram.
   2. The system should be able to listen for event messages
   3. The system should be able to send the appropriate files back to  the user
   4. The  system should be able to access external tools (e.g., google sheets, docs, notion, etc.)
2. Non-functional requirements:
   1. The system should be scalable (i.e., I can add more agents in the future)
   2. The system should be maintainable
Here are the tech stack I plan to use:

1. frontend - React
2. Backend - FastAPI
3. DB - firebase
4. LLM - OpenAI
5. CI/CD 
   1. Docker
   2. Git/Github
6. Redis

I will be using EDA (Event-Driven Architecture) for this project. 


For your reference this is a high-level overview of the system:
User input -> Telegram Input handler service (producer) -> Broker -> Agent (consumer) -> Response Service -> User

Strictly follow what is in this prompt. You are not allowed to:

1. Add your own interpretation and design
2. Modify any of the specifications