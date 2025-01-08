def opentxt(filename, type):
    file = open(filename, 'r', encoding="utf-8")
    if type == 0:
        print(file.read())
    if type == 1:
        for line in file:
            print(line)
    file.close()


def writetxt(filename, text):
    file = open(filename, 'a')
    file.write(text)
    file.close()


def opentxt2(filename, type):
    try:
        file = open(filename, 'r')
        try:
            if type == 0:
                print(file.read())
            if type == 1:
                for line in file:
                    print(line)

        finally:
            file.close()
    except FileNotFoundError:
        print("такого файла не существует!")
    except:
        print("Ошибка в работе с файлом")


# ------------task 1--------------
printtype = int(input("выберите режим вывода 0-весь сразу 1-построчно"))
opentxt('example.txt', printtype)
# ------------task 1--------------


# ------------task 2--------------
text = ("Porsche 918 Spyder — гибридный суперкар, выпущенный в ограниченном количестве с 2013 года. "
        "Он оснащён мощным бензиновым двигателем и электромоторами, что обеспечивает невероятную "
        "скорость и экологичность. 918 Spyder стал символом высоких технологий и передового дизайна Porsche.\n")
writetxt('user_input.txt', text)
# ------------task 2--------------


# ------------task 3--------------
opentxt2('example13213214.txt', 0)
# ------------task 3--------------
