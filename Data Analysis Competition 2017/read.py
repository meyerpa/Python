# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:16:47 2017

@author: Paige
Description: File that reads and cleans all of the .csv files.
"""

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
import numpy as np

#GET DATA
def read_interactions(output='Type_Material Goods', test_size=0.25):
    """Reads Interactions (with binaries).csv, and cleans the data.
    
    parameters
    ----------
    output : string
        The outcome (will be y-value)
    test_size: float, optional
        The percentage size of the test group. Default is 25%.
        
    returns
    -------
    X_train : pandas dataframe
        The x training variables
    X_test : pandas dataframe
        The x testing variables
    y_train : pandas dataframe
        The y training variables
    y_test : pandas dataframe
        The y testing variables    
    
    """
    # get X and y data
    df = pd.read_csv("Upd_Interactions (with binaries).csv", delimiter=",")
    df = df.drop_duplicates() # ensure no duplicates
    df = df.dropna()               # drop na
    df.HOH.replace(('Y', 'N'), (1, 0), inplace=True) # change head of household to binary
    #df['Property'] = df['Property'].map(lambda x: x.replace('-',''))
    y = df[output].to_frame()
    X = df.drop(output, 1)
    
    # Get training data to be random 75% and 
    # Testing data to be other 25% 
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42)
    
    return (X_train, X_test, y_train, y_test)


def read_events(output='Event', test_size=0.25):
    """Reads Events (with binaries).csv, and cleans the data.
    
    parameters
    ----------
    output : string
        The outcome (will be y-value)
    test_size: float, optional
        The percentage size of the test group. Default is 25%.
        
    returns
    -------
    X_train : pandas dataframe
        The x training variables
    X_test : pandas dataframe
        The x testing variables
    y_train : pandas dataframe
        The y training variables
    y_test : pandas dataframe
        The y testing variables    
    
    """
    # get X and y data
    df = pd.read_csv("Events (with binaries).csv", delimiter=",")
    df = df.drop_duplicates() # ensure no duplicates
    y = df[output].to_frame()
    X = df.drop(output, 1)
    # feature_names = list(X)
    
    # Get training data to be random 75% and 
    # Testing data to be other 25% 
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42)
    
    return (X_train, X_test, y_train, y_test)

    
def read_train(output="Negative"):
    """Reads Test-Services.csv, and cleans the data.
    
    parameters
    ----------
    output : string
        The outcome (will be y-value)
        
    returns
    -------
    X_train : pandas dataframe
        The x training variables
    X_test : pandas dataframe
        The x testing variables
    y_train : pandas dataframe
        The y training variables
    y_test : pandas dataframe
        The y testing variables    
    
    """
    
    # get X and y data
    df = pd.read_csv("Train Cases.csv", delimiter=",")
    df = df.drop_duplicates() # ensure no duplicates
    #df.HOH.replace(('Y', 'N'), (1, 0), inplace=True) # change head of household to binary
    df['PropCode'] = df['PropCode'].map(lambda x: x.replace('-',''))
    
    # replace shitty values
    df.UnitType.replace(('Tax Credit', 'Market Rate', 'Home Unit'), (1, 0, 2), inplace=True)
    df['Type of Service'] = df['Type of Service'].replace(
            ('Partner', 'None', 'Resident Connections'), (2, 1, 0))
    df['Services Available'] = df['Services Available'].replace(
            ('Y', 'N'), (1, 0))
    df = df.drop('Service Units', 1)
    df['ServiceUnits'] = df['ServiceUnits'].apply(lambda x: x if not x=="" else 0)
    df = df.drop('Service end year', 1)
    df = df.drop('Type of service 2', 1)
    df = df.drop('Service Units 2', 1)
    df = df.drop('Service start year 2', 1)
    df = df.drop('Service end year 2', 1)
    
    df['Aeon Services Available'].replace(('Y', 'N'), (1, 0), inplace=True)
    
    df['Late Fees?'].replace(('Y', 'N'), (1, 0), inplace=True)
    
    df = df.drop('Gender', 1)
    
    df = df.drop('Military', 1)
    df = df.drop('Disability', 1)
    df = df.drop('Immigrant', 1)
    df = df.drop('Homeless', 1)
    df = df.drop('Simplified Race', 1)
    #df['Simplified Race'].replace(('White', 'Black', 'NA', 'Decline'), (2, 0, 1, 1), inplace=True)
    df = df.drop('PrimaryIncome', 1)
    
    df['Marital Status'].replace(('S', 'M', 'Sep'), (1, 0, 2), inplace=True)
    df['Criminal Record'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Felon?'].replace(('Y', 'N'), (1, 0), inplace=True)
    #df.UnitType.replace(('Tax Credit', 'Market Rate'), (1, 0), inplace=True)
    #df.UnitType.replace(('Tax Credit', 'Market Rate'), (1, 0), inplace=True)
    print(df.shape)
    df.fillna(df.mean(), inplace=True)
    #df = df.interpolate()
    #df = df.dropna()               # drop na
    print(df.shape)    
    
    y = df[output].to_frame()
    X = df.drop(output, 1)

    
    return (X, y)
    
def read_test():
    """Reads Test Cases.csv, and cleans the data.
    
    parameters
    ----------
    none
        
    returns
    -------
    X_train : pandas dataframe
        The x training variables
    X_test : pandas dataframe
        The x testing variables
    y_train : pandas dataframe
        The y training variables
    y_test : pandas dataframe
        The y testing variables    
    
    """
    # get X and y data
    df = pd.read_csv("Test Cases.csv", delimiter=",")
    #df.HOH.replace(('Y', 'N'), (1, 0), inplace=True) # change head of household to binary
    df['PropCode'] = df['PropCode'].map(lambda x: x.replace('-',''))
    
    # replace shitty values
    df.UnitType.replace(('Tax Credit', 'Market Rate', 'Home Unit'), (1, 0, 2), inplace=True)
    df['Type of Service'] = df['Type of Service'].replace(
            ('Partner', 'None', 'Resident Connections'), (2, 1, 0))
    df['Services Available'] = df['Services Available'].replace(
            ('Y', 'N'), (1, 0))
    df = df.drop('Service Units', 1)
    df['ServiceUnits'] = df['ServiceUnits'].apply(lambda x: x if not x=="" else 0)
    df = df.drop('Service end year', 1)
    df = df.drop('Type of service 2', 1)
    df = df.drop('Service Units 2', 1)
    df = df.drop('Service start year 2', 1)
    df = df.drop('Service end year 2', 1)
    
    df['Aeon Services Available'].replace(('Y', 'N'), (1, 0), inplace=True)
    
    df['Late Fees?'].replace(('Y', 'N'), (1, 0), inplace=True)
    
    df = df.drop('Gender', 1)
    
    df = df.drop('Military', 1)
    df = df.drop('Disability', 1)
    df = df.drop('Immigrant', 1)
    df = df.drop('Homeless', 1)
    df = df.drop('Simplified Race', 1)
    #df['Simplified Race'].replace(('White', 'Black', 'NA', 'Decline'), (2, 0, 1, 1), inplace=True)
    df = df.drop('PrimaryIncome', 1)
    
    df['Marital Status'].replace(('S', 'M', 'Sep'), (1, 0, 2), inplace=True)
    df['Criminal Record'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Felon?'].replace(('Y', 'N'), (1, 0), inplace=True)
    #df.UnitType.replace(('Tax Credit', 'Market Rate'), (1, 0), inplace=True)
    #df.UnitType.replace(('Tax Credit', 'Market Rate'), (1, 0), inplace=True)
    df.fillna(0, inplace=True)
    return df

def read_train_test(output="Late Fees?", test_size=0.25):
    """Reads Train-Test Cases Combined.csv, and cleans the data.
    
    parameters
    ----------
    output : string
        The outcome (will be y-value)
    test_size: float, optional
        The percentage size of the test group. Default is 25%.
        
    returns
    -------
    X_train : pandas dataframe
        The x training variables
    X_test : pandas dataframe
        The x testing variables
    y_train : pandas dataframe
        The y training variables
    y_test : pandas dataframe
        The y testing variables    
    
    """
    # get X and y data
    df = pd.read_csv("Train-Test Cases Combined.csv", delimiter=",")
    df = df.drop_duplicates() # ensure no duplicates
    #df.HOH.replace(('Y', 'N'), (1, 0), inplace=True) # change head of household to binary
    df['PropCode'] = df['PropCode'].map(lambda x: x.replace('-',''))
    
    # replace shitty values
    df.UnitType.replace(('Tax Credit', 'Market Rate', 'Home Unit'), (1, 0, 2), inplace=True)
    df['Type of Service'] = df['Type of Service'].replace(
            ('Partner', 'None', 'Resident Connections'), (2, 1, 0))
    df['Services Available'] = df['Services Available'].replace(
            ('Y', 'N'), (1, 0))
    df = df.drop('Service Units', 1)
    df['ServiceUnits'] = df['ServiceUnits'].apply(lambda x: x if not x=="" else 0)
    df = df.drop('Service end year', 1)
    df = df.drop('Type of service 2', 1)
    df = df.drop('Service start year 2', 1)
    df = df.drop('Service end year 2', 1)
    
    df['Aeon Services Available'].replace(('Y', 'N'), (1, 0), inplace=True)
    
    df['Late Fees?'].replace(('Y', 'N'), (1, 0), inplace=True)
    
    df = df.drop('Gender', 1)
    
    df = df.drop('Military', 1)
    df = df.drop('Disability', 1)
    df = df.drop('Immigrant', 1)
    df = df.drop('Homeless', 1)
    df = df.drop('Simplified Race', 1)
    #df['Simplified Race'].replace(('White', 'Black', 'NA', 'Decline'), (2, 0, 1, 1), inplace=True)
    df = df.drop('PrimaryIncome', 1)
    df = df.drop('Negative', 1)
    
    df['Marital Status'].replace(('S', 'M', 'Sep'), (1, 0, 2), inplace=True)
    df['Criminal Record'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Felon?'].replace(('Y', 'N'), (1, 0), inplace=True)
    #df.UnitType.replace(('Tax Credit', 'Market Rate'), (1, 0), inplace=True)
    #df.UnitType.replace(('Tax Credit', 'Market Rate'), (1, 0), inplace=True)
    print(df.shape)
    df.fillna(df.mean(), inplace=True)
    #df = df.interpolate()
    #df = df.dropna()               # drop na
    print(df.shape)    
    
    y = df[output].to_frame()
    X = df.drop(output, 1)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size)
    
    return (X_train, X_test, y_train, y_test)
    
    
def read_services(output="Negative", test_size=0.25, filter_category=None,
                  filter_value=None):
    """Reads Services and Outcome.csv, and cleans the data.
    
    parameters
    ----------
    output : string
        The outcome (will be y-value)
    test_size: float, optional
        The percentage size of the test group. Default is 25%.
        
    returns
    -------
    X_train : pandas dataframe
        The x training variables
    X_test : pandas dataframe
        The x testing variables
    y_train : pandas dataframe
        The y training variables
    y_test : pandas dataframe
        The y testing variables    
    
    """
    # get X and y data
    df = pd.read_csv("Services and Outcome.csv", delimiter=",")
    df = df.drop_duplicates() # ensure no duplicates
    #df.HOH.replace(('Y', 'N'), (1, 0), inplace=True) # change head of household to binary
    df['PropCode'] = df['PropCode'].map(lambda x: x.replace('-',''))
    
    # replace shitty values
    df.UnitType.replace(('Tax Credit', 'Market Rate', 'Home Unit'), (1, 0, 2), inplace=True)
    df['Type of Service'] = df['Type of Service'].replace(
            ('Partner', 'None', 'Resident Connections'), (2, 1, 0))
    df['Services Available'] = df['Services Available'].replace(
            ('Y', 'N'), (1, 0))
    df = df.drop('Service Units', 1)
    df['ServiceUnits'] = df['ServiceUnits'].apply(lambda x: x if not x=="" else 0)
    df = df.drop('Type of service 2', 1)
    df['Aeon Services Available'].replace(('Y', 'N'), (1, 0), inplace=True)
    
    df['Late Fees?'].replace(('Y', 'N'), (1, 0), inplace=True)
    
    df = df.drop('Number of units 2', 1)
    df = df.drop('Gender', 1)
    df = df.drop('Military', 1)
    df = df.drop('Disability', 1)
    df = df.drop('Immigrant', 1)
    df = df.drop('Homeless', 1)
    df = df.drop('Simplified Race', 1)
    #df['Simplified Race'].replace(('White', 'Black', 'NA', 'Decline'), (2, 0, 1, 1), inplace=True)
    df = df.drop('PrimaryIncome', 1)
    
    df['Marital Status'].replace(('S', 'M', 'Sep'), (1, 0, 2), inplace=True)
    df['Criminal Record'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Felon?'].replace(('Y', 'N'), (1, 0), inplace=True)
    
    df['Material Good Request?'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Back to School Supplies?'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Bus Cards?'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Clothing?'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Coats?'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Food?'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Furniture?'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Gift Card?'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Household Goods?'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Toys for Tots?'].replace(('Y', 'N'), (1, 0), inplace=True)
    df['Welcome Basket?'].replace(('Y', 'N'), (1, 0), inplace=True)
    
    # get rid of user-defined filter
    if filter_category != None:
        #df[filter_category] = df[filter_category].fillna(df[filter_category].mean())
        df = df[ df[filter_category]==filter_value ]
    print(df.shape)
    df.fillna(df.mean(), inplace=True)
    #df = df.interpolate()
    #df = df.dropna()               # drop na
    print(df.shape)    
    
    y = df[output].to_frame()
    X = df.drop(output, 1)

    
    return X, y
    