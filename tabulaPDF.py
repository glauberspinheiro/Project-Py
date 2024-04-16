import tabula

table_list = tabula.read_pdf('relatorioCliente.pdf', pages = 'all')
print(len(table_list))

