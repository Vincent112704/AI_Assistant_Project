FROM python:3.13

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

# Install uvicorn explicitly
RUN pip install uvicorn==0.27.0

# Force install debugpy if Poetry missed it
RUN pip install debugpy==1.8.20

COPY . .

EXPOSE 8000
EXPOSE 5678

CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]