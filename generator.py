# -*- coding: utf-8 -*-
"""
Created on Thu Apr 09 18:21:33 2015

@author: Ed
"""

import random

def readNames(filename):
    f = open(filename, "r")
    global lines
    global columns
    lines = f.readlines()
    global boyNames
    boyNames = []
    global girlNames
    girlNames = []
    for line in lines:
        columns = line.split()
        boyNames.append(columns[0])
        girlNames.append(columns[1])
    f.close()

def chargen(verbose=0): #The function that will roll a character and define their name
    if(verbose==1):
        print "Generating a new character..."
        print "Opening default name file..."
    readNames("names.txt")
    gender = random.choice(['male','female'])
    if(gender=='male'):
        #name = random.choice(['Alfred', 'Ben', 'Collin', 'Dave'])
        name = random.choice(boyNames)
    else:
        #name = random.choice(['Alice','Becky','Chloe','Dianna'])
        name = random.choice(girlNames)
    Rolls = []
    for y in range(0,7):
        Rolls.append(random.randint(1,6)+random.randint(1,6)+random.randint(1,6))
    if(Rolls[5] <= 2):
        comMod = -8
    elif(Rolls[5] == 3):
        comMod = -5
    elif(Rolls[5] <= 5):
        comMod = -3
    elif(Rolls[5] <= 8):
        comMod = -1
    elif(Rolls[5] <= 12):
        comMod = 0
    elif(Rolls[5] <= 15):
        comMod = 1
    elif(Rolls[5] <= 17):
        comMod = 2
    elif(Rolls[5] == 18):
        comMod = 3
    else:
        comMod = 5
    Rolls[6] += comMod
    NewVillager = {}
    NewVillager["Name"] = name
    NewVillager["Gender"] = gender
    NewVillager["Strength"] = Rolls[0]
    NewVillager["Dexterity"] = Rolls[1]
    NewVillager["Constitution"] = Rolls[2]
    NewVillager["Intelligence"] = Rolls[3]
    NewVillager["Wisdom"] = Rolls[4]
    NewVillager["Charisma"] = Rolls[5]
    NewVillager["Comeliness"] = Rolls[6]
    villagers.append(NewVillager)
    return villagers
    
global villagers
villagers = []