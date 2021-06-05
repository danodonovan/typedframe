
import pandas as pd
import numpy as np
import datetime

import pytest

from typedframe import TypedDataFrame, DATE_TIME_DTYPE, STRING_DTYPE


class MyDataFrame(TypedDataFrame):
    schema = {
        'int_field': np.int16,
        'float_field': np.float64,
        'bool_field': bool,
        'str_field': STRING_DTYPE,
        'date_field': DATE_TIME_DTYPE
    }


class InheritedDataFrame(MyDataFrame):
    schema = {
        'new_field': np.int64
    }


class DataFrameWithOptional(TypedDataFrame):
    schema = {
        'required': bool
    }
    optional = {
        'optional': bool
    }


class CategoricalDataFrame(TypedDataFrame):
    schema = {
        'categorical_col': 'category'
    }

class IndexDataFrame(TypedDataFrame):
    schema = {
        'foo': bool
    }

    index_schema = ('bar', STRING_DTYPE)


class ChildIndexDataFrame(IndexDataFrame):
    pass



def test_index_success_case():
    df = pd.DataFrame({'foo': [True, False]})
    df.index = pd.Series([datetime.date.today(), datetime.date(2021, 5, 31)], name='bar')
    _ = IndexDataFrame(df)
    _ = ChildIndexDataFrame(df)


def test_index_fail_case():
    df = pd.DataFrame({'foo': [True, False]})
    with pytest.raises(AssertionError):
        _ = IndexDataFrame(df)


def test_base_success_case():
    df = pd.DataFrame({
        
    })