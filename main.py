import os

import requests, bs4
import csv

import abgefangeneBaelle, abgewehrteElfmeter, abgewehrteSchuesse, balleroberungen, ballverluste
import begangeneFouls, cleanSheet, erfolgreicheDribblings, error, flanken
import geblockteBaelle, geklaerteBaelle, grosschancenKreiert, grosschancenPariert
import luftkampf, paraden, passquote, schussgenauigkeit, shotOnTarget, tackling
import torschussvorlagen, transfermarkt, zweikampf, merge

bots = ['abgefangeneBaelle', 'abgewehrteElfmeter', 'abgewehrteSchuesse', 'balleroberungen', 'ballverluste',
        'begangeneFouls', 'cleanSheet', 'erfolgreicheDribblings', 'error', 'flanken', 'geblockteBaelle', 'geklaerteBaelle',
        'grosschancenKreiert', 'grosschancenPariert', 'luftkampf', 'paraden', 'passquote', 'schussgenauigkeit',
        'shotOnTarget', 'tackling', 'torschussvorlagen', 'transfermarkt', 'zweikampf', 'merge']

modules = map(__import__, bots)

import multiprocessing

multiprocessing.Process(target=modules)


os.remove('abgefangeneBaelle.csv')
os.remove('abgewehrteElfmeter.csv')
os.remove('abgewehrteSchuesse.csv')
os.remove('balleroberungen.csv')
os.remove('ballverluste.csv')
os.remove('begangeneFouls.csv')
os.remove('cleanSheet.csv')
os.remove('erfolgreicheDribblings.csv')
os.remove('error.csv')
os.remove('flanken.csv')
os.remove('geblockteBaelle.csv')
os.remove('geklaerteBaelle.csv')
os.remove('grosschancenKreiert.csv')
os.remove('grosschancenPariert.csv')
os.remove('luftkampf.csv')
os.remove('paraden.csv')
os.remove('passquote.csv')
os.remove('schussgenauigkeit.csv')
os.remove('shotOnTarget.csv')
os.remove('tackling.csv')
os.remove('torschussvorlagen.csv')
os.remove('transfermarkt.csv')
os.remove('zweikampf.csv')
os.remove('22.csv')




