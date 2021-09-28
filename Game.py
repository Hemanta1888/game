# create a  mat lib game using python

# input place which is later use by user

color1=input("Enter a color name: ")
color2=input("Enter an another color name: ")
Adjective=input("Enter an adjective name: ")


# Create a story

story=f"""
        Roses are {color1},
        violets are {color2},
        sugar is {Adjective},
        and so are you!
"""


print(story.format(color1,color2,Adjective))