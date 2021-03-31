FROM ubuntu:18.04
ENV PYTHONUNBUFFERED 1
RUN apt update -y
RUN apt install software-properties-common -y
RUN apt update -y
#RUN apt install add-apt-repository -y
#RUN apt update -y
#RUN apt-get postgresql -y Hayque instalar postgres parece. vr versionnes, tener en cuenta la imagen de postgresql. La instalación tiene configuraciones
RUN add-apt-repository ppa:ubuntugis/ppa
#RUN apt-get update -y
RUN apt-get install gdal-bin -y
RUN apt-get install python3-gdal -y
RUN apt-get install python-gdal -y
RUN apt-get install libgdal-dev -y
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal
RUN apt install python3-pip -y
RUN apt-get install python3-dev
#RUN pip3 install GDAL
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
#RUN apt install python-pip -y
RUN pip3 install -r requirements.txt
COPY . /code/