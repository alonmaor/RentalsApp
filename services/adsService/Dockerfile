FROM python:3.9
COPY ./ /app/
RUN pip3 install -r /app/requirements.txt
WORKDIR /app
EXPOSE ${PORT}
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-5000}
