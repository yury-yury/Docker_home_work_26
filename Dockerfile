FROM python:3.10

ENV HOME /app
ENV DB_USER $DB_USER
ENV DB_PASSWORD $DB_PASSWORD
ENV DB_NAME $DB_NAME
ENV POSTGRES_USER $DB_USER
ENV POSTGRES_PASSWORD $DB_PASSWORD
ENV POSTGRES_DB $DB_NAME

WORKDIR $HOME

COPY requirements.txt .
RUN python3 -m pip install --no-cache -r requirements.txt

COPY config.py config.py
RUN python3 -m config.py

COPY . .

CMD python3 app.py