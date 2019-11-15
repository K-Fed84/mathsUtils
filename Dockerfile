FROM python:3

ADD MathsUtils.py /

ENTRYPOINT [ "python", "./MathsUtils.py" ]