# Example InfluxDB in python
# Author: Rin Le <rinle.it@gmail.com>
# Date: May 14, 2019

import argparse
from influxdb import InfluxDBClient
from datetime import datetime
import json

_USER = 'admin'
_PASSWORD = 'admin'
_DBNAME = 'test'

class influxdbExample():
    def __init__ (self, _user, _pwd, _dbname):
        self._user = _user
        self._pwd = _pwd
        self._dbname = _dbname

    def connection(self, _host, _port):
        client = InfluxDBClient(_host,
                                _port, 
                                self._user, 
                                self._pwd, 
                                self._dbname)
        return client
    
    @staticmethod
    def create_db(_client, _dbname):
        # Create database
        _client.create_database(_dbname)

    @staticmethod
    def create_retention_policy(_client):
        # Create a retention policy
        _client.create_retention_policy('awesome_policy', '3d', 3, default=True)
    
    def insert(self, _client, _data):
        # _data is json object
        try:
            _client.write_points(_data)
        except Exception as _e:
            print(_e)
            # Insert Fail
            return False
        else:
            # Insert Success
            return True
    
    
    def update(self, _client, _data):
        # _data must be similar with pre-data
        try:
            self.insert(_client=_client, _data=_data)
        except Exception as _e:
            print(_e)
            return False
        else:
            return True
    
    def get(self, _client, _query):
        try:
            result = _client.query(_query)
        except Exception as _e:
            print(_e)
            # No result
            return None
        else:
            # Has result
            return result
    def delete(self, _client, _dbname, _time):
        try:
            _query = "delete from %s where time=%s" % (_dbname, _time)
            _client.query(_query)
        except Exception as _e:
            print(_e)
            # Delete Fail
            return False
        else:
            # Delete Success
            return True

    def delete_db(self, _client, _dbname):
        try:
            _client.drop_database(_dbname)
        except Exception as _e:
            print(_e)
            # Delete Fail
            return False
        else:
            # Delete Success
            return True
        
def main(_host='localhost', _port=8086):
    _influx = influxdbExample(_user=_USER,
                              _pwd=_PASSWORD,
                              _dbname=_DBNAME)
    
    # Connection
    _client = _influx.connection(_host=_host, _port=_port)

    # Create DB Name
    _influx.create_db(_client=_client,
                                _dbname=_DBNAME)
    
    # Create retention_policy
    _influx.create_retention_policy(_client=_client)

    # Get Time
    _time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    _old_time = _time

    # Insert
    _obj_data = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": _time,
            "fields": {
                "Float_value": 0.64,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]

    _ret = _influx.insert(_client=_client, _data=_obj_data)

    if _ret:
        print("Insert Success !!!")
    else:
        print("Insert Failed !!!")

    # Get
    _query = "select Float_value from cpu_load_short;"
    _result = _influx.get(_client=_client, _query=_query)
    print(_result)

    # Update
    # fix fields: Int_value
    _obj_data[0]["fields"]["Int_value"] = 5
    _ret = _influx.update(_client=_client, _data=_obj_data)
    if _ret:
        print("Update Success !!!")
    else:
        print("Update Failed !!!")

    # Delete Rows
    _ret = _influx.delete(_client=_client, _dbname=_DBNAME, _time=_old_time)
    if _ret:
        print("Delete Success !!!")
    else:
        print("Delete Failed !!!")

    # Delete DB Name
    _ret = _influx.delete_db(_client=_client, _dbname=_DBNAME)
    if _ret:
        print("Delete DB Success !!!")
    else:
        print("Delete DB Failed !!!")

def parse_args():
    """Parse the args."""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    main(_host=args.host, _port=args.port)