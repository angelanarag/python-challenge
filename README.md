# python-challenge
Module 3 assignment

Submitted by Angela Narag

The python-challenge repository contains two other folders: 
    PyBank          PyPoll
In each PyBank and PyPoll, each folder contains two other folders and a python script:
    Resources       analysis        main.py

The Resources folder contain the financial dataset in .csv format to use for each python script:
    PyBank/Resources contain the budget_data.csv 
    PyPoll/Resources contain the election_data.csv

The analysis folder will receive the output file once each python script successfully runs:
    PyBank/analysis will receive the budget_output.txt
    PyPoll/analysis will receive the election_output.txt
The output files will get overwritten each time the python script runs. The analysis folders will only be empty if you have never run the Python script before, or if you manually delete the output file. 

In PyBank, the Python script will analyze the budget_data.csv to calculate each of the following values:
    The total number of months included in the dataset
    The net total amount of "Profit/Losses" over the entire period
    The changes in "Profit/Losses" over the entire period, and then the average of those changes
    The greatest increase in profits (date and amount) over the entire period
    The greatest decrease in profits (date and amount) over the entire period

In PyPoll, the Python script will analyze the election_data.csv to calculate each of the following values:
    The total number of votes cast
    A complete list of candidates who received votes
    The percentage of votes each candidate won
    The total number of votes each candidate won
    The winner of the election based on popular vote

