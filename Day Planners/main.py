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


def turn_to_planner(today):
    today = today.strftime("%Y%m%d")
    file_name = f'Day Planner-{today}.md'

    file_content = []
    with open(file_name, 'r') as f:
        file_content = f.readlines()
        pass

    # get turn number and index
    turn_line_numbers = []
    pattern = r'> (\d*) turn'
    for i in range(len(file_content)):
        match = re.match(pattern, file_content[i])
        if match:
            temp = {
                'index': i,
                'turn': int(match.groups()[0])
            }

            turn_line_numbers.append(temp)

    result = file_content.copy()
    pattern = r'- \[.\] (\d*:\d*) (.*)'
    for turn_line_number in turn_line_numbers:
        # get base text info
        text = file_content[turn_line_number['index']+1]
        match = re.match(pattern, text)
        time, task = match.groups()

        # generate turn
        turn_texts = [text, ]
        for i in range(turn_line_number['turn']):
            work_line = f'- [ ] {time_add(time, (i + 1) * 30)} {task}'
            break_line = f'- [ ] {time_add(time, 25 + (i * 30))} BREAK'

            turn_texts.append(break_line)
            turn_texts.append(work_line)

        # remove last redundant element
        turn_texts.pop()
        turn_text = '\n'.join(turn_texts)
        result[turn_line_number['index']+1] = turn_text

    # remove turn line
    turn_line_numbers.reverse()
    for turn_line_number in turn_line_numbers:
        result.pop(turn_line_number['index'])

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
    turn_to_planner(datetime.now())
    move_redudant_md('..\Planners\Day Planners')
    clearfy_day_planner_dir()
