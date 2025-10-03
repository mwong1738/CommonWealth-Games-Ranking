from Data.Rankings import get_latest_ranking_url, download_pdf, process_pdf_file, process_list_content
from Data.Countries import commonwealth_countries
import pandas as pd
import pycountry


def filter_ranking(gender, weight):
    ijf_rank_url = get_latest_ranking_url()
    pdf_file_path = download_pdf(ijf_rank_url)
    listed_text = process_pdf_file(pdf_file_path)
    
    #Ranking data frame
    ranking_df = process_list_content(listed_text)
    by_weight_df = ranking_df[ranking_df['Weight'] == weight]

    commonwealth_df = pd.DataFrame()

    rows = []
    
    for index, row in by_weight_df.iterrows():
        country = pycountry.countries.get(alpha_3 = row["Ranking Nation"])
        if country and country.name in commonwealth_countries:
            rows.append(row.to_dict())
    
    return pd.DataFrame(data = rows)


def remove_doubles(dataframe):
    existing_countries = []

    rows = []
    for index, row in dataframe.iterrows():
        if row["Ranking Nation"] in existing_countries and row["Ranking Nation"] != "NZL":
            pass
        else:
            rows.append(row.to_dict())
            existing_countries.append(row["Ranking Nation"])
    
    return pd.DataFrame(data = rows)