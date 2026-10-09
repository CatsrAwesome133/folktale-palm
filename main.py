class Decision:
    def __init__(self,options:dict):
        self.options = options
        self.numbers = {}
        if type(self.options) != dict:
            raise TypeError("options must be a dictionary")
        for index in self.options:
            counter = 1
            if type(index) != int and type(index) != str:
                raise TypeError("indexes must be integers or strings")
            if type(self.options[index]) != list:
                raise TypeError("keys should be lists in this format: [choice text, narration text, jump id]")
            self.numbers[str(counter)] = index
            counter += 1

    def show(self):
        counter = 1
        for option in self.options:
            print(f"·{option}/{counter} > "+
                self.options[option][0])
            counter += 1

    def make(self):
        choice = input("   ··> ")
        result = ""
        valid = False
        while not valid:
            try:
                result = self.options[choice]
                valid = True
            except (IndexError,KeyError):
                print("Um, you can't do that. Try again?")
                choice = input("   ··> ")
        print(result[1])
        return result[2]

if __name__ == '__main__':
    new = Decision({"A": ["choose a","A!!", "B"]})
    second = Decision({"A": ["choose a", "No!!!", "C"],
                       "B": ["choose b", "yea!", "C"]
                       })
    all_options = {
        "A": new,
        "B": second
    }

    new.show()
    new.make()