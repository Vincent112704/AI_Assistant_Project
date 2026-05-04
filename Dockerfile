FROM python:3.13

WORKDIR /app


# COPY requirements.txt .
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

RUN pip install poetry
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root

COPY . . 

EXPOSE 8000
EXPOSE 5678


CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

#docker-compose up --build 
#^^ command to start docker-compose