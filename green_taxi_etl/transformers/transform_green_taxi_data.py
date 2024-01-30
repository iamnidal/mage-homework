if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def camel_to_snake(s):
    return ''.join(['_'+c.lower() if c.isupper() else c for c in s]).lstrip('_')

@transformer
def transform(data, *args, **kwargs):
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    vendor = data['VendorID']
    data.columns = ( data.columns
                  .str.replace(' ', '-')
                  .str.lower()
    )
    print('Vendor Id List', list(set(vendor)))
    return data[(data['passenger_count'] > 0) | (data['trip_distance'] > 0)]

@test
def test_output(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero distance' 
@test
def test_output(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passenger'
@test
def test_output(output, *args) -> None:
    assert output.columns.isin(['vendorid']).sum() == 1, 'There is no vendorid Column'
    # assert output[, 'There are rides with zero passenger'
