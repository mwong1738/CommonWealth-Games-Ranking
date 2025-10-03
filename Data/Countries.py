import pycountry
import requests
from bs4 import BeautifulSoup

commonwealth_countries = [
    "Antigua and Barbuda", "Australia", "Bahamas", "Bangladesh", "Barbados",
    "Belize", "Botswana", "Brunei", "Cameroon", "Canada", "Cyprus", "Dominica",
    "Eswatini", "Fiji", "Gabon", "Gambia", "Ghana", "Grenada", "Guyana",
    "India", "Jamaica", "Kenya", "Kiribati", "Lesotho", "Malawi", "Malaysia",
    "Maldives", "Malta", "Mauritius", "Mozambique", "Namibia", "Nauru",
    "New Zealand", "Nigeria", "Pakistan", "Papua New Guinea", "Rwanda",
    "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
    "Samoa", "Seychelles", "Sierra Leone", "Singapore", "Solomon Islands",
    "South Africa", "Sri Lanka", "Tanzania", "Togo", "Tonga",
    "Trinidad and Tobago", "Tuvalu", "Uganda", "United Kingdom", "Vanuatu", "Zambia"
]


men_weights = ['-60 kg', '-66 kg', '-73 kg', '-81 kg', '-90 kg', '-100 kg', '+100 kg']
women_weights = ['-48 kg', '-52 kg', '-57 kg', '-63 kg', '-70 kg', '-78 kg', '+78 kg']


weight_categories = {
    "Men": men_weights,
    "Women": women_weights
}





