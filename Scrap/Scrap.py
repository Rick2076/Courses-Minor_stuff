from re import I
from requests import get
from bs4 import BeautifulSoup

def Chapter(url):
    response = get(url).text
    html_soup = BeautifulSoup(response, 'html.parser')

    chapter_list = html_soup.find('div',class_="chapter-list")
    chapter_rows= chapter_list.find_all('div','row')

    chapter_links = []
    
    for row in chapter_rows:
        chapter_links += ["https://ww2.mangakakalot.tv/" + str(row.find(href=True)['href'])]
    
    return chapter_links

def Image(Chapter_links):
    Image_links = []
    for url in Chapter_links:
        Image_chapter = []
        response = get(url).text
        html_soup = BeautifulSoup(response, 'html.parser')

        Image_list = html_soup.find_all('img',class_="img-loading")
        Image_chapter = []

        for img in Image_list:
            Image_chapter += [img['data-src']]
        
        Image_links += Image_chapter
    
    return Image_links 
    
def Download(Image_links, local):
    for chapter in Image_links:
        chapter_num = str(Image_links.index(chapter))
        for url_img in chapter:
            page_num = str(chapter.index(url_img))
            page_img = get(url_img)

            open(local+'Chapter_'+chapter_num+'_Page_'+page_num+'.jpg', 'wb').write(page_img.content)



def Main():
    #main_url = input("Inisra o link do 'mangakalot' do anime que voce quer baixar por que eu sou preguiçoso e n vou me foder pra voce só precisar digitar o nome do manga")
    main_url = "https://ww1.mangakakalot.tv/manga/manga-bv959356"
    
    #local = input("Insira o caminho a pasta destino de começando de 'C:/Users', sim voce tem que fazer isso, n me importo com seu tempo")
    local = 'C:/Users/rick1/git-course/Scrap/'

    #Pega os links de cada capítulo e baixa individualmente cada imagem em cada capítulo
    Chapter_links = Chapter(main_url)
    
    #Pega o link de cada imagem dos capítulos fornecidos
    Image_links = Image(Chapter_links)

    #Baixa os arquivos
    Download(Image_links, local)

    
#Main()

image = [Image(["https://ww1.mangakakalot.tv/chapter/manga-bv959356/chapter-1"])]
local = 'C:/Users/rick1/git-course/Scrap/SBR/'
Download(image,local)
