from misc.funcs import print_curs
import misc.config as config


class Man:
    age: int = 32
    email: str = 'lntemp@yandex.ru'
    telegram_id: str = '@NikolayLavrov'


class Candidate(Man):

    def start(self) -> None:
        match input():
            case '1': print_curs(config.EDUCATION)
            case '2': print_curs(config.EXPERIENCE)
            case '3': print_curs(config.HARD_SKILLS)
            case '4': print_curs(config.SOFT_SKILLS)
            case '5': print_curs(config.ABOUT)
            case '6': self.contacts()
            case 'help': print_curs(config.HELP)
            case 'exit': exit(0)
            case _:
                print_curs(config.BAD_COMMAND)
        print_curs(config.END_MSG)

    def contacts(self) -> None:
        print_curs('Лавров Николай Вячеславович')
        print_curs(f'email: {self.email}')
        print_curs(f'telegram: {self.telegram_id}')

