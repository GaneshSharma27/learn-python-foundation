def list_making():
    generated_list = []
    while True:
        new_item = str(input("Enter new item: "))
        if new_item == "":
            break
        else:
            generated_list.append(new_item.title())
    return generated_list

def comma_code(any_list):
    for index, each_word in enumerate(any_list):
        if index == (len(any_list) - 1):
            print("and " + each_word, end="")
        else:
            print(each_word + ", ", end="")

def main():
    eg_list = list_making()
    # example_list = ["cat", "dog", "mouse", "horse", "elephant"]
    comma_code(eg_list)

if __name__ == "__main__":
    main()
