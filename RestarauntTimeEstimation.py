"""""""""
Pavel Uchamprin
Student id: 163173198
"""""""""""

import simpy
import random
from math import sqrt

def pizza_pickup(restaraunt):
    #The order is placed
        start = restaraunt.env.now
    #start cooking
        with restaraunt.oven.request() as cook:
            yield cook
            restaraunt.time_to_oven.append(restaraunt.env.now-start)

            yield restaraunt.env.timeout(10)
        #The cooking is finished after 10 min
            don=restaraunt.env.now
            restaraunt.oven_time.append(restaraunt.env.now-start)
            temperature = 150
        #the driver coming to pick up the pizza
        with restaraunt.driver.request() as uber:
            distance = 10 * sqrt(random.random())
            delivery_time = (distance / 30)*60
            yield uber
            #The time passed till driver collected it calculated
            restaraunt.delivery_time.append(restaraunt.env.now-don)
            yield restaraunt.env.timeout(delivery_time)
            #2 minute payment time
            yield restaraunt.env.timeout(2)
            #temperature of pizza when it is delivered
            restaraunt.temperature_time.append(temperature - delivery_time)
            yield restaraunt.env.timeout(2+delivery_time)
            #total time of the whole delivery
            restaraunt.total_time.append(restaraunt.env.now-start)


class Pizza:
    #initialzing variables and lists that would be filled with the values
    def __init__(self, env, oven, driver, temperature):
        self.env = env
        self.oven = oven
        self.driver= driver
        self.delivery_time=[]
        self.time_to_oven=[]
        self.oven_time=[]
        self.total_time=[]
        self.temperature_time = []
        self.temperature = temperature

def create_orders(env,restaraunt):
    #creating orders
    while True:
        env.process(pizza_pickup(restaraunt))
        yield env.timeout(random.gauss(5,0.5))

import matplotlib.pyplot as plt
import numpy as np
def main():
    #creating oven and driver and the process of cooking and delivery
    env = simpy.Environment()
    oven = simpy.Resource(env, capacity=4)
    driver = simpy.Resource(env, capacity=5)
    restaraunt = Pizza(env, oven, driver, 150)
    env.process(create_orders(env,restaraunt))
    env.run(until=180)
    print("Average time from order placement to pizza going in the oven",sum(restaraunt.time_to_oven)/len(restaraunt.time_to_oven))
    print("Average time from pizza finished cooking until delivery driver collects it",sum(restaraunt.delivery_time)/len(restaraunt.delivery_time))
    #creating 1000 attempts in order to find out the perfect value for delivery time that would be equal or less in 95% cases/
    for r in range(1000):
        for i in restaraunt.total_time:
           o= np.percentile(restaraunt.total_time, [95.0])
    print(" 95% of pizzas are delivered within", o, "minutes or less")
    print("Average total time from order placement to delivery",sum(restaraunt.total_time)/len(restaraunt.total_time))
    print("Average temperature at delivery",sum(restaraunt.temperature_time) / len(restaraunt.temperature_time))
    #Creating histograms
    plt.hist(restaraunt.time_to_oven,bins=15, alpha=0.5)
    plt.title('Average time from order placement to pizza going in the oven')
    plt.xlabel('Minutes')
    plt.show()
    plt.hist(restaraunt.delivery_time, bins=15, alpha=0.5)
    plt.title('Average time from pizza finished cooking until delivery driver collects it')
    plt.xlabel('Minutes')
    plt.show()
    plt.hist(restaraunt.total_time, bins=15, alpha=0.5)
    plt.title('Average total time from order placement to delivery')
    plt.xlabel('Minutes')
    plt.show()
    plt.hist(restaraunt.temperature_time,bins=15, alpha=0.5)
    plt.title('Average temperature at delivery')
    plt.xlabel('Minutes')
    plt.show()
main()


"""""""""
Part B
 for r in range(1000):
        for i in restaraunt.total_time:
           o= np.percentile(restaraunt.total_time, [95.0])
    print(o)
I used numpy to go through 1000 total time lists to find out a value that is greater than 95% of the values.
The value is approximately [62.89186272] which means that value could be used as the total amount of time or less in 95% cases it would take to perform the whole delivery.
"""""""""""
