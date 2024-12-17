## Docker commands to run Prometheus & Grafana & Node-exporter
# To run a node-exporter docker container:
docker run --name=node-exporter \
  -p 9100:9100 \
  -v /proc:/host/proc:ro \
  -v /sys:/host/sys:ro \ 
  -v /:/rootfs:ro \
prom/node-exporter

docker run --name node-exporter -p 9100:9100 -v /proc:/host/proc:ro -v /sys:/host/sys:ro -v /:/rootfs:ro prom/prometheus

# To run a Prometheus docker container:
docker run -d --name=prometheus -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus

# To run a Grafana docker container:
docker run -d --name=grafana -p 3000:3000 --link prometheus:prometheus grafana/grafana