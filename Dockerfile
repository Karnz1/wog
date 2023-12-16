FROM python:alpine
WORKDIR /scores
RUN pip install flask
#RUN echo "0" > /scores/Scores.txt
COPY main_score.py /scores
COPY Scores.txt /scores
CMD python main_score.py

