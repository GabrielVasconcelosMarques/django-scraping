from django.shortcuts import render
import requests
import json

def get_html_content(produto):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    produto = produto.replace(" ", "+")
    html_content = session.get(f'https://www.drogasil.com.br/search?w={produto}').text
    return html_content

def home(request):
    #lista_nome_produtos = None
    lista_nome = None
    lista_img = None
    lista_preco = None
    lista_tarja = None
    lista_conjunta = None
    if 'produtos' in request.GET:
        produto = request.GET.get('produtos')
        html_content = get_html_content(produto)
        #print(html_content)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Trecho do código implementado com sucesso
        # Caso eu quisesse pegar nome e imagem pelo beautifulsoup, porém preferi pegar pelo método da linha 39
        '''
        nome = soup.find_all('a', attrs={'class': 'LinkNextstyles__LinkNextStyles-t73o01-0 cpRdBZ LinkNext'})
        imagem = soup.find_all('img', attrs={'class': 'ProductCardImagestyles__ProductImage-sc-1dv85s1-1 juXUCX swiper-lazy'})
        '''

        script = soup.find('script', {'id':'__NEXT_DATA__'})
        texto_do_script = script.string

        retorno_json = json.loads(texto_do_script)
        with open('json1.json', 'w', encoding="utf-8") as f:
            f.write(str(texto_do_script))

        lista_preco = []
        lista_tarja = []
        lista_nome = []
        lista_img = []
        lista_conjunta = []

        for c in retorno_json['props']['pageProps']['initialData']['products']:
            #print(c['name'], c['price'], c['image'], c['descriptionStripe'])
            #print("\n")
            lista_nome.append(c['name'])
            lista_img.append(c['image'])
            lista_preco.append(c['price'])
            if c['descriptionStripe'] != None:
                lista_tarja.append(c['descriptionStripe'])
            else:
                lista_tarja.append('PRODUTO SEM TARJA')

        

        # Pega o conteúdo(string) da tag script encontrada
        
        #with open('arquivo.txt', 'w', encoding="utf-8") as f:
        #    f.write(str(html_content))
        #for elemento in nome:
        #    lista_nome_produtos.append(elemento.text)
            #print(elemento)
            #print("\n")

        '''
        for i in imagem:
            #print(i['src']) # pegando src das imagens
            #print(i['alt'])
            #print("\n")
            if i['alt'] not in lista_nome:
                lista_nome.append(i['alt'])
            
            if 'data:image' not in i['src']:
                lista_img.append(i['src'])


        print("lista nome tamanho: ", len(lista_nome))
        print("lista ing tamanho: ", len(lista_img))
        '''

        for c in range(len(lista_nome)):
            lista_conjunta.append([lista_nome[c], lista_img[c], lista_preco[c], lista_tarja[c]])

        print(lista_conjunta)
          
            

        #print(lista_nome_produtos)

    return render(request, 'core/home.html', {'lista_conjunta' : lista_conjunta})
