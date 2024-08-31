
text = "Ha kell koveto kovesd be es irj ra ig: IGNAME"
bonus_text = " {}x"


for i in range(100):  # loop 5 times
    print( text + bonus_text.format(i+1) )  # add bonus text with loop number and 'x'
