import math
import sys


#ipython = get_ipython()


#def hide_traceback(exc_tuple=None, filename=None, tb_offset=None,
#                   exception_only=False, running_compiled_code=False):
#    etype, value, tb = sys.exc_info()
#    return ipython._showtraceback(etype, value, ipython.InteractiveTB.get_exception_only(etype, value))


# Uncomment after tests
#ipython.showtraceback = hide_traceback


# No picking
def exercise_1(answers):
    solution = {"question_1": 3, "question_2": 3, "question_3":2,"question_4":4,"question_5":1, "question_6": 1, "question_7": 4, "question_8":2,"question_9":2,"question_10":1, "question_11": 2, "question_12": 3, "question_13":4,"question_14":1}
    common_pairs = dict()
    for key in answers:
        if (key in solution and answers[key] == solution[key]):
            common_pairs[key] = answers[key]

    assert len(common_pairs)==14, "You have "+ str(14- len(common_pairs))+" incorrect answer. The answers you were correct are: \n"+str((common_pairs))

    print("Answer is correct. Good Job.")


