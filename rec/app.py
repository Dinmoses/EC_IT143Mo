# The data blob copied from Postman (10 jokes in JSON format)
data = [
    {"type":"general","setup":"How did the hipster burn the roof of his mouth?","punchline":"He ate the pizza before it was cool.","id":117},
    {"type":"general","setup":"Why couldn't the kid see the pirate movie?","punchline":"Because it was rated arrr!","id":310},
    {"type":"general","setup":"How many bones are in the human hand?","punchline":"A handful of them.","id":138},
    {"type":"programming","setup":"What's the best part about TCP jokes?","punchline":"I get to keep telling them until you get them.","id":363},
    {"type":"general","setup":"What did the fish say when it hit the wall?","punchline":"Dam.","id":1},
    {"type":"general","setup":"Why do chicken coops only have two doors?","punchline":"Because if they had four, they would be chicken sedans","id":48},
    {"type":"general","setup":"Why did the opera singer go sailing?","punchline":"They wanted to hit the high Cs.","id":332},
    {"type":"general","setup":"How many kids with ADD does it take to change a lightbulb?","punchline":"Let's go ride bikes!","id":140},
    {"type":"general","setup":"What do I look like?","punchline":"A JOKE MACHINE!?","id":188},
    {"type":"general","setup":"What did the dog say to the two trees?","punchline":"Bark bark.","id":170}
]

# Isolate one dictionary (example: the 3rd joke)
one_joke = data[2]

# Print the entire dictionary
print("One joke dictionary:", one_joke)

# Print specific parts of the dictionary
print("Type:", one_joke['type'])
print("Setup:", one_joke['setup'])
print("Punchline:", one_joke['punchline'])