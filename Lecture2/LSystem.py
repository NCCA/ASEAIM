import turtle


def generatRuleString(axiom, rules, iterations):
    derived = [axiom]  # this is the first seed
    for _ in range(iterations):  # now loop for each iteration
        nextSequence = derived[-1]  # grab the last rule
        nextAxiom = [
            rule(char, rules) for char in nextSequence
        ]  # for each element in the rule expand
        derived.append(
            "".join(nextAxiom)
        )  # append to the list, we will only need the last element
    return derived


def rule(sequence, rules):
    if sequence in rules:
        return rules[sequence]
    return sequence


def drawLSystem(turtle, commands, length, angle):
    stack = []
    for command in commands:
        turtle.pendown()
        if command in [
            "F",
            "G",
            "R",
            "L",
            "A",
        ]:  # forward rules for some l system grammars
            turtle.forward(length)
        elif command in ["f", "B"]:
            turtle.penup()
            turtle.forward(length)
        elif command == "+":
            turtle.right(angle)
        elif command == "-":
            turtle.left(angle)
        elif command == "[":
            stack.append((turtle.position(), turtle.heading()))  # save turtle values
        elif command == "]":
            turtle.penup()  # were moving back to save pos
            position, heading = stack.pop()
            turtle.goto(position)
            turtle.setheading(heading)
