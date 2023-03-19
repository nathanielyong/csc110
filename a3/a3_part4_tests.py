"""CSC110 Fall 2021 Assignment 3: Part 4 (Student Test Suite)

Instructions (READ THIS FIRST!)
===============================
Complete the unit tests in this file based on their docstring descriptions.
"""
import pytest

from a3_part4 import load_data
from a3_ffwi_system import WeatherMetrics, FfwiOutput

import a3_ffwi_system as ffwi


class TestCalculateMr:
    """A collection of unit tests for calculate_mr."""

    def test_equation_3a_branch(self) -> None:
        """Test the branch calculate_mr that contains Equation 3a."""
        precip = 5
        mo = 100
        expected = 177.4820542185105
        actual = ffwi.calculate_mr(precip, mo)
        assert actual == pytest.approx(expected)

    def test_equation_3b_branch(self) -> None:
        """Test the branch calculate_mr that contains Equation 3b."""
        precip = 5
        mo = 200
        expected = 229.1022820621266
        actual = ffwi.calculate_mr(precip, mo)
        assert actual == pytest.approx(expected)


class TestCalculateM:
    """A collection of unit tests for calculate_m."""

    def test_no_mutation_mo_equals_ed(self) -> None:
        """Test that calculate_m does not mutate the WeatherMetrics argument when mo == ed."""
        wm = WeatherMetrics(1, 1, 100, 100, 100, 100)
        wm_copy = WeatherMetrics(1, 1, 100, 100, 100, 100)
        ed = 100
        mo = 100
        ffwi.calculate_m(wm, ed, mo)
        assert wm == wm_copy

    def test_no_mutation_mo_leq_ew(self) -> None:
        """Test that calculate_m does not mutate the WeatherMetrics argument when mo <= ew."""
        wm = WeatherMetrics(1, 1, 100, 100, 100, 100)
        wm_copy = WeatherMetrics(1, 1, 100, 100, 100, 100)
        ed = 100
        mo = 10
        ffwi.calculate_m(wm, ed, mo)
        assert wm == wm_copy

    def test_no_mutation_mo_greater_than_ew(self) -> None:
        """Test that calculate_m does not mutate the WeatherMetrics argument when mo > ew."""
        wm = WeatherMetrics(1, 1, 100, 100, 100, 100)
        wm_copy = WeatherMetrics(1, 1, 100, 100, 100, 100)
        ed = 100
        mo = 50
        ffwi.calculate_m(wm, ed, mo)
        assert wm == wm_copy

    def test_no_mutation_mo_greater_than_ed(self) -> None:
        """Test that calculate_m does not mutate the WeatherMetrics argument when mo > ed."""
        wm = WeatherMetrics(1, 1, 100, 100, 100, 100)
        wm_copy = WeatherMetrics(1, 1, 100, 100, 100, 100)
        ed = 100
        mo = 150
        ffwi.calculate_m(wm, ed, mo)
        assert wm == wm_copy


@pytest.fixture
def sample_data() -> tuple[list[WeatherMetrics], list[FfwiOutput]]:
    """A pytest fixture containing the data in data/ffwi/sample_data.csv

    NOTE: Do not change this function. Do not call this function directly. It is a pytest fixture,
    so pytest will call it automatically and pass it to test_ffmc_against_ground_truth below.
    """
    return load_data('data/ffwi/sample_data.csv')


def test_ffmc_against_ground_truth(sample_data) -> None:
    """Test the correctness of calculate_ffmc, calculate_dmc, calculate_dc, calculate_isi,
     calculate_bui, and calculate_fwi based on sample_data.

    Ensure that, for every WeatherMetric element in sample_data[0] passed to each of the calculate_
    functions mentioned above, the return value, rounded to the nearest decimal, matches the
    corresponding value from the FfwiOutput element in sample_data[1].

    Hints:
        - You will need to use the built-in function round.
        - You may want to use pytest.approx since you are comparing float values.
    """
    ffmc = ffwi.INITIAL_FFMC
    dmc = ffwi.INITIAL_DMC
    dc = ffwi.INITIAL_DC

    inputs, outputs = sample_data

    for i in range(len(inputs)):
        expected_ffmc = outputs[i].ffmc
        actual_ffmc = ffwi.calculate_ffmc(inputs[i], ffmc)
        assert round(actual_ffmc, 1) == pytest.approx(expected_ffmc)

        expected_dmc = outputs[i].dmc
        actual_dmc = ffwi.calculate_dmc(inputs[i], dmc)
        assert round(actual_dmc, 1) == pytest.approx(expected_dmc)

        expected_dc = outputs[i].dc
        actual_dc = ffwi.calculate_dc(inputs[i], dc)
        assert round(actual_dc, 1) == pytest.approx(expected_dc)

        expected_isi = outputs[i].isi
        actual_isi = ffwi.calculate_isi(inputs[i], actual_ffmc)
        assert round(actual_isi, 1) == pytest.approx(expected_isi)

        expected_bui = outputs[i].bui
        actual_bui = ffwi.calculate_bui(actual_dmc, actual_dc)
        assert round(actual_bui, 1) == pytest.approx(expected_bui)

        expected_fwi = outputs[i].fwi
        actual_fwi = ffwi.calculate_fwi(actual_isi, actual_bui)
        assert round(actual_fwi, 1) == pytest.approx(expected_fwi)

        ffmc = actual_ffmc
        dmc = actual_dmc
        dc = actual_dc


if __name__ == '__main__':
    pytest.main(['a3_part4_tests.py'])

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    import python_ta
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    python_ta.check_all(config={
        'allowed-io': ['load_data'],
        'extra-imports': ['a3_ffwi_system', 'a3_part4', 'pytest'],
        'max-line-length': 100,
        'max-args': 6,
        'max-locals': 25,
        'disable': ['R1705', 'R0201', 'C0103', 'W0621', 'E9970'],
    })
