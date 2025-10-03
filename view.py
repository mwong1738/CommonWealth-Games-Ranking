from Data.Countries import weight_categories



def get_user():
    user_gender = input("Choose sex: Men or Women: ")
    while "Men" != user_gender and "Women" != user_gender:
        user_gender = input("Choose sex: Men or Women: ")

    categ_selection =  "Select category from " + str((weight_categories[user_gender])) + ": "

    user_weight = input(categ_selection)

    while user_weight not in weight_categories[user_gender]:
        user_weight = input(categ_selection)
    
    return user_gender, user_weight













