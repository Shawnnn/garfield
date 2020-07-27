from bots.base import Bot


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
            return "Sorry to hear that"\


if __name__ == '__main__':
    g = GreetingBot()
    g.run()