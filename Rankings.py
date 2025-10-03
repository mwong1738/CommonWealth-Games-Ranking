from io import BytesIO
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import pdfplumber 
import camelot
import logging

import csv

import re
# Mapping weight classes to IJF URL parameters

logging.getLogger("pdfminer").setLevel(logging.ERROR)

category_map = {
    1: "-60 kg",
    2: "-66 kg",
    3: "-73 kg",
    4: "-81 kg",
    5: "-90 kg",
    6: "-100 kg",
    7: "+100 kg",
    8: "-48 kg",
    9: "-52 kg",
    10: "-57 kg",
    11: "-63 kg",
    12: "-70 kg",
    13: "-78 kg",
    14: "+78 kg",
    15: "Exceptions"
}



DOWNLOADS_PAGE = "https://www.ijf.org/wrl_downloads"

def get_latest_ranking_url():
    r = requests.get(DOWNLOADS_PAGE)
    soup = BeautifulSoup(r.text, "html.parser")

    pdf_link = soup.find("a", href=lambda h: h and h.endswith(".pdf"))
    pdf_url = pdf_link["href"]
    if not pdf_url.startswith("http"):
        pdf_url = "https://www.ijf.org" + pdf_url 
    return pdf_url

def download_pdf(pdf_url):
    response = requests.get(pdf_url)
    pdf_file = BytesIO(response.content)
    return pdf_file


def process_pdf_file(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        all_text = []
        pages_to_view = pdf.pages[1:-1]
        for page in pages_to_view:
            text = page.extract_text()
            if text:
                all_text.extend(text.split("\n"))
    return all_text

def process_list_content(listed_text):
    cols = ["weight", "Ranking","Ranking Nation", "Continent", "Name", "Total Points"]
    i = 0
    rows = []


    index, initial_weight = 1, category_map[1]
    next_weight = category_map[index + 1]
    
    while i < len(listed_text):

        # Skip the headers
        while "%" not in listed_text[i]:
            i += 1
        # Skip the percentages stuff
        while "%" in listed_text[i]:
            i += 1
        
        # Start processing names
        while i < len(listed_text) and next_weight not in listed_text[i]:

            individual_stats = (listed_text[i].split())
            
            if individual_stats[4].isdigit():
                wrl, country, contin, name, total_points = individual_stats[0], individual_stats[1], individual_stats[2], individual_stats[3], individual_stats[4]
            elif individual_stats[5].isdigit():
                wrl, country, contin, name, total_points = individual_stats[0], individual_stats[1], individual_stats[2], individual_stats[3] + individual_stats[4], individual_stats[5]
            else:
                wrl, country, contin, name, total_points = individual_stats[0], individual_stats[1], individual_stats[2], individual_stats[3] + individual_stats[4] + individual_stats[5], individual_stats[6]

            rows.append({"Weight": initial_weight, "Ranking": wrl, "Ranking Nation": country, "continent": contin, "Name": name, "Total Points": total_points})
            i += 1
        
        index += 1

        if index > 14 or i >= len(listed_text):
            df = pd.DataFrame(rows)
            return df
        
        initial_weight = next_weight
        next_weight = category_map[index + 1]

