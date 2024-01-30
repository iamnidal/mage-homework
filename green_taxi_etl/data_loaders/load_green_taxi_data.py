import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    file_names = [
        'green_tripdata_2020-10.csv.gz',
        'green_tripdata_2020-11.csv.gz',
        'green_tripdata_2020-12.csv.gz'
    ]
    # url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'
    # return pd.read_csv(url, sep=",", compression="gzip")
    base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green'
    final_data = []
    taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra':float,
                    'mta_tax':float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
    }
    # native date parsing 
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    def download_and_concatenate():
        for file_name in file_names:
            url = f'{base_url}/{file_name}'
            df = pd.read_csv(url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
            # print(len(df), file_name)
            final_data.append(df)
        return pd.concat(final_data, ignore_index=True)

    result = download_and_concatenate()
    return result

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
