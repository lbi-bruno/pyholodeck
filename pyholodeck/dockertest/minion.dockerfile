# dockerfile to build simple salt minion
# from which I can populate using salt and then build new docker images

FROM debian:jessie
RUN apt-get update
RUN apt-get install -y salt-minion
ADD startup.sh /root
RUN chmod 0777 /root/startup.sh
ENTRYPOINT ["/bin/bash", "/root/startup.sh"]
CMD ["Arg From Dockerfile"]

