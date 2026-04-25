# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:51:19 2026

@author: gio
"""

import os
   
def leitura_cabeçalho(arquivo_entrada):
        """Funcao de leitura do arquivo verfica se este foi encontrado, 
            em seguida chama a funcao open() para abrir o arquivo em leitura 
            binaria, "rb". """
        if os.path.isfile(arquivo_entrada):
            arquivo = open (arquivo_entrada,"rb")
            
            
            """Leitura dos 4 primeiros bytes e conversao para 
                hexadecimal """
            
            magic_nu = arquivo.read(4)
            hexa = magic_nu.hex().upper()            
            
            """ Verifica se produz o magic number em hexadeciomal,
                assinatura dos arquivos .class, caso contrário,
                a função é retornada"""
                
            if(hexa != "CAFEBABE"):
                print("Este não é um arquivo .class")
                return
            
        
            """ Leitura dos 2(5,6) bytes seguintes,para identificar
                a versao secundaria(minor version) do arquivo,
                conversao para int considerando o primeiro bit 
                como mais significativo (big-edian),
                formato utilizado em arquivos .class"""            
            menor = arquivo.read(2)
            menor_int = int.from_bytes(menor, byteorder='big')
            

            
            """ Leitura dos 2(7,8) bytes seguintes,para identificar
                a versão princial JVM,conversao para int considerando
                o primeiro bit como mais significativo (big-edian)
                , formato utilizado em arquivos .class"""     
            maior = arquivo.read(2)
            maior_int = int.from_bytes(maior, byteorder= 'big')
            
            
            """Leitura da constant pool, numero de refererências estáticas
                do arquivo. Conversao para int, considerando o primeiro bit como mais significativo (big-edian)
                , formato utilizado em arquivos .class"""
            constant = arquivo.read(2)
            constant_pool = int.from_bytes(constant, byteorder= 'big')
            
            
            
            
            """ Condição para verificar a versao final Java """
            if maior_int >= 45:
                java_versao = maior_int - 44 
                
            else: 
                java_versao = "Antiga/Desconhecida"
                
                
            texto_saida = (
                f"Magic Number: {hexa}\n"
                f"Minor Version: {menor_int}\n"
                f"Major Version: {maior_int} (Java {java_versao})\n"
                f"Constant Pool: {constant_pool}, sendo {constant_pool-1} entradas válidas.\n"
            )
            
            escrever_arquivo(texto_saida)
            arquivo.close()
            
            
        else:
            print( "O arquivo não existe ou é um diretório")
            return
    
       
def escrever_arquivo(texto):
    """Funcao que irá receber os dados convertidos do arquivo de
        entrada e retornar em um arquivo.txt""" 
        
    arquivo_txt = open("arquivo_final.txt", 'w')
    arquivo_txt.write(texto)
    arquivo_txt.close()
    print("Arquivo criado com sucesso!")
    
    
  
      

path = input("Indique o caminho para o arquivo que deseja ler\n"
      "Ou apenas o nome, caso este arquivo esteja na mesma pasta que este programa: \n")    
        
 
leitura_cabeçalho(path)

    





