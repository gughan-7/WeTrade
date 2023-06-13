from bs4 import BeautifulSoup 


with open("portfolio.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")    

div_bs4 = soup.find(id = "stock_display") 
    
print(div_bs4.text)