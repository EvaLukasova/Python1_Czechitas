""" Pomocí nástroje regex101 vymysli regulární výraz, který označí platná data a neoznačí neplatná data:
platná data:
2.2.2022
13. 8. 1999
4/5/2001
neplatná data:
5.123.458.91
21.4
8./9 """
(0?[1-9]|[12][0-9]|3[01])(\.|\/)(\ ?)(0?[1-9]|1[012])(\.|\/)(\ ?)\d{4}