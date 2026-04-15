# School Assistant Agent

A scalable, event-driven school assistant system that processes user requests through Telegram and leverages AI to provide intelligent responses and file management.

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

The School Assistant Agent is an intelligent system designed to assist users through Telegram. It processes user inputs, understands context through AI, accesses external tools and resources, and sends appropriate responses and files back to users. The system is built on an Event-Driven Architecture (EDA) to ensure scalability and maintainability.

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
- Node.js 14+
- Docker and Docker Compose
- Git
- Redis
- Firebase account

### Backend Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd school-assistant-agent
```

2. Navigate to the backend directory:
```bash
cd backend
```

3. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Configure environment variables (see [Configuration](#configuration))

6. Run the backend services:
```bash
python -m uvicorn main:app --reload
```


### Docker Setup

1. Build and run all services with Docker Compose:
```bash
docker-compose up --build
```

2. Services will be accessible at:
   - Frontend: `http://localhost:3000`
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

# FastAPI
FASTAPI_ENV=development
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000

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

# Or run services individually
# Terminal 1: Start Redis
redis-server

# Terminal 2: Start Backend
cd backend && python -m uvicorn main:app --reload

# Terminal 3: Start Frontend
cd frontend && npm start
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
school-assistant-agent/
├── backend/
│   ├── services/
│   │   ├── telegram_handler.py      # Telegram Input Handler (Producer)
│   │   ├── agent.py                 # Agent Service (Consumer)
│   │   ├── response_service.py       # Response Service
│   │   └── external_tools.py         # External Tool Integration
│   ├── models/
│   │   └── schemas.py               # Data Models and Schemas
│   ├── config/
│   │   └── settings.py              # Configuration Settings
│   ├── utils/
│   │   ├── firebase.py              # Firebase Database Integration
│   │   ├── redis_client.py          # Redis Client
│   │   └── openai_client.py         # OpenAI Integration
|   ├── Dockerfile
│   ├── main.py                      # FastAPI Application Entry Point
│   └── requirements.txt             # Python Dependencies
|   
```

## Contributing

### Code Standards

- Follow PEP 8 for Python code
- Follow ESLint configuration for JavaScript/React code
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

**Last Updated**: April 2026
