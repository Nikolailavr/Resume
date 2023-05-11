from misc.funcs import print_curs


class Man:
    age: int
    phone: str
    telegram_id: str


class Candidate(Man):

    @staticmethod
    def soft_skills():
        print_curs('I am the best prrrroooooggrrraaammeeerrr')
