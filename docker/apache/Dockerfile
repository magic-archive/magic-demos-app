FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      ca-certificates \
      git \
      apache2 \
    && apt-get purge -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/ttyd

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
