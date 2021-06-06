import math
import sys


#ipython = get_ipython()


#def hide_traceback(exc_tuple=None, filename=None, tb_offset=None,
#                   exception_only=False, running_compiled_code=False):
#    etype, value, tb = sys.exc_info()
#    return ipython._showtraceback(etype, value, ipython.InteractiveTB.get_exception_only(etype, value))


# Uncomment after tests
#ipython.showtraceback = hide_traceback


def generate_data():
    return [{"animal_name": "gull", "hair": 0, "feathers": "?", "eggs": 1, "milk": 0, "aquatic": "?", "toothed": 0, "fins": 0, "legs": 2, "class_type": "Bird"},
            {"animal_name": "hare", "hair": 1, "feathers": "0", "eggs": 0, "milk": 1, "aquatic": "0", "toothed": 1, "fins": 0, "legs": 4, "class_type": "Mammal"},
            {"animal_name": "gull", "hair": 0, "feathers": "?", "eggs": 1, "milk": 0, "aquatic": "?", "toothed": 0, "fins": 0, "legs": 2, "class_type": "Bird"},
            {"animal_name": "pheasant", "hair": 0, "feathers": "?", "eggs": 1, "milk": 0, "aquatic": "0", "toothed": 0, "fins": 0, "legs": 2, "class_type": "Bird"},
            {"animal_name": "cavy", "hair": 1, "feathers": "0", "eggs": 0, "milk": 1, "aquatic": "0", "toothed": 1, "fins": 0, "legs": 4, "class_type": "Mammal"},
            {"animal_name": "haddock", "hair": 0, "feathers": "0", "eggs": 1, "milk": 0, "aquatic": "?", "toothed": 1, "fins": 1, "legs": 0, "class_type": "Fish"},
            {"animal_name": "crow", "hair": 0, "feathers": "?", "eggs": 1, "milk": 0, "aquatic": "0", "toothed": 0, "fins": 0, "legs": 2, "class_type": "Bird"},
            {"animal_name": "wren", "hair": 0, "feathers": "?", "eggs": 1, "milk": 0, "aquatic": "0", "toothed": 0, "fins": 0, "legs": 2, "class_type": "Bird"},
            {"animal_name": "calf", "hair": 1, "feathers": "0", "eggs": 0, "milk": 1, "aquatic": "0", "toothed": 1, "fins": 0, "legs": 4, "class_type": "Mammal"},
            {"animal_name": "hawk", "hair": 0, "feathers": "?", "eggs": 1, "milk": 0, "aquatic": "0", "toothed": 0, "fins": 0, "legs": 2, "class_type": "Bird"},
            {"animal_name": "giraffe", "hair": 1, "feathers": "0", "eggs": 0, "milk": 1, "aquatic": "0", "toothed": 1, "fins": 0, "legs": 4, "class_type": "Mammal"}]


def generate_data_replaced():
    data = generate_data()
    data_replaced = [{k: v.replace('?', '1') if isinstance(v, str) else v
                     for k, v in animal.items()}
                     for animal in data]
    return data_replaced


def generate_data_int():
    data = generate_data_replaced()
    data_int = [{k: int(v) if isinstance(v, str) and v.isdigit() else v
                for k, v in animal.items()}
                for animal in data]
    return data_int


def generate_data_lower():
    data = generate_data_int()
    data_lower = [{k: v.lower() if k == 'class_type' else v
                  for k, v in animal.items()}
                  for animal in data]
    return data_lower


def b2w2_exerc_1_grading(replace_unknown):
    columns = list(generate_data()[0].keys())
    data_replaced = replace_unknown(generate_data())
    assert len(data_replaced) == 11, "Not correct. Keep trying."
    assert isinstance(data_replaced, list), "Not correct. Keep trying."
    for animal in data_replaced:
        assert isinstance(animal, dict), "Not correct. Keep trying."
        assert len(animal) == 10, "Not correct. Keep trying."

        for k, v in animal.items():
            if isinstance(v, str):
                assert "?" not in v, "Not correct. Keep trying."
            assert k in columns, "Not correct. Keep trying."
            if k == "feathers":
                assert isinstance(v, str), "Not correct. Keep trying."
            elif k == "eggs":
                assert isinstance(v, int), "Not correct. Keep trying."
            elif k == "aquatic":
                assert isinstance(v, str), "Not correct. Keep trying."

    assert data_replaced[0]["feathers"] == "1", "Not correct. Keep trying."
    assert data_replaced[1]["feathers"] == "0", "Not correct. Keep trying."
    assert data_replaced[1]["legs"] == 4, "Not correct. Keep trying."
    assert data_replaced[0]["feathers"] == "1", "Not correct. Keep trying."
    assert data_replaced[8]["aquatic"] == "0", "Not correct. Keep trying."
    assert data_replaced[5]["aquatic"] == "1", "Not correct. Keep trying."


