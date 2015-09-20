bluesky-client-libpython
========================
The library provides a simple way to connect the bluesky API. 

How to
------

- compile form source

```shell
python setup.py build
cd build/lib.{your system detail}-{python version}/bluesky_libpython
python testlib.py
```
The testlib.py get all of sensor data that connecting bluesky. The program will show the sensor data from all of sensor nodes that connected the mcp3208 of all channel and specified pin 0. The pin is specified as the physical pin of SPI specification following the standard RaspberryPi model b specification. In addidition, the pin number can be specified with the API provided by the light-weight connecting protocol of [Blue-sky cloud server](https://github.com/Bluesky-CPS/BlueSkyLoggerCloudBINResearchVer1.0).

- python package manager

  - install the client library

  ```shell
  pip install bluesky_libpython
  ```

  - test the code

  [list_ed.py]
  
  ```shell
  import bluesky_libpython
  
  # Specified your bluesky gateway
  BlueskyGateway = "127.0.0.1:8189"
  
  conn = bluesky_libpython.bluesky_cli.blueskyconn(BlueskyGateway, "guest", "guest")
  deviceList = conn.list_ed()
  print deviceList
  ```

  - running the code
   
  ```shell
  python list_ed.py
  ```
  
***Author***: *Praween AMONTAMAVUT*
