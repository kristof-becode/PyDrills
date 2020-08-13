from lxml import etree

def main():
    # open .xml
    file = open("/home/becode/data/data.xml", "r")
    print(file.read())
    file.close()

    # parse 1
    # I define my source document
    tree = etree.parse("/home/becode/data/data.xml")
    # I look at my document and identify the tag path to get to the "user" information
    # Indeed, the information is in a name tag itself present in a user tag
    # it even presents itself in a users tag. This last tag is located at the root of the directory
    # so in tree.xpath("/users/user/name") there are the tags associated with our search
    for user in tree.xpath("/users/user/nom"):
        # I want to display only the content (.text) of these tags /users/user/name
        print(user.text)

    # parse 2
    tree.xpath("/users/user/nom")[0].text

    #parse 3 : You can display the attributes of the tags that store this information
    tree = etree.parse("/home/becode/data/data.xml")
    for user in tree.xpath("/users/user"):
        print(user.get("data-id"))

    #parse 4 : You can refine the display by proposing to display only users whose job is Veterinary
    tree = etree.parse("/home/becode/data/data.xml")
    # Quel joli petit dictionnaire
    for user in tree.xpath("/users/user[metier='Veterinaire']/nom"):
        print(user.text)


main()