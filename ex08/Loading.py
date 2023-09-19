import os
import datetime


def ft_tqdm(lst: range) -> None:
    """Progress bar for a for loop."""
    time_start = datetime.datetime.now()
    iter_total = len(lst)
    for iter_passed in range(len(lst)):
        iter_start = datetime.datetime.now()
        yield iter_passed
        iter_end = datetime.datetime.now()

        percentage = iter_passed / len(lst)
        percentage_str = f"{round(percentage*100):3}%"

        rate = 1 / ((iter_end - iter_start).total_seconds())
        rate_str = f"{rate:.2f}it/s"

        time_passed = (iter_end - time_start).total_seconds()
        hours_passed, remainder = divmod(time_passed, 3600)
        minutes_passed, seconds_passed = map(int, divmod(remainder, 60))
        time_passed_str = ""
        if hours_passed != 0:
            time_passed_str += str(hours_passed) + ":"
        time_passed_str += f"{minutes_passed:02}:{seconds_passed:02}"

        time_left = (len(lst) - iter_passed - 1) / rate
        hours_left, remainder = divmod(time_left, 3600)
        minutes_left, seconds_left = map(int, divmod(remainder, 60))
        time_left_str = ""
        if hours_left != 0:
            time_left_str += str(hours_left) + ":"
        time_left_str += f"{minutes_left:02}:{seconds_left:02}"

        count_str = f"{iter_passed + 1}/{iter_total}"

        bar_length = os.get_terminal_size().columns - 9 - len(percentage_str) \
            - len(count_str) - len(time_passed_str) - len(time_left_str) \
            - len(rate_str)
        bar = "█" * round(bar_length * percentage) \
            + " " * round(bar_length * (1 - percentage))
        print(f"{percentage_str}|{bar}| {count_str} \
[{time_passed_str}<{time_left_str}, {rate_str}]", end="\r")
