FROM python:latest
COPY main.py /main.py
ENTRYPOINT ["python", "/main.py"]
CMD ["9"]
