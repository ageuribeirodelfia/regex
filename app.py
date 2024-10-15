import re

# texto para atualização
texto = "CLASSIFICAÇÃO:    EQUIPAMENTOS.CONECTIVIDADE.MODELOX.BANDA LARGA PROATIVO"
print('Texto original:'+texto)
# regex para alterar o texto
regex = r'\bMODELOX\b'

# método para verificar e alterar o texto incluindo o espaço se necessário
def corrigir_erro_classificacao(texto):
    # Se encontrar 'MODELOX'
    if re.search(regex, texto):
        # Substituir por "MODELO X"
        texto_corrigido = re.sub(regex, "MODELO X", texto)
        # Retornar o texto corrigido
        return texto_corrigido
    # Se não encontrar 'MODELOX'
    else:
        # Retornar o texto original
        return texto
    
# Rodando a funcao
texto_correto = corrigir_erro_classificacao(texto)
print('Texto corrigido: '+texto_correto)