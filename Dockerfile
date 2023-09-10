FROM python:3.8.10
ADD . ./opt/
WORKDIR /opt/
EXPOSE 5000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]