from time import sleep 

def iniciar_contagem_regressiva(segundo_final,segundo_inicial,window):
    window.write_output('Você tem 60 segundos para realizar o logi\n')
    for time in range(segundo_final, segundo_inicial,-1):
        window.write_output(f'Restam {time} segundos\n')
        sleep(1)

def rolar_pagina_totalmente_para_baixo(driver):
    # Rolar a página totalmente para baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def rolar_pagina_totalmente_para_cima(driver):
    # Rolar a página totalmente para baixo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")