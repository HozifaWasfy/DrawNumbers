FROM ubuntu:latest

#COPY "C:\Users\hozay\PycharmProjects\pythonProject4"  /pythonProject4
#WORKDIR /pythonProject4
COPY C:\Users\hozay\PycharmProjects\pythonProject4 project4
WORKDIR project4
RUN apt-get update && apt-get install -y \
    python3\
    python3-pip
RUN pip install matplotlib \
    pip install numpy \
    pip install tensorflow \
    pip install keras \
    pip install pygame \

CMD ["cd project4;./createNN.py;./main.py"]
