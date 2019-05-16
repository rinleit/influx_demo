#!/bin/sh



# setup
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add - 
source /etc/lsb-release 
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt-get update && sudo apt-get install influxdb
sudo service influxdb start
sudo apt-get install influxdb-client
influx -version

# fix buges
# sudo dpkg -i --force-overwrite /var/cache/apt/archives/influxdb-client_*.deb

