import pandas as pd
import utils
from datetime import datetime


def build_df():
    """
    Build a test dataframe
    :return:
    """
    dates = [datetime.strftime(datetime(year=2018,
                                        month=11,
                                        day=d),
                               "%Y-%m-%d")
             for d in range(1, 4)]
    data = [{'date': d} for d in dates]
    test_df = pd.DataFrame(data=data,
                           index=range(len(data))
                           )
    test_df['date'] = pd.to_datetime(test_df['date'])
    return test_df


def test_add_weekday_feature():
    """
    Test that a weekday column is added to a dataframe
    :return:
    """
    test_df = build_df()
    mod_df = utils.add_weekday_feature(test_df)
    assert 'weekday' in mod_df.columns
    assert not mod_df['weekday'].isna().all()


def test_add_month_feature():
    """
    Test that a weekday column is added to a dataframe
    :return:
    """
    test_df = build_df()
    mod_df = utils.add_month_feature(test_df)
    assert 'month' in mod_df.columns
    assert not mod_df['month'].isna().all()

