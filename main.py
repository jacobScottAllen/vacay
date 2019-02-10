import csv
from datetime import timedelta, datetime

config = {
    'vacation_days': "./vacation_days.csv",
    'current_accrual': 40,
    'biweekly_accrual': 4.62,
    'next_accrual_date': datetime(2019, 2, 22)
}

class VacationDay:
    def __init__(self):
        self.name = None
        self.date = None

def main():
    vacation_days = list()

    with open(config['vacation_days']) as csv_file: 

        planned_vacation_days = csv.reader(csv_file)
        for line in planned_vacation_days:
            this_vacation_date = VacationDay()
            this_vacation_date.name = line[0]
            this_vacation_date.date = datetime.strptime(line[1].strip(), '%Y-%m-%d')

            vacation_days.append(this_vacation_date)

    vacation_days.sort(key= lambda x: x.date)

    bookmark_accrual = config['current_accrual'] # accrual since last accrual date
    bookmark_accrual_date = config['next_accrual_date'] # date of last accural date before date being analyzed
    for vacation_day in vacation_days:
        # figure out the last accrual date before the date being analyzed, and what the accrual is to that point
        time_since_last_accrual_date = vacation_day.date - bookmark_accrual_date
        while time_since_last_accrual_date.days >= 14:
            bookmark_accrual += config['biweekly_accrual']
            bookmark_accrual_date += timedelta(days=14)
            time_since_last_accrual_date = vacation_day.date - bookmark_accrual_date

        bookmark_accrual -= 8
        if bookmark_accrual <= 0:
            print(vacation_day.name + ' on ' + str(vacation_day.date) + ' caused accrual to be ' + str(bookmark_accrual))
        

    print(str(bookmark_accrual) + ' hours left')
        

def print_vacation_days(vacation_days):
    for vacation_day in vacation_days:
        print(vacation_day.date)

    


if __name__ == '__main__':
    main()