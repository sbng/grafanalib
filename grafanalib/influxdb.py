"""Helpers to create InfluxDB-specific Grafana queries."""

import attr

TIME_SERIES_TARGET_FORMAT = 'time_series'


@attr.s
class InfluxDBTarget(object):
    """
    Generates InfluxDB target JSON structure.

    Grafana docs on using InfluxDB:
    https://grafana.com/docs/features/datasources/influxdb/
    InfluxDB docs on querying or reading data:
    https://v2.docs.influxdata.com/v2.0/query-data/

    :param alias: legend alias
    :param format: Bucket aggregators
    :param datasource: InfluxDB name (Required if different influxb is used for different target) 
    :param measurement: Metric Aggregators
    :param query: query
    :param rawQuery: target reference id
    :param refId: target reference id
    """

    alias = attr.ib(default="")
    format = attr.ib(default=TIME_SERIES_TARGET_FORMAT)
    datasource = attr.ib(default="")
    measurement = attr.ib(default="")
    query = attr.ib(default="")
    rawQuery = attr.ib(default=True)
    refId = attr.ib(default="")

    def to_json_data(self):
        return {
            'query': self.query,
            'resultFormat': self.format,
            'datasource': self.datasource,
            'alias': self.alias,
            'measurement': self.measurement,
            'rawQuery': self.rawQuery,
            'refId': self.refId
        }
