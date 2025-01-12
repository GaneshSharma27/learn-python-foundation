# --------------------------------- whole project pending ---------------------------------
board = {"top-L": " ", "top-M": " ", "top-R": " ",
         "mid-L": " ", "mid-M": " ", "mid-R": " ",
         "low-L": " ", "low-M": " ", "low-R": " "}

def print_board(board):
    print(board["top-L"] + " | " + board["top-M"] + " | " + board["top-R"])
    print("--+---+--")
    print(board["mid-L"] + " | " + board["mid-M"] + " | " + board["mid-R"])
    print("--+---+--")
    print(board["low-L"] + " | " + board["low-M"] + " | " + board["low-R"])
print_board(board)

def input_choice():
    print("1. top-L\t2. top-M\t3. top-R")
    print("4. mid-L\t5. mid-M\t6. mid-R")
    print("7. low-L\t8. low-M\t9. low-R")
    print("----------------------------------------")
    while True:
        try:
            select = int(input("Where you want to write? "))
            break
        except ValueError:
            print("Please select only from 1 to 9 values.")
    return select

def play(choice, turn):
    match(choice):
        case 1:
            board["top-L"] = turn
            print_board(board)
            win(board)
        case 2:
            board["top-M"] = turn
            print_board(board)
            win(board)
        case 3:
            board["top-R"] = turn
            print_board(board)
            win(board)
        case 4:
            board["mid-L"] = turn
            print_board(board)
            win(board)
        case 5:
            board["mid-M"] = turn
            print_board(board)
            win(board)
        case 6:
            board["mid-R"] = turn
            print_board(board)
            win(board)
        case 7:
            board["low-L"] = turn
            print_board(board)
            win(board)
        case 8:
            board["low-M"] = turn
            print_board(board)
            win(board)
        case 9:
            board["low-R"] = turn
            print_board(board)
            win(board)
        case _:
            print("Only 1 to 9 values are acceptable.")

def win(board):
    if "top-L" == "top-M" == "top-R":
        print({board["top-L"]} + " win")
    if "mid-L" == "mid-M" == "mid-R":
        print({board["mid-L"]} + " win")
    if "low-L" == "low-M" == "low-R":
        print({board["low-M"]} + " win")
    if "top-L" == "mid-M" == "low-R":
        print({board["mid-M"]} + " win")
    if "low-L" == "mid-M" == "top-R":
        print({board["mid-M"]} + " win")
    if "top-L" == "mid-L" == "low-L":
        print({board["mid-L"]} + " win")
    if "top-M" == "mid-M" == "low-M":
        print({board["mid-M"]} + " win")
    if "top-R" == "mid-R" == "low-R":
        print({board["mid-R"]} + " win")

def main():
    while True:
        print("\n--------------- X's turn ---------------")
        choice = input_choice()
        play(choice, "X")
        print("\n--------------- 0's turn ---------------")
        choice = input_choice()
        play(choice, "0")

if __name__ == "__main__":
    main()
