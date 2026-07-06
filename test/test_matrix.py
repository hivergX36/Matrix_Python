import pytest
import src.Matrix as m


def test_parse_data_nb_rows_and_cols():
    matrix = m.Matrix()
    matrix.parse_data("data/data2.txt")
    assert matrix.rows == 34
    assert matrix.cols == 4


def test_parse_data_negative():
    matrix = m.Matrix()
    matrix.parse_data("data/data2.txt")
    assert matrix.rows != 35
    assert matrix.cols != 5
