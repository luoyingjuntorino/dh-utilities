from flask import Flask, request, render_template
from flask import send_from_directory
from influxdb_client.client.warnings import MissingPivotFunction
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import InfluxDBClient
import warnings
import pytz
import os

app = Flask(__name__)
warnings.simplefilter("ignore", MissingPivotFunction)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        bucket = request.form['bucket']
        start_time = request.form['start_time']
        stop_time = request.form['stop_time']
        query_field = request.form['query_field']

        token = "xlPqJw4yEbmJ2u6vEyD7xVpCqIwcsR3tvIREXQoiYki32rXo43mUdVQ8e5k6YA2TBZQ-FO9Lf-aORU26HTLLcQ=="
        org = "polito"
        client = InfluxDBClient(url="http://localhost:8087", token=token, org=org, debug=False)

        query = f'from(bucket: "{bucket}") \
                  |> range(start: {start_time}, stop: {stop_time}) \
                  |> filter(fn: (r) => r["_field"] == "{query_field}")'

        query_api = client.query_api()
        result = query_api.query_data_frame(query=str(query))

        df = result[['_time', '_measurement', '_field', '_value']]

        def convert_to_rome_time(row):
            dt = row['_time']
            rome_tz = pytz.timezone('Europe/Rome')
            rome_time = dt.astimezone(rome_tz)
            row['_time'] = rome_time
            return row

        df = df.apply(convert_to_rome_time, axis=1)
        # df.set_index("_time", inplace=True)

        df.to_csv(os.path.join('influxweb', 'exported.csv'), index=False)

        return render_template('index.html', exported=True)

    return render_template('index.html', exported=False)

@app.route('/exported.csv')
def download_csv():
    return send_from_directory(app.root_path, 'exported.csv', as_attachment=True)

if __name__ == '__main__':
    app.run()
