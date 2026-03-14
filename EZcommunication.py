import time

opt = input("Do you want to look for data changed (1) or do you want to write data (2): ")
filename = "/opt/communication/communication/unencdata.txt"
if opt == "2":
    name = input("What name would you like to be called as: ")
    try:
        while True:
            usr_txt = input("Text: ")
            with open(filename, "r") as file:
                text = file.read()
            pot_name = ""
            pot_name_pos = 0
            start = 0
            found_name = False
            for i in range(len(text)):
                if not found_name:
                    if text[i] == name[pot_name_pos]:
                        if pot_name_pos == 0:
                            start = i
                        pot_name += name[pot_name_pos]
                        pot_name_pos += 1
                    else:
                        start = 0
                        pot_name_pos = 0
                        pot_name = ""
                    if pot_name == name:
                        found_name = True
            if not found_name:
                print("User not found, creating user and adding text")
                with open(filename, "a") as file:
                    file.write("\n" + name + ": " + usr_txt)
            else:
                print("User found, adding text")
                text2 = ""
                line_end = False
                for i in range(len(text)):
                    if i < start or line_end:
                        text2 += text[i]
                    else:
                        if start == i:
                            text2 += name + ": " + usr_txt + "\n"
                        if text[i] == '\n':
                            line_end = True
                with open(filename, "w") as file:
                    file.write(text2)
    except KeyboardInterrupt:
        print("\nAdios")
elif opt == "1":
    try:
        with open(filename, "r") as file:
            text = file.read()
        prev_txt = text
        while True:
            with open(filename, "r") as file:
                text = file.read()
            if text != prev_txt:
                line = ""
                on_line = False
                for i in range(len(text)):
                    if i < len(prev_txt) and i < len(text):
                        if text[i] != prev_txt[i]:
                            on_line = True
                        else:
                            on_line = False
                    else:
                        on_line = False
                    if on_line:
                        line += text[i]
                print("File changed: " + line)
                prev_txt = text
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAdios")
