FROM python:3.9
COPY ./ /app/
RUN pip3 install -r /app/requirements.txt
RUN echo | ls
WORKDIR /app
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "15400"]