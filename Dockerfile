FROM registry.access.redhat.com/ubi8/python-38

ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install pytest selenium==3.141.0

CMD ["cat"]
