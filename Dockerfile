FROM python:3
WORKDIR /app
RUN pip install flask
#RUN echo "0" > /scores/Scores.txt
COPY ./templates /app/templates
COPY main_score.py /app
COPY Scores.txt /app
EXPOSE 8777
CMD ["python", "main_score.py"]

