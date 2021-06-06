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


def generate_data():
    return [{"Year": "2013", "Total": "53,2", "Education": "80,4", "Arts and Humanities": "56,9", "Social Sciences, Management and Law": "58,1", "Sciences, Maths and Computer Science": "(R) 47,2", "Engineering": "(R) 27,4", "Agriculture": "56,9", "Health and Social Security": "76,8", "Services": "(R) 41,4"},
            {"Year": "201", "Total": "22,2", "Education": "80,4", "Arts and Humanities": "16,9", "Social Sciences, Management and Law": "58,1", "Sciences, Maths and Computer Science": "(R) 47,2", "Engineering": "(R) 27,4", "Agriculture": "56,9", "Health and Social Security": "76,8", "Services": "(R) 41,4"},
            {"Year": "2014", "Total": "53,5", "Education": "80,7", "Arts and Humanities": "58,0", "Social Sciences, Management and Law": "58,5", "Sciences, Maths and Computer Science": "(R) 47,5", "Engineering": "(R) 27,6", "Agriculture": "56,9", "Health and Social Security": "76,6", "Services": "(R) 41,1"},
            {"Year": "2015", "Total": "53,6", "Education": "80,7", "Arts and Humanities": "58,7", "Social Sciences, Management and Law": "58,6", "Sciences, Maths and Computer Science": "(R) 47,8", "Engineering": "(R) 27,0", "Agriculture": "56,3", "Health and Social Security": "76,7", "Services": "(R) 41,0"},
            {"Year": "2016", "Total": "53,4", "Education": "80,3", "Arts and Humanities": "58,6", "Social Sciences, Management and Law": "58,9", "Sciences, Maths and Computer Science": "(R) 45,7", "Engineering": "(R) 27,3", "Agriculture": "56,4", "Health and Social Security": "76,8", "Services": "(R) 41,7"},
            {"Year": "2017", "Total": "53,6", "Education": "79,3", "Arts and Humanities": "59,0", "Social Sciences, Management and Law": "59,5", "Sciences, Maths and Computer Science": "44,2", "Engineering": "27,5", "Agriculture": "57,3", "Health and Social Security": "77,0", "Services": "42,1"},
            {"Year": "2013", "Total": "52,2", "Education": "80,4", "Arts and Humanities": "57,9", "Social Sciences, Management and Law": "58,1", "Sciences, Maths and Computer Science": "(R) 47,2", "Engineering": "(R) 27,4", "Agriculture": "56,9", "Health and Social Security": "76,8", "Services": "(R) 41,4"},
            {"Year": "2014", "Total": "53,5", "Education": "80,7", "Arts and Humanities": "58,0", "Social Sciences, Management and Law": "58,5", "Sciences, Maths and Computer Science": "(R) 47,5", "Engineering": "(R) 27,6", "Agriculture": "56,9", "Health and Social Security": "76,6", "Services": "(R) 41,1"},
            {"Year": "2015", "Total": "53,6", "Education": "80,7", "Arts and Humanities": "58,7", "Social Sciences, Management and Law": "58,6", "Sciences, Maths and Computer Science": "(R) 47,8", "Engineering": "(R) 27,0", "Agriculture": "56,3", "Health and Social Security": "76,7", "Services": "(R) 41,0"},
            {"Year": "2016", "Total": "53,4", "Education": "80,3", "Arts and Humanities": "58,6", "Social Sciences, Management and Law": "58,9", "Sciences, Maths and Computer Science": "(R) 45,7", "Engineering": "(R) 27,3", "Agriculture": "56,4", "Health and Social Security": "76,8", "Services": "(R) 41,7"}
            ]


