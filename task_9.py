#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    while wall_is_above() or wall_is_beneath():
        move_right()
        if not wall_is_above() and wall_is_beneath():
            fill_cell()

    pass


if __name__ == '__main__':
    run_tasks()


