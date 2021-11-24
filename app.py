import pandas as pd 
#pandas é uma biblioteca de software criada para a linguagem Python para manipulação e análise de dados. 

from selenium import webdriver
#O Selenium, nada mais é, do que uma biblioteca que permite com que o Python abra o seu 
#navegador para executar os comandos desejados.

#Driver para realizar as interações como o Microsoft Edge:
driver = webdriver.Edge(executable_path = r'.\msedgedriver.exe')

#define a fonte dos dados:
df = pd.read_excel('challenge.xlsx')

#Abre site do challenge
driver.get('https://www.rpachallenge.com')

#Star challenge
buttonStart = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button")
buttonStart.click()

#percorre os dados da planilha:
for i, row in df.iterrows():

    #define os campos com CSS selector:
    field_FirstName = driver.find_element_by_css_selector("input[ng-reflect-name='labelFirstName']")
    field_LastName = driver.find_element_by_css_selector("input[ng-reflect-name='labelLastName'")
    field_CompanyName = driver.find_element_by_css_selector("input[ng-reflect-name='labelCompanyName'")
    field_RoleInCompany = driver.find_element_by_css_selector("input[ng-reflect-name='labelRole'")
    field_Address = driver.find_element_by_css_selector("input[ng-reflect-name='labelAddress'")
    field_Email = driver.find_element_by_css_selector("input[ng-reflect-name='labelEmail'")
    field_PhoneNumber = driver.find_element_by_css_selector("input[ng-reflect-name='labelPhone'")

    #preenche os dados em cada campo:
    field_FirstName.send_keys(row[0])
    field_LastName.send_keys(row[1])
    field_CompanyName.send_keys(row[2])
    field_RoleInCompany.send_keys(row[3])
    field_Address.send_keys(row[4])
    field_Email.send_keys(row[5])
    field_PhoneNumber.send_keys(row[6])

    #Clica em "Subimit" para ir para o proximo:
    buttonSubimt = driver.find_element_by_css_selector("input[value='Submit']")
    buttonSubimt.click()
    






