# InfluxDB Python Example
* Support on Python3.X

# Install requirement
```
pip install -r requirement.txt
```



# Setup InfluxDB on Ubuntu OS.

## Setup
```
sh ./setup.sh
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

- If this text {"results":[{"statement_id":0}]} show on screen, setup done !!!
# Remote to Influxdb server
```
influx -host 'host' -port 'port' -username 'username' -password 'password'
```
# Reference
[InfluxDB Python Examples]!(https://influxdb-python.readthedocs.io/en/latest/examples.html)  
[Managing InfluxDB users]!(https://docs.influxdata.com/chronograf/v1.7/administration/managing-influxdb-users/)
