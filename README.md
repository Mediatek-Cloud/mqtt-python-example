# MQTT Client Python Example

MQTT Python example code to connect to MCS via mqtt protocol.

## Prerequisite

Please follows the [MCS tutorial](https://mcs.mediatek.com/resources/latest/tutorial/getting_started) to create your prototype and test device.

## Usage

### 1.Install paho mqtt client.

```
$ pip install paho
```

### 2.Subscribe to a topic

If you want to subscribe a topic, the format should be `mcs/deviceId/deviceKey/dataChnnelId`.

The format of the subscribe arguments are: `host`、`port` and `topic`.

For example,

```
$ python subscribe.py mqtt.mcs.medaitek.com 1883 mcs/xxxxxx/yyyyyyyy/int
```
### 3.Publish a datapoints

The format of the publish arguments are: `host`、`port`、 `topic` and `values`.

```
$ python publish.py mqtt.mcs.mediatek.com 1883 mcs/deviceId/deviceKey/dataChannelId timestamp,dataChannelId/values
```

For more information about MCS MQTT protocol, please check [TCP and MQTT Connection](https://mcs.mediatek.com/resources/latest/tutorial/communication_channels).
