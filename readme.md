# IG-Collector
 Um projeto que visa automatizar o processo de sabe se um perfil está ativo no instagram através da data do último post


## Feito com:
 <p align="left">
 <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
 <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/>
 <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a></p>


## Requisitos:
Python

Selenium

Chrome


# Instruções de uso:

```sh
1 - Realize o download dos arquivos. Você pode fazer isso da seguinte forma:
    1.1 - Baixar esse repositório em formato .zip e por fim extrair os arquivos para uma pasta de sua preferência.
    1.2 - Clonar esse repositório através do git com o seguinte comando: "$ git clone https://github.com/MauPxt/".
2 - Utilizar o comando "$ pip install -r requirements.txt"
3 - Inserir os perfis que deseja analisar no arquivo "perfis.txt"
4 - Executar o script "$ python InstagramCollector.py":
  4.1 - Vai abrir um navegador do Chrome, MINIMIZE ele e vá para o terminal que executou o código
  4.2 - Inserir os dados solicitados no terminal.
5 - Acompanhe e aguarde o processo finalizar
6 - Verifique os resultados no arquivo gerado "resultados.csv"

- Bônus - Para transformar o arquivo em um executável basta utilizar o seguinte comando "$ pyinstaller .\InstagramCollector.py --onefile"
```
