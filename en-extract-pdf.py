import camelot

tables = camelot.read_pdf('foo.pdf', page='1')

print(tables)

tables.export('foo.pdf', f='csv', compress=True)

# export to a csv file
tables[0].to_csv('foo.csv')

# print the data frame
print(tables[0].df)