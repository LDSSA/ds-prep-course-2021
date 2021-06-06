import inspect
import math
import re
import json
import sys


#ipython = get_ipython()


#def hide_traceback(exc_tuple=None, filename=None, tb_offset=None,
#                   exception_only=False, running_compiled_code=False):
#    etype, value, tb = sys.exc_info()
#    return ipython._showtraceback(etype, value, ipython.InteractiveTB.get_exception_only(etype, value))


# Uncomment after tests
#ipython.showtraceback = hide_traceback


def import_data_solution():
    with open("data/countries.json") as json_file:
        data = json.load(json_file)
    return data

def b1_exerc_1_grading(import_data):
    countries = import_data()
    assert isinstance(countries, dict), "Not correct. Keep trying."
    assert len(countries) == 194, "Not correct. Keep trying."
    assert countries["Albania"]["Continent"] == "Europe", \
           "Not correct. Keep trying."
    assert countries["Vietnam"]["Area"] == 329560, "Not correct. Keep trying."


def b1_exerc_2_grading(convert_population_to_int):
    countries = import_data_solution()
    countries = convert_population_to_int(countries)
    for country in countries.keys():
        assert isinstance(countries[country]["Population"], int), \
               "Not correct. Keep trying."
    assert len(countries) == 194, "Not correct. Keep trying."
    source = inspect.getsource(convert_population_to_int)
    assert "for" in source, "Not correct. Keep trying."


def b1_exerc_3_grading(convert_area_to_sq_km):
    countries = import_data_solution()
    countries = convert_area_to_sq_km(countries)
    for country in countries.keys():
        assert isinstance(countries[country]["Area"], float), \
                "Not correct. Keep trying."
    assert len(countries) == 194, "Not correct. Keep trying."
    assert math.isclose(countries["Haiti"]["Area"], 71872.2, abs_tol=0.1), \
           "Not correct. Keep trying."
    assert math.isclose(countries["Morocco"]["Area"], 1156560.0, abs_tol=0.1), \
           "Not correct. Keep trying."


def b1_exerc_4_grading(get_europe_countries):
    countries = import_data_solution()
    countries_list = get_europe_countries(countries)
    assert isinstance(countries_list, list), "Not correct. Keep trying."
    assert len(countries_list) == 35, "Not correct. Keep trying."
    assert countries_list[0] == "Albania", "Not correct. Keep trying."
    assert countries_list[5] == "Croatia", "Not correct. Keep trying."
    assert countries_list[34] == "United Kingdom", "Not correct. Keep trying."
    source = inspect.getsource(get_europe_countries)
    assert "for" in source, "Not correct. Keep trying."
    assert "[" in source, "Not correct. Keep trying."
    assert "in" in source, "Not correct. Keep trying."
    assert ".sort(" in source, "Not correct. Keep trying."


def b1_exerc_5_grading(get_literacy_levels_by_continent, continent):
    countries = import_data_solution()
    literacy_tuple = get_literacy_levels_by_continent(countries, continent)    
    for literacy in literacy_tuple:
        assert len(literacy) == 3, "Not correct. Keep trying."
        assert isinstance(literacy[0], str), "Not correct. Keep trying."
        assert isinstance(literacy[1], float), "Not correct. Keep trying."
        assert isinstance(literacy[2], str), "Not correct. Keep trying."

    if continent == "Europe":
        assert len(literacy_tuple) == 35, "Not correct. Keep trying."
        assert literacy_tuple[21][0] == 'Malta', "Not correct. Keep trying."
        assert math.isclose(literacy_tuple[21][1], 92.8, abs_tol=0.1), \
               "Not correct. Keep trying."
        assert literacy_tuple[21][2] == 'VERY_HIGH', "Not correct. Keep trying."
        assert literacy_tuple[1][2] == 'VERY_HIGH', "Not correct. Keep trying."
        assert literacy_tuple[0][2] == 'HIGH', "Not correct. Keep trying."
        assert literacy_tuple[-1][2] == 'VERY_HIGH', "Not correct. Keep trying."

    if continent == "Africa":
        assert len(literacy_tuple) == 55, "Not correct. Keep trying."
        assert literacy_tuple[14][0] == 'Djibouti', "Not correct. Keep trying."
        assert math.isclose(literacy_tuple[14][1], 67.9, abs_tol=0.1), \
               "Not correct. Keep trying."
        assert literacy_tuple[14][2] == 'MEDIUM', "Not correct. Keep trying."
        assert literacy_tuple[1][2] == 'LOW', "Not correct. Keep trying."
        assert literacy_tuple[0][2] == 'HIGH', "Not correct. Keep trying."
        assert literacy_tuple[-1][2] == 'VERY_HIGH', "Not correct. Keep trying."


def b1_exerc_6_grading(get_country_codes):
    countries = import_data_solution()
    country_codes = get_country_codes(countries) 
    assert len(country_codes) == 194, "Not correct. Keep trying."
    for code in country_codes:
        assert isinstance(code, str), "Not correct. Keep trying."
        assert len(code) == 3, "Not correct. Keep trying."
    assert country_codes[134] == "Pak", "Not correct. Keep trying."
    assert country_codes[62] == "Fra", "Not correct. Keep trying."

    source = inspect.getsource(get_country_codes)
    assert "map" in source, "Not correct. Keep trying."
    assert "lambda" in source, "Not correct. Keep trying."


def b1_exerc_7_1_grading(country, Country):
    assert isinstance(country, Country), "Not correct. Keep trying."
    assert isinstance(country.get_population_in_millions(), float), \
           "Not correct. Keep trying."
    if country.country_name == "Penguinea":
        assert math.isclose(country.get_population_in_millions(), 12.35, abs_tol=0.01), \
               "Not correct. Keep trying."
    if country.country_name == "Walrussia":
        assert math.isclose(country.get_population_in_millions(), 8.34, abs_tol=0.01), \
               "Not correct. Keep trying."


def b1_exerc_7_2_grading(country_name, get_country_population):
    countries = import_data_solution()
    if country_name == "Turkey":
        assert math.isclose(get_country_population(countries, "Turkey"),
                            70.41,
                            abs_tol=0.01), "Not correct. Keep trying."
    elif country_name == "Narnia":
        assert get_country_population(countries, "Narnia") is None, \
               "Not correct. Keep trying."
