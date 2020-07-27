from bots.base import Bot


class HelloBot(Bot):

    def _q(self):
        return "Hi, what is your name?"

    def _think(self, s):
        if self.session is not None:
            self.session['name'] = s
        return f"Hello {s}"


if __name__ == '__main__':
    h = HelloBot()
    h.run()