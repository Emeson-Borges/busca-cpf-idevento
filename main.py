import os
import xml.etree.ElementTree as ET

# Caminho para a pasta contendo os XMLs
pasta_xmls = 'C:/Users/itarg/Downloads/TOMEACU-FINAL'  # Substitua pelo caminho da sua pasta

# Diretório para salvar o arquivo de saída único
diretorio_saida = 'C:/Users/itarg/Desktop/ler-xml-salvar-arquivo/dados.txt'  # Substitua pelo caminho desejado

# Função para extrair o CPF e o ID de um arquivo XML
def extrair_cpf_e_id_arquivo_xml(xml_file):
    try:
        # Parse o XML
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Namespace
        namespace = {'eSocial': 'http://www.esocial.gov.br/schema/evt/evtRemun/v_S_01_01_00'}

        # Encontre o elemento 'cpfTrab' no XML
        cpf_trab = root.find('.//eSocial:cpfTrab', namespaces=namespace)

        if cpf_trab is not None:
            # Obtenha o CPF
            cpf = cpf_trab.text

            # Encontre o atributo 'Id' no elemento 'evtRemun'
            ide_evento = root.find('.//eSocial:evtRemun', namespaces=namespace).attrib.get('Id')

            if ide_evento is not None:
                return cpf, ide_evento

        return None, None
    except Exception as e:
        print(f"Erro ao analisar o arquivo {xml_file}: {str(e)}")
        return None, None

# Dicionário para armazenar CPFs e IDs correspondentes
mapeamento_cpf_id = {}

# Loop através de todos os arquivos XML na pasta
arquivos_xml = [os.path.join(pasta_xmls, arquivo) for arquivo in os.listdir(pasta_xmls) if arquivo.endswith('.xml')]

for arquivo_xml in arquivos_xml:
    cpf, ide_evento = extrair_cpf_e_id_arquivo_xml(arquivo_xml)
    if cpf and ide_evento:
        # Armazenar CPF e ID correspondente no dicionário
        mapeamento_cpf_id[cpf] = ide_evento

# Salvar o mapeamento de CPFs e IDs em um único arquivo de saída
with open(diretorio_saida, 'w') as arquivo_saida:
    for cpf, ide_evento in mapeamento_cpf_id.items():
        arquivo_saida.write(f"CPF: {cpf}, IDEVENTO: {ide_evento}\n")

print("Mapeamentos CPF para ID foram salvos no arquivo de saída único.")
