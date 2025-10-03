from Data.Rankings import get_latest_ranking_url, download_pdf, process_pdf_file, process_list_content
from system import service
from system import view

def main():
    gender, weight = view.get_user()
    rank_df = service.filter_ranking(gender, weight)

    print(rank_df)
    
    user_filter = input("Would you like to remove the double ups? no/yes: ")
    while "yes" not in user_filter and "no" not in user_filter:
        user_filter = input("Would you like to remove the double ups? no/yes: ")
    
    if user_filter == "yes":
        dataframe_db = service.remove_doubles(rank_df)
        print(dataframe_db)

if __name__ == "__main__":
    main()