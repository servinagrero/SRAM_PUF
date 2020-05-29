#!/usr/bin/python

import csv


def extract_board_params(board_id):
    '''Returns the boards parameters from the board id'''
    return {'Board': board_id,
            'Wafer': board_id[2:4],
            'Lot': board_id[4:18],
            'Y': int(board_id[18:20], 16),
            'X': int(board_id[20:22], 16)}


csv_in = open('./database_raw.csv', 'r')
db_file = open('./exported_dumps.csv', 'w+')

reader = csv.DictReader(csv_in, quotechar='"')
fields = [
    "_id", "board_id", "wafer", "lot", "Y", "X",
    "mem_pos",
    "temp", "vdd", "temp_cal_30", "temp_cal_110", "vrefint_cal",
    "length", "timestamp", "data"
]

csv_out = csv.DictWriter(db_file,
                         delimiter=',',
                         fieldnames=fields,
                         quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_out.writeheader()

for line in reader:
    board_params = extract_board_params(str(line['board_id']))

    csv_out.writerow({
        fields[0]: line['_id'],
        fields[1]: board_params['Board'],
        fields[2]: board_params['Wafer'],
        fields[3]: board_params['Lot'],
        fields[4]: board_params['Y'],
        fields[5]: board_params['X'],
        fields[6]: line['mem_pos'],
        fields[7]: line['temp'],
        fields[8]: line['vdd'],
        fields[9]: line['temp_cal_30'],
        fields[10]: line['temp_cal_110'],
        fields[11]: line['vrefint_cal'],
        fields[12]: line['length'],
        fields[13]: line['timestamp'],
        fields[14]: line['data']
        })

    print(f'Inserted {line["_id"]}')
