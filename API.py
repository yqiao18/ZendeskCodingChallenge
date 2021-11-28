import requests
import json
from collections import defaultdict


class Zendesk(object):
    data = []
    step = 25
    def requestData(self):
        url = 'https://zccasuhelp.zendesk.com/api/v2/tickets.json'
        user = 'yqiao18@asu.edu'
        password = 'GoodLuck2021!'
        response = requests.get(url, auth=(user, password))
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request.Exiting.')
            exit()
        else:
            print('Connected to Zendesk API')

        self.data = response.json()

    def handleData1(self):
        allTickets = self.data['tickets']
        n = len(allTickets)
        print('Number of total tickets: %d' % n)
        print('id    '+'       descriptions')
        print(self.step)
        for i in allTickets[self.step-25:self.step]:
            print(str(i['id'])+"           "+i['description'])
            print('\n')
        if self.step >= 100:
            self.step -= 75
        else:
            self.step += 25



    def handleData2(self, serialNum):
        allTickets = self.data['tickets']
        print('id    ' + '       descriptions')
        print(str(allTickets[serialNum-1]['id'])+"           "+allTickets[serialNum-1]['description'])


