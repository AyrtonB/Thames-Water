import os
import datetime

from dotenv import load_dotenv

from thameswaterclient import ThamesWater, meter_usage_lines_to_timeseries


load_dotenv()

email = os.environ['EMAIL']
password = os.environ['PASSWORD']
account_number = os.environ['ACCOUNT_NUMBER']
meter = os.environ['METER']

def test_hourly_reading_retrieval():
    thames_water = ThamesWater(email=email, password=password, account_number=account_number)

    start = datetime.date(2025, 2, 11)
    end = datetime.date(2025, 2, 16)

    meter_usage = thames_water.get_meter_usage(meter, start, end)
    readings = meter_usage_lines_to_timeseries(start, end, meter_usage.Lines)

    assert len(readings) > 0
