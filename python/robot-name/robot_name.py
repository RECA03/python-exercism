import random

class Robot:

    used_names = set(" ")

    def __init__(self):
        self.name = self.name_generator()

    def name_generator(self):
        name = " " # placeholder name to start while loop

        if len(Robot.used_names) == 676001:
            raise RuntimeError("All possible robot names have been exhausted!")

        while name in Robot.used_names: # generate a name until it is 100% new
            letters = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ",k=2))
            numbers = "".join(random.choices("1234567890",k=3))
            name = letters + numbers

        Robot.used_names.add(name)
        return letters + numbers

    def reset(self):
        self.name = self.name_generator()