FROM gethue/hue:4.4.0

RUN apt-get update && \
    apt-get install -yqq \
    netcat-openbsd
    
COPY ./entrypoint.sh .

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]

CMD ["./startup.sh"]