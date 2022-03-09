from itertools import cycle
from datetime import datetime
from glob import glob

import os
import re


def time_add(time, minutes):
    org_minutes = int(time[-2:])
    org_hours = int(time[:2])

    org_minutes += minutes
    if org_minutes >= 60:
        org_hours += org_minutes // 60
        org_minutes %= 60

    org_hours = str(org_hours)
    org_minutes = str(org_minutes)

    return f'{org_hours.zfill(2)}:{org_minutes.zfill(2)}'


def cycle_to_planner(today):
    today = today.strftime("%Y%m%d")
    file_name = f'Day Planner-{today}.md'

    file_content = []
    with open(file_name, 'r') as f:
        file_content = f.readlines()
        pass

    # get cycle number and index
    cycle_line_numbers = []
    pattern = r'> (\d*) cycle'
    for i in range(len(file_content)):
        match = re.match(pattern, file_content[i])
        if match:
            temp = {
                'index': i,
                'cycle': int(match.groups()[0])
            }

            cycle_line_numbers.append(temp)

    result = file_content.copy()
    pattern = r'- \[.\] (\d*:\d*) (.*)'
    for cycle_line_number in cycle_line_numbers:
        # get base text info
        text = file_content[cycle_line_number['index']+1]
        match = re.match(pattern, text)
        time, task = match.groups()

        # generate cycle
        cycle_texts = [text, ]
        for i in range(cycle_line_number['cycle']):
            work_line = f'- [ ] {time_add(time, (i + 1) * 30)} {task}'
            break_line = f'- [ ] {time_add(time, 25 + (i * 30))} BREAK'

            cycle_texts.append(break_line)
            cycle_texts.append(work_line)

        # remove last redundant element
        cycle_texts.pop()
        cycle_text = '\n'.join(cycle_texts)
        result[cycle_line_number['index']+1] = cycle_text

    # remove cycle line
    cycle_line_numbers.reverse()
    for cycle_line_number in cycle_line_numbers:
        result.pop(cycle_line_number['index'])

    with open(file_name, 'w') as f:
        f.writelines(result)


def move_redudant_md(target_dir):
    all_planner_path = glob('./Day Planner-*.md')

    if len(all_planner_path) >= 10:
        for planner_path in all_planner_path[:-1]:
            os.rename(planner_path, target_dir + planner_path)


def clearfy_day_planner_dir():
    root_dir = '..\Planners\Day Planners'
    all_file_path = glob('..\Planners\Day Planners\*.md')
    pattern = r"Day Planner-(\d{6})\d{2}"
    for file_path in all_file_path:
        file_name = file_path.split('\\')[-1]
        match = re.match(pattern, file_name)
        target_dir, = match.groups()
        target_dir = os.path.join(root_dir, target_dir)

        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)

        os.rename(file_path, os.path.join(target_dir, file_name))

if __name__ == '__main__':
    cycle_to_planner(datetime.now())
    move_redudant_md('..\Planners\Day Planners')
    clearfy_day_planner_dir()
