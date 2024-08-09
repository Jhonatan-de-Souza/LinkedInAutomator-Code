from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from utils import iniciar_contagem_regressiva,rolar_pagina_totalmente_para_baixo, rolar_pagina_totalmente_para_cima
import logging

logging.basicConfig(filename='erros.log',filemode='a',level=logging.ERROR)

def conectar_com_pessoas_na_pagina_atual(driver,window):
    try:
        window.write_output('buscando por botões de conectar na página atual\n')
        rolar_pagina_totalmente_para_baixo(driver)
        rolar_pagina_totalmente_para_cima(driver)
    except Exception as error:
        window.write_output('erro ao tentar rolar a página, favor entrar em contato com o suporte\n')
        logging.error(error)
        
    
    sleep(3)
    try:
        botoes_conectar = driver.find_elements(By.XPATH,"//button[contains(@aria-label, 'Convidar')]")
        window.write_output('encontrado o botão conectar\n')

        for botao_conectar in botoes_conectar:
            sleep(3)
            driver.execute_script("arguments[0].click()", botao_conectar)
            window.write_output('clicado no botao conectar\n')
            sleep(3)
            
            # Extrair nome do contato
            elemento_com_nome_do_contato = driver.find_element(By.XPATH,"//span[@class='flex-1']/strong")
            nome = elemento_com_nome_do_contato.text
            # clicar em Enviar sem Nota
            botao_enviar_sem_nota = driver.find_element(By.XPATH,"//button[@aria-label='Enviar sem nota']")
            window.write_output(f'Enviando convite sem nota para {nome}\n')
            sleep(2)
            
            botao_enviar_sem_nota.click()
            window.write_output(f'{nome} acaba de ser convidado!\n')
            sleep(3)
    except Exception as error:
        window.write_output('houve um erro ao tentar encontrar os botões para se conectar com outras pessoas, favor entrar em contato com o suporte\n')
        logging.error(error)
        
def ir_para_proxima_pagina(driver,window):
    # Verificar se é possível ir para a próxima página
    rolar_pagina_totalmente_para_baixo(driver)
    window.write_output('buscando botão de próxima página\n')
        
    botao_ir_para_proxima_pagina = driver.find_element(By.XPATH,"//button[@aria-label='Avançar']")
    sleep(2)
        
    if botao_ir_para_proxima_pagina.is_enabled() is True:
        botao_ir_para_proxima_pagina.click()
        window.write_output('indo para a próxima página\n')
        conectar_com_pessoas_na_pagina_atual(driver,window)
    else:
        window.write_output('automação chegou à última página!\n')
        driver.quit()
        window['iniciar_automacao'].update(disabled=False)
            
def iniciar_driver():
    chrome_options = Options()
    
    arguments = ['--lang=pt-BR', '--window-size=1920,1080']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    
    driver = webdriver.Chrome()
    return driver

def iniciar_automacao(palavra_chave,window):
    driver = iniciar_driver()
    # delete notifications, pop-ups, set language to pt-br, set default resolution
    link_pesquisa_por_programadores = f'https://www.linkedin.com/search/results/people/?keywords={palavra_chave}&origin=SWITCH_SEARCH_VERTICAL&sid=oJd'

    driver.get(link_pesquisa_por_programadores)
    iniciar_contagem_regressiva(60,1,window)
    conectar_com_pessoas_na_pagina_atual(driver,window)
    ir_para_proxima_pagina(driver,window)    
    sleep(3)
   