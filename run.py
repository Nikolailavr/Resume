from candidate.main import Candidate
import misc.config as config
from misc.funcs import print_curs


def start():
    me = Candidate()
    print_curs(config.HELLO)
    print_curs(config.HELP)
    while True:
        try:
            me.start()
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    start()
