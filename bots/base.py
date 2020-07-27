from time import sleep
from termcolor import colored


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
