import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

def format_ocean_proximity(raw_df):
    """
    Changes the feature `ocean_proximity` to be lowercase and change the value `<1H OCEAN` to `within_hour_ocean`
    Args:
        raw_df: pandas data frame object with the raw data from the csv
    Returns:
        formatted_df: pandas df object with the `ocean_proximity` feature with lower case values and `<1H OCEAN` values changed to `within_hour_ocean`
    """
    raw_df["ocean_proximity"] = ["within_hour_ocean" if val == "<1H OCEAN" else val for val in raw_df["ocean_proximity"]]
    raw_df["ocean_proximity"] = raw_df["ocean_proximity"].apply(lambda x: x.lower().replace(" ", "_"))
    return raw_df