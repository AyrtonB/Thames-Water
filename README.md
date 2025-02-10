# Thames-Water

`pip install thameswaterclient`

Thames water API client, login with:

```python
from thameswaterclient import ThamesWater

email = 'myname@provider.com'
password = '**********'
account_number = 123456789

thames_water = ThamesWater(email=email, password=password, account_number=account_number)
```

You can then retrieve your hourly data and convert it into a pandas seriess

```python
from thameswaterclient import meter_usage_lines_to_timeseries

meter = 123456789
start = datetime.date(2024, 10, 1)
end = datetime.date(2024, 12, 31)

meter_usage = thames_water.get_meter_usage(meter, start, end)
s_readings = meter_usage_lines_to_timeseries(start, end, meter_usage.Lines)
```
