def task_1() -> None:
    is_integer: int = 10
    is_float: float = 15.5
    is_string: str = 'Test'
    is_list: list = [1, 2, 3, 'Test']
    is_bool: bool = True
    print(type(is_integer))
    print(type(is_float))
    print(type(is_string))
    print(type(is_list))
    print(type(is_bool))


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])


def task_3(a: int) -> int:
    return a*a


task_1()
task_2()
print(task_3(3))
