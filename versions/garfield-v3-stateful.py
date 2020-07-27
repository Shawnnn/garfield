from time import sleep
from termcolor import colored
import random
from simpleeval import simple_eval


class Bot:

    wait = 1

    def __init__(self, run_type='once', session=None):
        self.run_type = run_type
        self.session = session

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
        a = input()
        self._say(self._think(a))

    def _run_loop(self):
        while True:
            a = input()
            if a.lower() in ['q', 'x', 'quit', 'exit']:
                break
            self._say(self._think(a))
    
    def run(self):
        self._say(self._q())

        if self.run_type == 'once':
            self._run_once()
        elif self.run_type == 'loop':
            self._run_loop()        


class HelloBot(Bot):

    def _q(self):
        return "Hi, what is your name?"

    def _think(self, s):
        self.session['name'] = s
        return f"Hello {s}"


def is_good(feeling):
    g = feeling.lower()
    if ('good' in g or 'fine' in g) and g.find('not') == -1:        
        return True
    elif 'bad' in g and 'not' in g:
        return True
    return False

class GreetingBot(Bot):

    def _q(self):
        return "How are you today?"

    def _think(self, s):
        if is_good(s):
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
        s = f"Hi, {self.session.get('name', 'you')}! Through recent upgrade I can do arithmetic now. Give me some expression to try"
        if self.run_type == 'loop':
            s += " (type x, q, exit or quit to quit)"
        return s + ":"

    def _think(self, s):
        try:
            result = simple_eval(s)
            return f"Done. Result = {result}"
        except:
            return f"Something is wrong..."


class Garfield:
    
    def __init__(self, mode='default', wait=1):
        self.mode = mode
        Bot.wait = wait
        self.bots = [] # a list container for bots in system
        self.session = {} # a dict container for session date from bots

    def add(self, bot_class, run_type='once'):
        bot = bot_class(run_type, self.session)
        self.bots.append(bot)

    def _prompt(self, s):
        print(s)
        print()

    def run(self):
        self._prompt("This is Garfield dialog system. Let's talk.")

        if self.mode == 'list':
            self._run_list_mode()
        else:
            self._run_default_mode()

    def _run_default_mode(self):
        for bot in self.bots:
            bot.run()

    def _run_list_mode(self):
        for index, bot in enumerate(self.bots):
            print(f"{index + 1}. {type(bot).__name__}")
        
        bot_index = 0
        bot_count = len(self.bots)
        input_prompt = f"Enter a number to choose your friend (1-{bot_count}): "
        while True:
            try:
                bot_index = int(input(input_prompt))
            except ValueError:
                print(f"Not a valid number. Please retry.")
                continue

            if bot_index < 1 or bot_index > bot_count:
                print(f"You can only choose between 1-{bot_count}")
                continue
            else:
                break

        bot = self.bots[bot_index - 1]
        bot.run()


if __name__ == '__main__':
    garfield1 = Garfield()
    garfield1.add(HelloBot)
    garfield1.add(GreetingBot)
    garfield1.add(FavoriteColorBot)
    garfield1.add(CalcBot, 'loop')
    
    garfield2 = Garfield(mode='list')
    garfield2.add(HelloBot)
    garfield2.add(GreetingBot)
    garfield2.add(FavoriteColorBot)
    garfield2.add(CalcBot)
    
    garfield1.run()
    garfield2.run()