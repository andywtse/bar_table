from bar_tab import Tab

table1 = Tab()
table2 = Tab()

table1.add('wine')
table1.add('desert')

table2.add('beer')
table2.add('beef')
table2.add('veggie')

table1.print_bill(6.25, 20)
table2.print_bill(6.25, 15)
