FROM ubuntu:focal AS spython-base
RUN apt-get -y update && apt-get -y install python3-pip git
RUN git clone https://github.com/nuitrcs/rcds-gh-actions-workshop /template
RUN cd /template
RUN pip3 install /template
CMD python3 -c "from YOURPACKAGE.mymodule.mymodule import MyClass;print(MyClass().return_one())"
