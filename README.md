# InfluxDB Python Example
* Support on Python3.X

# Install requirement
```
pip install -r requirement.txt
```



# Setup InfluxDB on Ubuntu OS.

## Setup

### line 1
```
curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
```
### line 2
```
sudo apt-get update && sudo apt-get install influxdb
```
### line 3
```
sudo apt-get install influxdb-client
```

### line 4
```
sudo service influxdb start
```
### line 5
```
influx -version
```

InfluxDB shell version: 1.1.1 (if this text is visible on your screen, setup will be done!)

## Create Users.

### Step1 : Enable authentication
- The configuration file is located in /etc/influxdb/influxdb.conf.
- Edit this file.
- In the [http]section of the InfluxDB configuration file (influxdb.conf), uncomment the auth-enabled option and set it to true, as shown here:

```
  [http]  
  # Determines whether HTTP endpoint is enabled.
  # enabled = true

  # The bind address used by the HTTP service.
  # bind-address = ":8086"

  # Determines whether HTTP authentication is enabled.
  auth-enabled = true #
```


### Step2 : Restart InfluxDB Service 
```
sudo systemctl restart influxdb
```

### Step3 : Create a admin user
```
curl -XPOST "http://localhost:8086/query" --data-urlencode "q=CREATE USER admin WITH PASSWORD 'admin' WITH ALL PRIVILEGES"
```

- localhost : with the IP or hostname of your InfluxDB OSS instance or one of your InfluxEnterprise data nodes
- admin : with your own username
- admin : with your own password (note that the password requires single quotes)

# Reference
[InfluxDB Python Examples]!(https://influxdb-python.readthedocs.io/en/latest/examples.html)  
[Managing InfluxDB users]!(https://docs.influxdata.com/chronograf/v1.7/administration/managing-influxdb-users/)
