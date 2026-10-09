# Palm's no good, very bad time in probably-but-not-explicitly Soul Sanctum
Folktale text adventure based off of a wip hollow knight fic (and some ocs!)

## To play:
1. Run `main.py`
2. Read the text, and type in your choice when presented!

The choices look like this:
```
·Input1/Input2 > The choice you're making
```

## How does this work?
With OOP, duh.

But seriously, the game itself is just a while loop and a bunch of decision data. Almost all the logic is handled by the `Decision` class. I accidentally (?) made it very picky on inputs, oops.

**Here's an overview:**

The `Decision` class has three functions:
1. `__init__`: of course we have this one! It passes one dictionary throguh to `self.options`.
2. `send()`: this one outputs the available options, and not much else.
3. `make()`: this lets the user make a decision. It prints text that comes after the decision and returns the ID of the next decision to make.

The dictionary passed when initialising a `Decision` object should look something like this:
```py
options={
    "ID1": ["option text","text after option chosen","Next_ID"],
    "ID2": ["option text","text after option chosen","Next_ID"],
    #...
    "IDn": ["option text","text after option chosen","Next_ID"],
}
```

By the way, `Next_ID` refers to the id of the next *decision*, not the next choice.

I've structured the main code to initialize this dictionary after creating all decision objects:
```py
all_options = {
    "ID1": decision_one,
    "ID2": decision_two,
    #...
    "IDn": decision_n,
}
```

This way, the game loop becomes very simple!
```py
all_options["A"].show()
next = all_options["A"].mak

while playing:
    all_options[next].show()
    print()
    next = all_options[next].make()

    if next == "C":
        playing = False
```

## Soo... I wanna use this sturcture for my game!
I have no idea why you would, but you can just grab `classes.py` and import it!

Oh and here's an actual explanation of the gameplay loop:

```py
# ^^^ If you have narration or other text to display before the player can make decisions, do it here! ^^^

# This makes the first decision, which you will always have to put outside the loop :D
all_options["A"].show()
next = all_options["A"].mak

# This is the main gameplay loop, where the player keeps making decisions until they finish the game
while playing:
    all_options[next].show()
    print() # This makes a new line for readability
    next = all_options[next].make()

    # This is the end condition! You can add "End" or any other ID to your ending option, and copy it here. When the player picks that option, the game will end
    if next == "C":
        playing = False

# If you want more text after the game ends (ie. "Congrats! You won!"), do it here!
```

The logic quickly becomes confusing, so I suggest you draw diagrams!
<br/><small>this is why my game is so linear</small>

## Weaknesses
Variable-based logic is pretty much impossible currently. I... didn't implement this because I didn't really need it. I *might* add it in the future though!

Also, this is really, *really* picky about your dictionaries. If you don't pass a dictionary with elements with the type `int: list`, you get an error. If you don't pass a correctly formatted list, the text gets really confusing.

Finally, just use Ren'Py. 