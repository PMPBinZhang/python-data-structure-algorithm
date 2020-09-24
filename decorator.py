from functools import wraps
import time
import os
import pickle


file_path = None


def set_decorator_para(path=None, func=None):
    global file_path
    global function_name
    file_path = path
    function_name = func


#用于每次执行完带函数后，重置filepath和function name
def reset_decorator_para_ori(fn):
    def func(*args, **kwargs):
        res = fn(*args, **kwargs)
        global file_path
        global function_name
        file_path = None
        function_name = None
        return res
    return func


def reset_decorator_para():
    global file_path
    global function_name
    file_path = None
    function_name = None


def time_cal(fn):
    def fx(*args, **kwargs):
        start = time.perf_counter()
        res = fn(*args, **kwargs)
        print(f"{fn.__name__} is over, time_cost is ", time.perf_counter() - start)
        reset_decorator_para()
        return res

    return fx


def exist_read_or_cal(fn):
    @wraps(fn)
    def fun_name(*args, **kwargs):
        if (not file_path) or (not os.path.exists(file_path)):
            res = fn(*args, **kwargs)
            # file_path不为None，则写入
            if file_path:
                # if not os.path.exists(file_path):
                #     os.makedirs(file_path)

                with open(file_path, "wb") as f:
                    pickle.dump(res, f)
        else:
            with open(file_path, "rb") as f:
                res = pickle.load(f)
        reset_decorator_para()
        return res

    return fun_name


def exist_read_or_cal_mod(file_path):
    print(file_path)
    def fn_1(fn):
        @wraps(fn)
        def fn_2(*args, **kwargs):
            if (not file_path) or (not os.path.exists(file_path)):
                res = fn(*args, **kwargs)
                # file_path不为None，则写入
                if file_path:
                    with open(file_path, "wb") as f:
                        pickle.dump(res, f)
            else:
                with open(file_path, "rb") as f:
                    res = pickle.load(f)
            return res

        return fn_2
    return fn_1