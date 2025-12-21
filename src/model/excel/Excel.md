# ExcelCore (controla a criação e edição do arquivo):

    - ao criar a classe já pode passar o nome do arquivo para ser aberto em um workbook(grupo de tabelas)
    - set_active_sheet: seleciona uma worksheet(aba) do arquivo 
    - create_sheet: cria uma nova worksheet(aba) e a define como ativa
    - write_cell: escreve um valor em uma célula
    - write_row: escreve uma lista de valores em uma linha inteira
    - read_row: lê os valores de uma linha
    - save: salva o arquivo

# ExcelStyle (controla a formatação do arquivo):

    - ao criar a classe já pode passar a worksheet(aba) do arquivo
    - format_cell: formata uma célula
    - format_row: formata uma linha inteira
    - autosize_columns: ajusta automaticamente a largura das colunas