def b2w2_exerc_2_grading(convert_int):
    columns = list(generate_data_replaced()[0].keys())
    data_replaced = generate_data_replaced()
    data_int = convert_int(data_replaced)

    assert len(data_int) == 11, "Not correct. Keep trying."
    assert isinstance(data_int, list), "Not correct. Keep trying."
    for animal in data_int:
        assert isinstance(animal, dict), "Not correct. Keep trying."
        assert len(animal) == 10, "Not correct. Keep trying."

        for k, v in animal.items():
            if isinstance(v, str):
                assert "?" not in v, "Not correct. Keep trying."
            assert k in columns, "Not correct. Keep trying."
            if k in ["animal_name", "class_type"]:
                assert isinstance(v, str), "Not correct. Keep trying."
            else:
                assert isinstance(v, int), "Not correct. Keep trying."

    assert data_int[0]["feathers"] == 1, "Not correct. Keep trying."
    assert data_int[1]["feathers"] == 0, "Not correct. Keep trying."
    assert data_int[1]["legs"] == 4, "Not correct. Keep trying."
    assert data_int[0]["feathers"] == 1, "Not correct. Keep trying."
    assert data_int[8]["aquatic"] == 0, "Not correct. Keep trying."
    assert data_int[5]["aquatic"] == 1, "Not correct. Keep trying."


def b2w2_exerc_3_grading(lower_class):
    columns = list(generate_data_replaced()[0].keys())
    data_int = generate_data_int()
    data_class = lower_class(data_int)

    assert len(data_class) == 11, "Not correct. Keep trying."
    assert isinstance(data_class, list), "Not correct. Keep trying."
    for animal in data_class:
        assert isinstance(animal, dict), "Not correct. Keep trying."
        assert len(animal) == 10, "Not correct. Keep trying."

        for k, v in animal.items():
            if isinstance(v, str):
                assert "?" not in v, "Not correct. Keep trying."
            assert k in columns, "Not correct. Keep trying."
            if k in ["animal_name", "class_type"]:
                assert isinstance(v, str), "Not correct. Keep trying."
            else:
                assert isinstance(v, int), "Not correct. Keep trying."

            if k == "class_type":
                assert v.lower() == v, "Not correct. Keep trying."

    assert data_class[0]["feathers"] == 1, "Not correct. Keep trying."
    assert data_class[1]["feathers"] == 0, "Not correct. Keep trying."
    assert data_class[1]["legs"] == 4, "Not correct. Keep trying."
    assert data_class[0]["feathers"] == 1, "Not correct. Keep trying."
    assert data_class[8]["aquatic"] == 0, "Not correct. Keep trying."
    assert data_class[5]["aquatic"] == 1, "Not correct. Keep trying."


def b2w2_exerc_4_grading(order_animals):
    data_lower = generate_data_lower()
    data_order = order_animals(data_lower)
    assert isinstance(data_order, list), "Not correct. Keep trying."
    assert len(data_order) == 11, "Not correct. Keep trying."
    for animal in data_order:
        assert len(animal) == 3, "Not correct. Keep trying."
        assert isinstance(animal[0], str), "Not correct. Keep trying."
        assert isinstance(animal[1], str), "Not correct. Keep trying."
        assert isinstance(animal[2], int), "Not correct. Keep trying."

    assert data_order[3][0] == "pheasant", "Not correct. Keep trying."
    assert data_order[6][0] == "hawk", "Not correct. Keep trying."
    assert data_order[-1][0] == "giraffe", "Not correct. Keep trying."
    assert data_order[0][1] == "fish", "Not correct. Keep trying."
    assert data_order[4][1] == "bird", "Not correct. Keep trying."
    assert data_order[-2][1] == "mammal", "Not correct. Keep trying."
    assert data_order[0][2] == 0, "Not correct. Keep trying."
    assert data_order[6][2] == 2, "Not correct. Keep trying."
    assert data_order[-1][2] == 4, "Not correct. Keep trying."


def b2w2_exerc_5_grading(mammals_letters):
    data_lower = generate_data_lower()
    data_letters = mammals_letters(data_lower)
    assert isinstance(data_letters, float), "Not correct. Keep trying."
    assert math.isclose(data_letters,
                        4.75,
                        abs_tol=0.01), "Not correct. Keep trying."


def b2w2_exerc_6_grading(Animal):
    test1 = Animal("Duck", "bird", True)
    assert isinstance(test1.lay_eggs(), int), "Not correct. Keep trying."
    assert test1.lay_eggs() >= 0, "Not correct. Keep trying."
    assert test1.lay_eggs() <= 10, "Not correct. Keep trying."

    test2 = Animal("Dolphin", "mammal", False)
    assert isinstance(test2.lay_eggs(), str), "Not correct. Keep trying."
    assert test2.lay_eggs() == "I can't lay eggs...", "Not correct. Keep trying."
