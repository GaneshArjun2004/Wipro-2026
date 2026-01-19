import time

def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("[LOG] Method", func.__name__, "executed successfully")
        return result
    return wrapper

def admin_only(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("is_admin", False):
            return func(*args, **kwargs)
        print("Access Denied: Admin privileges required")
    return wrapper

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start, "seconds")
        return result
    return wrapper
