import json

def main():
    data = read_json('data.json')

    for item in data:
        if item['StationID'] == '1715':
            print('車種：' + item['TrainTypeName']['Zh_tw'])
            print('車次：' + item['TrainTypeID'])

            print('預計到站時間：' + item['ScheduledArrivalTime'])
            print('預計離站時間：' + item['ScheduledDepartureTime'])

            print('預估誤點：' + str(item['DelayTime']) + ' 分鐘')

def read_json(filename):
    with open(filename, 'r', encoding='utf8') as data_file:
        data = json.load(data_file)

    return data


if __name__ == "__main__":
    main()