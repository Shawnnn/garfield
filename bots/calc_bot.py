from bots.base import Bot
from simpleeval import simple_eval


class CalcBot(Bot):

    def _q(self):
        prefix = self.session.get('name', 'Hi') + '! ' if self.session is not None else ''
        s = prefix + "Through recent upgrade I can do arithmetic now. Give me some expression to try"
        if self.run_type == 'loop':
            s += " (type x, q, exit or quit to quit)"
        return s + ":"

    def _think(self, s):
        try:
            result = simple_eval(s)
            return f"Done. Result = {result}"
        except:
            return f"Something is wrong..."


if __name__ == '__main__':
    c = CalcBot()
    c.run()

    c = CalcBot('loop')
    c.run()
