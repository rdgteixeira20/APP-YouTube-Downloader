Aplicação execuável para download de vídeos do Youtube

- Python 3 
- QT5 Design
############Instalar Biblioteca PyQt5#######################
- pip install PyQt5


############Converter Projeto .Ui (QTDesign) para python#######

/diretorio_do_frame/ pyuic5 'nomedoframe'.ui -o 'nomedoframe'.py -x


############Converter Imagem para Python###########

/diretorio_da_imagem/ pyrcc5 'nomedaimagem'.qrc -o 'nomedaimagem'.py

############Tornar programa executável##############
- pip3 install py installer

/diretorio_do_arquivo/ pyinstaller --onefile --noconsole 'nome_do_arquivo'.py

############Se der erro de chamada ( pyinstaller não existe) #############
- Erro ao chamar o pyinstaller ( Adicionar o caminho HOME ao Path ) 
    export PATH="$HOME/.local/bin:$PATH" 



