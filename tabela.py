import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

try:
    url = 'https://brasilescola.uol.com.br/quimica/tabela-periodica.htm'
    s = Service(r"C:\Users\c12828q\OneDrive - EXPERIAN SERVICES CORP\Área de Trabalho\Treinando Python\chromedriver-win64\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=s, options=options)
    driver.get(url)
    time.sleep(15)
    #Encontrar a tabela
    
    tabela = driver.find_element(By.XPATH, '//*[@id="area-site"]/div/div[2]/div/div[3]/article/div/div/div[3]/div/div[4]/table')
    tabelaTeste = driver.find_element(By.XPATH, '//*[@id="area-site"]/div/div[2]/div/div[3]/article/div/div/div[3]/div/div[4]/table').text
    #Extrair dados da tabela
    
    linhas = tabela.find_elements(By.TAG_NAME, "tr")
    dados = []
    for linha in linhas:
        colunas = linha.find_elements(By.TAG_NAME, "td")
        dados.append([coluna.text for coluna in colunas])
    
    #Crie um dataframe pandas com os dados extraidos
    df = pd.DataFrame(dados)

    #Salvar os dados em um arquivo excel
    nome_arquivo = "DeusPFV.xlsx"
    try:
        df.to_excel(nome_arquivo, index=False)
        print(f"Tabela {nome_arquivo} salvo, Deus está conosco!!!!")
    except Exception as e:
        print(f"Deus não está conosco :c {str(e)}")

except Exception as e:
    print(f"Deu erro: {str(e)}")
    
driver.quit()
