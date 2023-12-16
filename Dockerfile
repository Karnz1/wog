FROM python:3
RUN pip install flask
WORKDIR /scores
COPY main_score.py scores.txt /scores
CMD python main_score.py

