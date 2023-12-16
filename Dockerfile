FROM python:alpine
RUN pip install flask
WORKDIR /scores
COPY main_score.py /scores
#COPY Scores.txt /scores
CMD python main_score.py