def generate_data_comma():
    return [{"year": "2013", "total": "53,2", "education": "80,4", "arts_and_humanities": "56,9", "social_sciences_management_and_law": "58,1", "sciences_maths_and_computer_science": "47,2", "engineering": "27,4", "Agriculture": "56,9", "health_and_social_security": "76,8", "services": "41,4"},
            {"year": "201", "total": "22,2", "education": "80,4", "arts_and_humanities": "16,9", "social_sciences_management_and_law": "58,1", "sciences_maths_and_computer_science": "47,2", "engineering": "27,4", "Agriculture": "56,9", "health_and_social_security": "76,8", "services": "41,4"},
            {"year": "2014", "total": "53,5", "education": "80,7", "arts_and_humanities": "58,0", "social_sciences_management_and_law": "58,5", "sciences_maths_and_computer_science": "47,5", "engineering": "27,6", "Agriculture": "56,9", "health_and_social_security": "76,6", "services": "41,1"},
            {"year": "2015", "total": "53,6", "education": "80,7", "arts_and_humanities": "58,7", "social_sciences_management_and_law": "58,6", "sciences_maths_and_computer_science": "47,8", "engineering": "27,0", "Agriculture": "56,3", "health_and_social_security": "76,7", "services": "41,0"},
            {"year": "2016", "total": "53,4", "education": "80,3", "arts_and_humanities": "58,6", "social_sciences_management_and_law": "58,9", "sciences_maths_and_computer_science": "45,7", "engineering": "27,3", "Agriculture": "56,4", "health_and_social_security": "76,8", "services": "41,7"},
            {"year": "2017", "total": "53,6", "education": "79,3", "arts_and_humanities": "59,0", "social_sciences_management_and_law": "59,5", "sciences_maths_and_computer_science": "44,2", "engineering": "27,5", "Agriculture": "57,3", "health_and_social_security": "77,0", "services": "42,1"},
            {"year": "2013", "total": "52,2", "education": "80,4", "arts_and_humanities": "57,9", "social_sciences_management_and_law": "58,1", "sciences_maths_and_computer_science": "47,2", "engineering": "27,4", "Agriculture": "56,9", "health_and_social_security": "76,8", "services": "41,4"},
            {"year": "2014", "total": "53,5", "education": "80,7", "arts_and_humanities": "58,0", "social_sciences_management_and_law": "58,5", "sciences_maths_and_computer_science": "47,5", "engineering": "27,6", "Agriculture": "56,9", "health_and_social_security": "76,6", "services": "41,1"},
            {"year": "2015", "total": "53,6", "education": "80,7", "arts_and_humanities": "58,7", "social_sciences_management_and_law": "58,6", "sciences_maths_and_computer_science": "47,8", "engineering": "27,0", "Agriculture": "56,3", "health_and_social_security": "76,7", "services": "41,0"},
            {"year": "2016", "total": "53,4", "education": "80,3", "arts_and_humanities": "58,6", "social_sciences_management_and_law": "58,9", "sciences_maths_and_computer_science": "45,7", "engineering": "27,3", "Agriculture": "56,4", "health_and_social_security": "76,8", "services": "41,7"}
            ]


