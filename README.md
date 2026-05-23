# School Assistant Agent


A scalable, event-driven assistant system that processes user requests through Telegram and leverages AI to provide intelligent responses and file management.

## Table of Contents

1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Functional Requirements](#functional-requirements)
4. [Non-Functional Requirements](#non-functional-requirements)
5. [Tech Stack](#tech-stack)
6. [Installation](#installation)
7. [Configuration](#configuration)
8. [Usage](#usage)
9. [Project Structure](#project-structure)
10. [Contributing](#contributing)
11. [License](#license)

## Overview

The Assistant Agent is an intelligent system designed to assist users through Telegram. It processes user inputs, understands context through AI, accesses external tools and resources, and sends appropriate responses and files back to users. The system is built on an Event-Driven Architecture (EDA) to ensure scalability and maintainability.

## System Architecture

The system follows an event-driven architecture with the following flow:

```
User Input → Telegram Input Handler Service (Producer) 
  → Broker → Agent (Consumer) → Response Service → User
```

### Architecture Components

- **Telegram Input Handler Service**: Receives messages from users via Telegram and acts as a producer, sending events to the broker
- **Broker**: Message queue system that decouples services and manages event distribution
- **Agent**: Consumer service that processes events, executes business logic, and communicates with external tools
- **Response Service**: Handles sending responses and files back to users through Telegram
- **LLM Integration**: OpenAI integration for intelligent request processing and understanding

## Functional Requirements

### 1. Telegram Communication
- The system shall understand and communicate with users through Telegram messaging platform
- Users can send text messages that are processed by the assistant

### 2. Event Message Listening
- The system shall listen for event messages from the Telegram Input Handler Service
- Events are routed through a message broker for asynchronous processing

### 3. File Management
- The system shall send appropriate files back to the user
- Files are retrieved from external sources and delivered through Telegram

### 4. External Tool Integration
- The system shall access external tools and services including:
  - Google Sheets
  - Google Docs
  - Notion
  - Other configurable external tools

## Non-Functional Requirements

### 1. Scalability
- The system architecture supports adding more agents in the future
- Event-driven design allows horizontal scaling of consumer services
- Multiple agent instances can process events concurrently from the message broker

### 2. Maintainability
- Clean separation of concerns through microservice architecture
- Modular design facilitates updates and feature additions
- Comprehensive documentation and code structure for ease of maintenance

## Tech Stack

### Backend
- **FastAPI**: High-performance web framework for building APIs and services

### Database
- **Firebase**: Cloud database for storing user data, agent configurations, and system state

### AI/LLM
- **OpenAI**: Language model for understanding user requests and generating intelligent responses

### Message Broker & Caching
- **Redis**: Message broker for event-driven architecture and caching layer

### DevOps & CI/CD
- **Docker**: Containerization for consistent deployment across environments
- **Git/GitHub**: Version control and collaboration platform

## Installation

### Prerequisites
- Python 3.8+
- Docker and Docker Compose
- Git
- Redis
- Firebase account

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd personal-assistant-agent
```

2. Build docker compose
```bash
docker-compose up --build #for initial set up
```

if you an image already exists locally in your docker you can simply do:
```bash
docker-compose up
```


### Docker Setup

1. Build and run all services with Docker Compose:
```bash
docker-compose up --build
```

2. Services will be accessible at:
   - Backend API: `http://localhost:8000`
   - Redis: `localhost:6379`

## Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

#### Backend Configuration
```
# OpenAI
OPENAI_API_KEY=<your-openai-api-key>

# Telegram
TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>

# Firebase
FIREBASE_PROJECT_ID=<your-firebase-project-id>
FIREBASE_PRIVATE_KEY=<your-firebase-private-key>
FIREBASE_CLIENT_EMAIL=<your-firebase-client-email>

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# External Tools (configure as needed)
GOOGLE_SHEETS_API_KEY=<your-google-sheets-api-key>
GOOGLE_DOCS_API_KEY=<your-google-docs-api-key>
NOTION_API_KEY=<your-notion-api-key>
```


### Firebase Setup

1. Create a Firebase project at [Firebase Console](https://console.firebase.google.com)
2. Generate a service account key:
   - Go to Project Settings → Service Accounts
   - Click "Generate New Private Key"
   - Save the JSON file and extract credentials for environment variables

### Telegram Bot Setup

1. Create a Telegram bot via [BotFather](https://t.me/botfather)
2. Copy the bot token to your `.env` file
3. Configure webhook or polling settings as needed

### External Tools Configuration

Configure API keys for Google Sheets, Google Docs, Notion, or other external tools in the `.env` file and in the agent configuration.

## Usage

### Starting the Application

#### Development Mode
```bash
# Start all services with Docker Compose
docker-compose up


```

#### Production Mode
```bash
# Build and run with Docker Compose
docker-compose -f docker-compose.prod.yml up --build
```

### Interacting with the Agent

1. Open Telegram and search for your bot
2. Send a message to the bot
3. The bot will:
   - Receive your message through the Telegram Input Handler Service
   - Process it through the agent with AI assistance
   - Retrieve necessary files from external tools if needed
   - Send appropriate responses and files back to you

### Adding New Agents

To add more agents in the future:

1. Create a new agent service following the existing agent pattern
2. Configure the agent in the message broker configuration
3. Ensure the agent subscribes to the appropriate event topics
4. Deploy using Docker

## Project Structure


```
personal_assistant_agent/
├── .vscode/
│   └── launch.json #Configs for debugger
├── src/
│   ├── agents/                                 #file directory for all agents
│   │   ├── base_agent.py                       #Class that all agents inherit from
│   │   └── simple_agent.py                     #Agent used for simple tasks
│   ├── firebase/                               #file directory for firebase configurations
│   │   └── firebase.py                          
│   ├── services/                               #apps core business logics
│   │   ├── agent_executor_service.py           #runs agents 
│   │   ├── document_generator_service.py       #creates docx file
│   │   ├── docx_to_pdf_service.py              #converts docx file to pdf
│   │   ├── query_classifier_service.py         #classifies query to determine which agent to use
│   │   ├── telegram_input_handler_service.py   #handles telegram input (producer)
│   │   └── telegram_push_message_service.py    #sends response back to telegram
│   ├── tools/                                  #tools agents use directory
│   │   ├── create_docx_tool.py                 #tool used by agent to create a docx file
│   │   ├── registry.py                         #centralized directory for all the tools agent can use.
│   │   └── search_internet_tool.py             #tool for searching the internet
│   ├── utils/                                  #reusable helper function directory
│   │   └── preprocess_string.py                #cleans string 
│   └── main.py                                 #entrypoint of app
├── tmp/                                        #directory for storing document files generated by app
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml                              #dependencies of app
├── logs.txt                                    #documentation for problems dev has encountered and how dev solved it
└── notes.txt                                   #documentation for devs notes about the app
```

## Contributing

### Code Standards

- Follow PEP 8 for Python code
- Write clear, descriptive commit messages
- Include tests for new features

### Submitting Changes

1. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. Commit your changes:
```bash
git commit -am 'Add new feature'
```

3. Push to the branch:
```bash
git push origin feature/your-feature-name
```

4. Submit a pull request for review

## License

This project is licensed under the MIT License. See LICENSE file for details.

---

**Last Updated**: May 2026
