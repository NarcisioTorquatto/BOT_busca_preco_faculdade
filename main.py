from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
from openpyxl import load_workbook
import os

class Bot:
    def __init__(self, driver_path: str):
        """Inicializa o WebDriver."""
        try:
            self.service = Service(driver_path)
            self.driver = webdriver.Chrome(service=self.service)
            self.driver.maximize_window()
        except Exception as e:
            print(f"Erro ao iniciar o WebDriver: {e}")

    def navegacao_site(self):
        self.driver.get("https://www.educamaisbrasil.com.br/")
        time.sleep(3)

        while len(self.driver.find_elements(By.XPATH, '//*[@id="BuscaCursoSuperior"]/div/div[1]/div/ng-select/div/div/div[3]/input')) < 1:
            print('Aguardando o Carregamento...')

        elemento_cidade = self.driver.find_element(By.XPATH, '//*[@id="BuscaCursoSuperior"]/div/div[1]/div/ng-select/div/div/div[3]/input')
        elemento_cidade.click()
        time.sleep(1)
        elemento_cidade.send_keys("Manaus")
        elemento_cidade.send_keys(Keys.ENTER)
        time.sleep(1)

        elemento_curso = self.driver.find_element(By.XPATH, '//*[@id="BuscaCursoSuperior"]/div/div[2]/div/ng-select/div/div/div[2]/input')
        elemento_curso.click()
        elemento_curso.send_keys('Direito')
        time.sleep(2)
        elemento_curso.send_keys(Keys.ENTER)

        btn_buscar = self.driver.find_element(By.XPATH, '//*[@id="BuscaCursoSuperior"]/div/div[4]/button')
        btn_buscar.click()
        time.sleep(2)

        elemento_filtro = self.driver.find_element(By.XPATH, '//*[@id="ConteudoPrincipal"]/app-curso-ofertas-container/div/div[2]/app-lista-oferta-superior/div[1]/div/div/div[2]/ul/li[1]/button')
        elemento_filtro.click()
        time.sleep(2)
        elemento_caixa_filtro = self.driver.find_element(By.XPATH, '//*[@id="ConteudoPrincipal"]/app-curso-ofertas-container/div/div[2]/app-lista-oferta-superior/div[2]/div[2]/div/div/div/label[1]/input')
        elemento_caixa_filtro.click()
        time.sleep(2)

        elemento_ordenar = self.driver.find_element(By.XPATH, '//*[@id="ConteudoPrincipal"]/app-curso-ofertas-container/div/div[2]/app-lista-oferta-superior/div[1]/div/div/div[2]/ul/li[2]/button')
        elemento_ordenar.click()
        time.sleep(3)
        elemento_menor_preco = self.driver.find_element(By.XPATH, '//*[@id="ConteudoPrincipal"]/app-curso-ofertas-container/div/div[2]/app-lista-oferta-superior/div[1]/div/div/div[2]/ul/li[2]/div/div/ul/li[2]')
        elemento_menor_preco.click()
        time.sleep(5)

    def extracao_info(self):
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-oferta.ng-star-inserted")

        faculdades = []

        for card in cards:
            try:
                # Pega o nome da faculdade a partir do href
                link = card.find_element(By.CLASS_NAME, "logo").find_element(By.TAG_NAME, "a").get_attribute("href")
                nome_slug = link.split("/")[-1]
                nome_formatado = nome_slug.replace("-", " ").title()

                # Pega o valor da mensalidade
                valor_element = card.find_element(By.CLASS_NAME, "valor-bolsa")
                valor_texto = valor_element.text.replace("\n", "").strip()
                
                # Tipo de curso (ex: Bacharelado, Tecnólogo)
                tipo_element = card.find_element(By.CSS_SELECTOR, "span.ng-star-inserted")
                tipo_curso = tipo_element.text.replace("|", "").strip()                    
                
                # Modalidade (ex: Presencial, EAD, etc.)
                modalidade_texto = card.find_element(By.TAG_NAME, "button").text.strip()
                modalidade = modalidade_texto.split(" ")[0]  # Pega só a primeira palavra   
                
                curso_nome = card.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text.strip()
                curso = curso_nome.split(" ")[0]  # Pega só a primeira palavra   
                
                                    
                faculdades.append({
                    "FACULDADE": nome_formatado,
                    "MENSALIDADE": valor_texto,
                    "TIPO": tipo_curso,
                    "MODALIDADE": modalidade,
                    "CURSO": curso_nome 
                })                
                
                # Salva a planilha com pandas
                df = pd.DataFrame(faculdades)
                caminho_arquivo = r"Output\faculdades_educamais.xlsx"
                if os.path.exists(caminho_arquivo):
                    os.remove(caminho_arquivo)                
                df.to_excel(caminho_arquivo, index=False)

                # Ajusta o tamanho das colunas com openpyxl
                wb = load_workbook(caminho_arquivo)
                ws = wb.active

                # Loop pelas colunas
                for col in ws.columns:
                    max_length = 0
                    coluna = col[0].column_letter 

                    for cell in col:
                        try:
                            if cell.value:
                                max_length = max(max_length, len(str(cell.value)))
                        except:
                            pass

                    ajuste = max_length + 2
                    ws.column_dimensions[coluna].width = ajuste

                # Salva novamente o arquivo
                wb.save(caminho_arquivo)

                print("✅ Planilha criada e formatada com sucesso!")                

            except Exception as e:
                print("Erro em um dos cards:", e)
                continue
            
        # Mostra os resultados
        # for item in faculdades:
        #     print(f"🏫 {item['faculdade']} | 💰 {item['mensalidade']} | 📘 {item['tipo']} | 🏫 {item['modalidade']} | 🎓 {item['area']}")
                
        input()

    def run(self):
        """Lógica principal do bot."""
        try:
            self.navegacao_site()
            self.extracao_info()
               
        except Exception as e:
            print(f"Erro na execução do bot: {e}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    DRIVER_PATH = r"resources\chromedriver-win64\chromedriver.exe" 
    bot = Bot(DRIVER_PATH)
    bot.run()
    
