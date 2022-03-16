FROM python:3.7

ADD discordbot.py . 

RUN pip install requests discord

CMD ["python", "discordbot.py" ]


