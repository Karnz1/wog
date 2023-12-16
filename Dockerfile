FROM python:3
WORKDIR /scores
RUN pip install flask
#RUN echo "0" > /scores/Scores.txt
COPY main_score.py /scores
COPY Scores.txt /scores
EXPOSE 8777
CMD ["python", "main_score.py"]

