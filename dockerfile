FROM python:3.9

RUN mkdir -p /home/backend

COPY  requirements.txt /home/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /home/requirements.txt


WORKDIR /home/
COPY ./backend ./backend/

CMD ["uvicorn","backend.manage:app","--host=0.0.0.0","--port=5000","--reload"]