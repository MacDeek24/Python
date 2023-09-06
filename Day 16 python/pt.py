from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","aquirtle","charmander"])
table.add_column("type",["Electric","Water","Fire"])
table.align="l"
print(table)