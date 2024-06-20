import requests 
from bs4 import BeautifulSoup 
 
def extract_price(element): 
    price_text = element.get_text() 
    price_text = price_text.replace("$", "").replace("\n", "").replace(",", "") 
    return float(price_text) 
 
#ersal dar khavast be saite  HTML 
response = requests.get("https://coinranking.com/") 
soup = BeautifulSoup(response.content, "html.parser") 
 
# yaftan tamai eleman ha ba class"valuta" 
price_elements = soup.find_all("div", class_="valuta") 
total_values_to_process = 50 
 
current_count = 0 
batch_total = 0.0#hame daste 
batch_count = 0 #daste shomares  
 
# pardazesh az eleman  
for index in range(0, total_values_to_process, 2): 
    current_count += 1 
    price = extract_price(price_elements[index]) 
    print(price) 
    batch_total += price 
 
    if current_count == 5: 
        batch_count += 1 
        print(f"Average [{batch_count}]: {batch_total / 5}") 
        print("-------------------------") 
        batch_total = 0 
        current_count = 0

