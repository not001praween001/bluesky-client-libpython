bluesky-client-libpython
========================
The library provides a simple way to connect the bluesky API. 

How to
------
```shell
python testlib.py
```
The testlib.py get all of sensor data that connecting bluesky. The program will show the sensor data from all of sensor nodes that connected the mcp3208 of all channel and specified pin 0. The pin is specified as the physical pin of SPI specification following the standard RaspberryPi model b specification. In addidition, the pin number can be specified with the API provided by the light-weight connecting protocol of [Blue-sky cloud server](https://github.com/Bluesky-CPS/BlueSkyLoggerCloudBINResearchVer1.0).

***Author***: *Praween AMONTAMAVUT*