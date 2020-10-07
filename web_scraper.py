#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:29:05 2020

@author: ryanfinegan
"""

#libraries
import pandas as pd
import requests

#main function web scraper
def main():
    '''web scraper main function that makes 50 requests to get the 
    information on all the fake company names and purpose statements.'''
    #empty list to see if certain company names failed with an error in the script
    passed = []
    failed = []
    #counter 
    req_count = 0
    #empty list of companies to be added to a dataframe
    company = []
    #empty list of company purposes to be added to a dataframe
    purposes = []
    # Matthew Poltorak: In my code I used a for loop. While I don't think it makes any difference in terms of speed I find its more concise because you don't have to keep track of a counter variable
    while req_count <= 49:
        try:
            # response get request
            resp = requests.get("http://3.95.249.159:8000/random_company",auth = ("user","pass"))
            # splitting at the company name
            name = resp.text.split('Name: ')[1:]
            # splitting at the company purpose
            purpose = resp.text.split('Purpose: ')[1:]
            # data cleaning for the company name to put into a dataframe, then text file
            name = str(name).rsplit('</li>\\n')[0][2:]
            # data cleaning for the company purpose to put into a dataframe, then text file 
            purpose = str(purpose).rsplit('</li>\\n')[0][2:]
            # append to the company name to the list
            purposes.append(purpose)
            # append to the company purpose to the list 
            company.append(name)
            # counter
            req_count = req_count + 1
            passed.append(name)
        except:
            print(f"An error has occurred.{failed}")
            failed.append(name)
    # return a dataframe
    df = pd.DataFrame({'Purpose':purposes}, index = [company])
    # changing the index name to Company from Unnamed
    df.index.names = ['Company']
    # saving the new dataframe into a text file. I wanted a completely new file each time since it's random
    df.to_csv('web_scraper.txt')
    return df

if __name__ == "__main__":
    main()
