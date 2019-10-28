#!/usr/bin/env bash

set -x

su vagrant


docker run --name mysql --network=host -d -e MYSQL_ROOT_PASSWORD=datadogpassword -e MYSQL_USER=datadog -e MYSQL_PASSWORD=datadogpassword -l com.datadoghq.ad.check_names='["mysql"]' -l com.datadoghq.ad.init_configs='[{}]' -l com.datadoghq.ad.instances='[{"server": "127.0.0.1", "user": "root","pass": "datadogpassword"}]' mysql:5.7

DOCKER_CONTENT_TRUST=1 \
docker run --name datadog -d -v /var/run/docker.sock:/var/run/docker.sock:ro -v /proc/:/host/proc/:ro -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro -v /home/vagrant/datadog-agent-conf/conf.d:/conf.d:ro -v /home/vagrant/datadog-agent-conf/checks.d:/checks.d:ro -e DD_API_KEY=94ee5ca0a31657a5f42ec35ecc206718 -e DD_SITE="datadoghq.eu" -e DD_APM_ENABLED=true --network host datadog/agent:latest
