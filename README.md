Leitor de Cabeçalho de Arquivos .class (Java) Um script em Python desenvolvido para analisar e extrair as informações estruturais do cabeçalho de arquivos binários compilados pelo Java (.class).  

📌 Sobre o Projeto Este projeto foi desenvolvido como um trabalho acadêmico prático de  Organização de Computadores / Engenharia de Software. O objetivo principal é compreender a estrutura interna de arquivos binários e como a Máquina Virtual Java (JVM) reconhece e valida um programa compilado através da leitura de bytes específicos, respeitando a arquitetura Big-Endian. 

🚀 Funcionalidades O script abre o arquivo .class em modo binário e decodifica os seguintes campos obrigatórios da especificação Java: 
Magic Number: Identifica a assinatura do arquivo (o famoso CAFEBABE). 
Minor Version & Major Version: Identifica a versão do compilador utilizado e traduz para a versão comercial do Java (ex: Major Version 52 = Java 8).  
Constant Pool Count: Informa a quantidade de itens presentes na piscina de constantes do arquivo.  

🛠️ Tecnologias Utilizadas Linguagem: Python 3.x  Bibliotecas: Apenas bibliotecas nativas (não requer instalação de pacotes externos).  

⚙️ Como Executar 1. Clone o repositório:  Bash git clone [https://github.com/Giovanna-Teodoro/-Leitura-do-cabe-alho-arquivos-.class.git]
2. Prepare o ambiente: Coloque qualquer arquivo .class válido (gerado pelo comando javac) na mesma pasta do script Python.  
3. Execute o script:  Bash python leitor_cabecalho.py (Certifique-se de que o nome do arquivo .class no código corresponde ao arquivo que você deseja analisar).  


✅ Validação Para atestar a corretude deste algoritmo, os resultados podem ser comparados com a ferramenta oficial de desestruturação do Java. Ao executar o comando nativo javap -v Arquivo.class no terminal, os mesmos valores de Magic Number, versões e tamanho da Constant Pool devem ser exibidos.  

👨‍💻 Autores  Carolina Baba, Daniely Maximo e Giovanna Teodoro 
