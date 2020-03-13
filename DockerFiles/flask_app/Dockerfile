FROM python:3.7-alpine
RUN pip install Flask
COPY run.sh .
COPY main.py .
ENV FLASK_APP=main.py
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