def generate_data_clean():
    return [{"education": 80.4, "health_and_social_security": 76.8, "social_sciences_management_and_law": 58.1, "sciences_maths_and_computer_science": 47.2, "engineering": 27.4, "arts_and_humanities": 56.9, "year": 2013, "services": 41.4, "total": 53.2, "agriculture": 56.9},
            {"education": 80.7, "health_and_social_security": 76.6, "social_sciences_management_and_law": 58.5, "sciences_maths_and_computer_science": 47.5, "engineering": 27.6, "arts_and_humanities": 58.0, "year": 2014, "services": 41.1, "total": 53.5, "agriculture": 56.9},
            {"education": 80.4, "health_and_social_security": 76.8, "social_sciences_management_and_law": 58.1, "sciences_maths_and_computer_science": 47.2, "engineering": 27.4, "arts_and_humanities": 56.9, "year": 2013, "services": 41.4, "total": 53.2, "agriculture": 56.9},
            {"education": 80.7, "health_and_social_security": 76.6, "social_sciences_management_and_law": 58.5, "sciences_maths_and_computer_science": 47.5, "engineering": 27.6, "arts_and_humanities": 58.0, "year": 2014, "services": 41.1, "total": 53.5, "agriculture": 56.9},
            {"education": 80.7, "health_and_social_security": 76.7, "social_sciences_management_and_law": 58.6, "sciences_maths_and_computer_science": 47.8, "engineering": 27.0, "arts_and_humanities": 58.7, "year": 2015, "services": 41.0, "total": 53.6, "agriculture": 56.3},
            {"education": 80.3, "health_and_social_security": 76.8, "social_sciences_management_and_law": 58.9, "sciences_maths_and_computer_science": 45.7, "engineering": 27.3, "arts_and_humanities": 58.6, "year": 2016, "services": 41.7, "total": 53.4, "agriculture": 56.4},
            {"education": 79.3, "health_and_social_security": 77.0, "social_sciences_management_and_law": 59.5, "sciences_maths_and_computer_science": 44.2, "engineering": 27.5, "arts_and_humanities": 59.0, "year": 2017, "services": 42.1, "total": 53.6, "agriculture": 57.3},
            {"education": 80.4, "health_and_social_security": 76.8, "social_sciences_management_and_law": 58.1, "sciences_maths_and_computer_science": 47.2, "engineering": 27.4, "arts_and_humanities": 56.9, "year": 2013, "services": 41.4, "total": 53.2, "agriculture": 56.9},
            {"education": 80.7, "health_and_social_security": 76.6, "social_sciences_management_and_law": 58.5, "sciences_maths_and_computer_science": 47.5, "engineering": 27.6, "arts_and_humanities": 58.0, "year": 2014, "services": 41.1, "total": 53.5, "agriculture": 56.9},
            {"education": 80.7, "health_and_social_security": 76.7, "social_sciences_management_and_law": 58.6, "sciences_maths_and_computer_science": 47.8, "engineering": 27.0, "arts_and_humanities": 58.7, "year": 2015, "services": 41.0, "total": 53.6, "agriculture": 56.3},
            {"education": 80.3, "health_and_social_security": 76.8, "social_sciences_management_and_law": 58.9, "sciences_maths_and_computer_science": 45.7, "engineering": 27.3, "arts_and_humanities": 58.6, "year": 2016, "services": 41.7, "total": 53.4, "agriculture": 56.4},
            {"education": 79.3, "health_and_social_security": 77.0, "social_sciences_management_and_law": 59.5, "sciences_maths_and_computer_science": 44.2, "engineering": 27.5, "arts_and_humanities": 59.0, "year": 2017, "services": 42.1, "total": 53.6, "agriculture": 57.3}
            ]


def generate_data_enrolled():
    return [(2013, 56.9), (2014, 58.0), (2015, 58.7), (2016, 58.6), (2017, 59.0)]


def b2w1_exerc_1_grading(clean_percentage):
    data = generate_data()
    data_fixed = clean_percentage(data)
    assert len(data_fixed) == 10, "Not correct. Keep trying."
    assert isinstance(data_fixed, list), "Not correct. Keep trying."

    for r in range(len(data)):
        assert isinstance(data[r], dict), "Not correct. Keep trying."
        assert len(data[r]) == 10, "Not correct. Keep trying."

        for k in data[r].keys():
            assert "(R)" not in data_fixed[r][k], "Not correct. Keep trying."
            assert re.search(r"[a-zA-Z\(\)]", data_fixed[r][k]) is None, \
                   "Not correct. Keep trying."


def b2w1_exerc_2_grading(clean_header_string, clean_header):
    data = generate_data()
    for r in range(len(data)):
        for k in data[r].keys():
            area_clean = clean_header_string(k)
            assert isinstance(area_clean, str), "Not correct. Keep trying."
            assert re.search(r"[\,\sA-Z]", area_clean) is None, \
                   "Not correct. Keep trying."

    data_fixed = clean_header(data)
    assert isinstance(data_fixed, list), "Not correct. Keep trying."
    for r in range(len(data_fixed)):
        assert isinstance(data_fixed[r], dict), "Not correct. Keep trying."
        for k in data_fixed[r].keys():
            assert isinstance(k, str), "Not correct. Keep trying."
            assert re.search(r"[\,\sA-Z]", k) is None, \
                   "Not correct. Keep trying."


