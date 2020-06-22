import xml.etree.ElementTree as ET


def xmlkelime_parser():
    object = ET.parse(
        "turkish_wordnet.xml")
    source = object.getroot()
    while True:
        value = str(input("Kelime giriniz:"))
        value = value.lower()



        for given in source:
            state = search(given,value)

        break


def search(given,text):        #search işlemi yapmak için tanımladık
    for child in given:
        if child.tag == "SYNONYM":
            for little in child:
                if little.text == text:
                    printSynset(given)
                    return 1


def printSynset(given):        #tagları ekrana yazdırmak için gereken metod
    for child in given:
        if child.tag == "SYNONYM":
            print(child.text)
            for little in child:
                print(little.tag + " - " + little.text)
        elif child.tag == "SR":
            print(child.text)
            for little in child:
                print(little.tag + " - " + little.text)

        else:
            print(child.tag + " - " + child.text)
    print("-----------END-----------------")
    """tag = source.tag

    for x in source[1]:
            for y in x:
                print(x.tag)
                print(y.text)
        print("---")

       """





"""def xml_parser():
    object = ET.parse(
        "C:/Users/Fatih/Downloads/Compressed/TurkishWordNet-master/src/main/resources/turkish_wordnet.xml")
    source = object.getroot()
    for x in source[1].findall("DEF"):
        print("Kelimeler:", x.text)"""

xmlkelime_parser()





