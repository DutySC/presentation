FROM python:3.10-alpine
LABEL name="Python project-TelegramBot"
LABEL version="1.0"
LABEL email="dutyscbars@gmail.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
COPY . app
WORKDIR app
RUN mkdir -pv Results/Results_sc
RUN pip install -r requirements.txt
CMD ["python3", "BotTelegram.py"]
#docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest