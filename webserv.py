#!/usr/bin/env python
#Written by Stuart Anderson
#This is a python web server that listens for specific textual websocket input, parses it, then processes it.
#I run that data through my brewery program, in which it checks the day, produces booze, tries to sell booze,
#then returns the result back to an awaiting web socket on the other end.

import asyncio, websockets, random
from datetime import datetime, timedelta


class market:
    def __init__(self, data):
        self.rum_prices = 0
        self.wine_prices = 0
        self.data = data
        self.data = self.data.split(',')
        self.data = {'days':int(self.data[0]),'old':int(self.data[1]),'wine':int(self.data[2]),'rum':int(self.data[3]),'storage':int(self.data[4]),'cash':int(self.data[5])}
        print(str(self.data))
        self.start_date = datetime(2430,3,1)
        self.rem_ad = 2320
        self.date = self.start_date+timedelta(self.data['days'])
        self.date = str(self.date.month)+'-'+str(self.date.day)+'-'+str(self.date.year-self.rem_ad)+"PA"
        self.high_rum = 20
        self.high_wine = 12
        if (self.data['days']-self.data['old'])%15 == 0: self.data.update(self.production(self.data))
        self.daily_prices()
        print(self.rum_prices)
        print(self.wine_prices)
        self.inv_reduce()
        self.sales()

    def rollx(self,x):
        r = random.randint(1,x)
        if r == x:
            return r + self.roll(x)
        else:
            return r

    def roll(self,x):
        return random.randint(1,x)
        
    def market(self,x):
        return [[self.rollx(x)+4,self.roll(5000)] for i in range(self.roll(10))]

    def daily_prices(self,x=None):
        if x == 'rum':
            self.rum_prices = self.market(16)
            self.rum_prices.sort(reverse=True)
        elif x == 'wine':
            self.wine_prices = self.market(8)
            self.wine_prices.sort(reverse=True)
        else:
            self.rum_prices = self.market(16)
            self.rum_prices.sort(reverse=True)
            self.wine_prices = self.market(8)
            self.wine_prices.sort(reverse=True)
   

    def recommend(self):
        if self.data['cash'] <= 24000:
            return .1
        elif 12000 < self.data['cash'] <= 146000:
            return self.data['cash']/156000
        else:
            return 1

    def production(self,x):
        return {'old':x['days'],'wine':x['wine']+8000,'rum':x['rum']+4000,'cash':x['cash']-12000}

    def sell(self,k):
        if k == 'rum':
            self.data['cash']+=self.rum_prices[0][0]-(self.rum_prices[0][0]*.1)
            self.data['rum']-=1
            if self.rum_prices[0][1]>1:
                self.rum_prices[0][1]-=1
            else:
                self.rum_prices.remove(self.rum_prices[0])
                self.rum_prices.sort(reverse=True)
        if k == 'wine':
            self.data['cash']+=self.wine_prices[0][0]-(self.wine_prices[0][0]*.1)
            self.data['wine']-=1
            if self.wine_prices[0][1]>1:
                self.wine_prices[0][1]-=1
            else:
                self.wine_prices.remove(self.wine_prices[0])
                self.wine_prices.sort(reverse=True)

    def prices(self,x):
        if x=='rum':
            if self.rum_prices != []: return self.rum_prices[0][0]
            else: return 0
        if x=='wine':
            if self.wine_prices != []: return self.wine_prices[0][0]
            else: return 0
                

    def inv_reduce(self):
        def full(self):
            return self.data['wine']+self.data['rum'] > self.data['storage']

                    
        while full(self):
            if self.data['rum'] > 0 and self.prices('rum') > self.prices('wine')*2 and self.prices('rum') >= self.high_rum: self.sell('rum')
            elif self.prices('wine') > 2 and self.data['wine'] > 0: self.sell('wine')
            elif self.prices('rum') > 4 and self.data['rum'] > 0: self.sell('rum')
            elif self.data['wine']>0:
                self.data['wine']-=1
                self.data['cash']+=2
            else:
                self.data['rum']-=1
                self.data['cash']+=4

    def sales(self):
        while self.data['cash'] < 12000:
            if self.data['wine']>=1:
                self.sell('wine')
                
            elif self.data['rum']>=1:
                self.sell('rum')
                
        while self.data['wine']>=1 and self.high_wine * self.recommend() <= self.prices('wine') or self.data['rum']>=1 and self.high_rum * self.recommend() <= self.prices('rum'):
            if self.data['wine']>=1 and self.high_wine * self.recommend() <= self.prices('wine'):
                self.sell('wine')
            elif self.data['rum']>=1 and self.high_rum * self.recommend() <= self.prices('rum'):
                self.sell('rum')

    def __call__(self):
        return str(self.data['old'])+','+str(self.data['wine'])+','+str(self.data['rum'])+','+str(self.data['cash'])+','+str(self.date)

async def echo(websocket, path):
    async for message in websocket:
        print('RECEIVED: %s' % message)
        data = market(message)()
        await websocket.send(data)

asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8089))
asyncio.get_event_loop().run_forever()