def b2w1_exerc_3_grading(commas, data_types):
    data_comma = generate_data_comma()
    data_dot = commas(data_comma)
    assert isinstance(data_dot, list), "Not correct. Keep trying."
    for r in range(len(data_dot)):
        assert isinstance(data_dot[r], dict), "Not correct. Keep trying."
        for v in data_dot[r].values():
            assert isinstance(v, str), "Not correct. Keep trying."
            assert re.search(r"[\,]", v) is None, \
                   "Not correct. Keep trying."

    data_dot_type = data_types(data_dot)
    assert isinstance(data_dot_type, list), "Not correct. Keep trying."
    for r in range(len(data_dot_type)):
        assert isinstance(data_dot_type[r], dict), "Not correct. Keep trying."
        for k, v in data_dot_type[r].items():
            if k == "year":
                assert isinstance(v, int), "Not correct. Keep trying."
            else:
                assert isinstance(v, float), "Not correct. Keep trying."


def b2w1_exerc_4_grading(education_years):
    data_clean = generate_data_clean()
    education_areas = [key for key in data_clean[0].keys() if key not in ["year"]]
    for area in education_areas:
        percent_women_year = education_years(data_clean, area)
        assert isinstance(percent_women_year, list), "Not correct. Keep trying."
        assert len(percent_women_year) == 12, "Not correct. Keep trying."
        for year in percent_women_year:
            assert isinstance(year, tuple), "Not correct. Keep trying."
            assert len(year) == 2, "Not correct. Keep trying."
            assert isinstance(year[0], int), "Not correct. Keep trying."
            assert isinstance(year[1], float), "Not correct. Keep trying."

    test1 = education_years(data_clean, "total")
    assert math.isclose(test1[3][1],
                        53.5,
                        abs_tol=0.1), "Not correct. Keep trying."
    assert test1[10][0] == 2016, "Not correct. Keep trying."
    test2 = education_years(data_clean, "services")
    assert math.isclose(test2[5][1],
                        41.7,
                        abs_tol=0.1), "Not correct. Keep trying."
    assert test2[8][0] == 2014, "Not correct. Keep trying."

    source = inspect.getsource(education_years)
    assert "map" in source, "Not correct. Keep trying."
    assert "lambda" in source, "Not correct. Keep trying."


def b2w1_exerc_5_grading(female_enrolled, threshold):
    data_enrolled = generate_data_enrolled()
    data_filtered = female_enrolled(data_enrolled, 0)
    assert isinstance(data_filtered, list), "Not correct. Keep trying."
    assert len(data_filtered) == 5, "Not correct. Keep trying."
    for year in data_filtered:
        assert isinstance(year, tuple), "Not correct. Keep trying."
        assert len(year) == 2, "Not correct. Keep trying."
        assert isinstance(year[0], int), "Not correct. Keep trying."
        assert isinstance(year[1], float), "Not correct. Keep trying."

    test1 = female_enrolled(data_enrolled, 58.1)
    assert len(test1) == 3, "Not correct. Keep trying."
    assert math.isclose(test1[1][1],
                        58.7,
                        abs_tol=0.1), "Not correct. Keep trying."
    assert test1[1][0] == 2015, "Not correct. Keep trying."

    test2 = female_enrolled(data_enrolled, 58.0)
    assert len(test2) == 4, "Not correct. Keep trying."
    assert math.isclose(test2[3][1],
                        58.0,
                        abs_tol=0.1), "Not correct. Keep trying."
    assert test2[3][0] == 2014, "Not correct. Keep trying."

    source = inspect.getsource(female_enrolled)
    assert "sorted" in source, "Not correct. Keep trying."


def b2w1_exerc_6_grading(Lottery, simple_lottery, raffle_key):
    assert isinstance(simple_lottery, Lottery), "Not correct. Keep trying."
    assert hasattr(simple_lottery, "raffle_key"), "Not correct. Keep trying."
    assert simple_lottery.get_lucky(1) == "10 euros", "Not correct. Keep trying."
    assert simple_lottery.get_lucky(5) == "100 euros", "Not correct. Keep trying."
    assert simple_lottery.get_lucky(9) == "40 euros", "Not correct. Keep trying."
    assert simple_lottery.get_lucky("1") == "Better luck next time!", \
           "Not correct. Keep trying."
    assert simple_lottery.get_lucky(-3) == "Better luck next time!", \
           "Not correct. Keep trying."
    source = inspect.getsource(simple_lottery.get_lucky)
    assert "try" in source, "Not correct. Keep trying."
    assert "except" in source, "Not correct. Keep trying."
