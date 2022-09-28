# django-scraping

--- 

## Sobre
- Aplicação desenvolvida para pegar a entrada do usuário, e baseado nela, ir até o site da [Drogasil](https://www.drogasil.com.br) e trazer os resultados da primeira página, relacionado ao que o usuário solicitou
- Esta aplicação foi desenvolvida utilizando o ambiente virtual do python, o framework ```django```, a biblioteca ```beautifulsoup``` e a biblioteca ```requests```
- Desenvolvida no sistema operacional windows


## Instruções de execução
Você deverá realizar o clone deste projeto na sua área de trabalho:
- Navegando pelo terminal do seu sistema operacional, vá até a pasta da sua área de trabalho e digite o comando ```git clone https://github.com/GabrielVasconcelosMarques/django-scraping.git```

Após ter feito o clone do projeto, abra a pasta do projeto na IDE de sua escolha:
- Como o projeto foi desenvolvido num ambiente virtual do python, você deverá ativar o ambiente, antes de executá-lo, rodando o seguinte comando: 
- Caso esteja no windows: ```.\venv\Scripts\activate```, caso apresente algum erro nessa ativação, no windows, digite o comando ```Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned``` e após isso, digite novamente o comando ```.\venv\Scripts\activate```
- Caso esteja no linux: ```source bin/activate```
- Após rodar o comando acima, você deverá instalar as bibliotecas que foram utilizadas para essa aplicação, elas estão descritas no arquivo requirements.txt deste repositório. Para instalá-los, você deverá utilizar o comando ```pip install -r requirements.txt```
- Se por alguma razão o comando acima não funcionar, dentro do seu ambiente, você digita os comandos de instalação ```pip install django```, ```pip install beautifulsoup4``` e ```pip install requests```

Agora, para executar a aplicação:
- Na pasta raiz do projeto, pela sua IDE, digite o comando ```python .\manage.py runserver```, caso esteja no windows
- Caso esteja no linux, digite o comando ```python3 manage.py runserver```
- Abra no seu navegador, o endereço ```http://127.0.0.1:8000/```

## Utilização da aplicação
- Após a aplicação estar rodando, você verá uma tela com uma barra de pesquisa, onde você poderá informar o produto que deseja pesquisar ou o sintoma que deseja pesquisar, e depois pressiona no botão ```buscar```, caso queira resetar a busca, pressione no botão ```resetar```, sendo retornado ao usuário a listagem dos produtos, com o nome do produto, valor e sua indicação de tarja para venda.


## Demonstração do projeto

### Tela inicial
![1](https://user-images.githubusercontent.com/66792384/192638643-c62298a4-a192-4ee0-87e1-e8aad57751d5.PNG)

### Tela após o usuário informar que deseja pesquisar o produto desodorante
![2](https://user-images.githubusercontent.com/66792384/192638646-ec826f96-6703-455a-a6eb-94cc4fc1860e.PNG)

### Tela após o usuário pressionar no botão buscar, com o resultado sendo mostrado
![3](https://user-images.githubusercontent.com/66792384/192638649-c9f7de1c-0190-43bd-b1f0-e53809173d72.PNG)

![4](https://user-images.githubusercontent.com/66792384/192638651-ee296688-12f7-4a3e-9545-5c2c1a2e4ef9.PNG)

## Tela de exemplo caso o usuário opte por pesquisar pelo sintoma de dor de cabeça
![5](https://user-images.githubusercontent.com/66792384/192638655-4bd9fc40-3cb4-4c13-8a2f-2d1d427e9234.PNG)

## Tela de resultado, após pressionar em buscar
![6](https://user-images.githubusercontent.com/66792384/192638657-b6bb5f51-56c6-4764-89df-f01bf97cc6b8.PNG)

## Author
### Gabriel Vasconcelos
