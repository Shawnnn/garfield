from bots.base import Bot
import random


class FavoriteColorBot(Bot):

    def _q(self):
        return "What's your favorite color?"

    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}"


if __name__ == '__main__':
    f = FavoriteColorBot()
    f.run()