from pandas import read_csv, DataFrame, set_option
import random

def NeverHaveIEver():
    df_never = read_csv('data/NeverHaveIEver.csv', names=['Question'])
    set_option('display.max_colwidth', None)
    #count = len(df_never.index)
    #n = random.randint(0, count)
    question = df_never.sample()
    return question.Question.to_string(index=False)

def WouldYouRather():
    set_option('display.max_colwidth', None)
    df_wyr = read_csv('data/WouldYouRather.csv', names=['Question'])
    #count = len(df_wyr.index)
    #n = random.randint(0, count)
    question = df_wyr.sample()
    return question.Question.to_string(index=False)

def DrunkPictionary(category):
    df_drunk = read_csv('data/DrunkPictionary.csv', sep=';', names=['Category', 'Object'])
    rows = df_drunk[df_drunk.Category == category].sample()
    return rows.Object.to_string(index=False)
    