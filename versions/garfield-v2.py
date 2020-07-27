from time import sleep
from termcolor import colored
import random
from simpleeval import simple_eval


class Bot:

    wait = 1

    def __init__(self, runtype='once'):
        self.runtype = runtype

    def _think(self, s):
        return s

    def _format(self, s):
        return colored(s, 'blue')

    def _say(self, s):
        sleep(Bot.wait)
        print(self._format(s))

    def _q(self):
        return ''

    def _run_once(self):
        self._say(self._q())
        a = input()
        self._say(self._think(a))

    def _run_looped(self):
        self._say(self._q())
        while True:
            a = input()
            if a.lower() in ['q', 'x', 'quit', 'exit']:
                break
            self._say(self._think(a))
    
    def run(self):
        if self.runtype == 'once':
            self._run_once()
        elif self.runtype == 'loop':
            self._run_looped()        


class HelloBot(Bot):

    def _q(self):
        return "Hi, what is your name?"

    def _think(self, s):
        return f"Hello {s}"


class GreetingBot(Bot):

    def _q(self):
        return "How are you today?"

    def _think(self, s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too"
        else:
            return "Sorry to hear that"


class FavoriteColorBot(Bot):

    def _q(self):
        return "What's your favorite color?"

    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}"


class CalcBot(Bot):

    def _q(self):
        s = "Through recent upgrade I can do calculation now. Input some arithmetic expression to try."
        if self.runtype == 'loop':
            s += " (type x, q, exit or quit to quit)"
        return s

    def _think(self, s):
        result = simple_eval(s)
        return f"Done. Result = {result}"


class Garfield:
    
    def __init__(self, wait=1):
        Bot.wait = wait
        self.bots = []

    def add(self, bot_class, runtype='once'):
        bot = bot_class(runtype)
        self.bots.append(bot)

    def _prompt(self, s):
        print(s)
        print()

    def run(self):
        self._prompt("This is Garfield dialog system. Let's talk.")
        for bot in self.bots:
            bot.run()


if __name__ == '__main__':
    garfield = Garfield()

    garfield.add(HelloBot)
    garfield.add(GreetingBot)
    garfield.add(FavoriteColorBot)
    garfield.add(CalcBot, 'loop')
    
    garfield.run()