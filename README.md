# АвитоПарсер.
В одной из первых строк кода вам нужно будет заменить ссылку на авито на свою. А так же в функции `init()` заменить пути до `chromedriver` и `chrome binary`.

## Как работает?
Скрипт нужно запускать раз в *пять* минут, этим занимается `run.py`. При каждом запуске `avito.py` скрипт проверяет появились ли новые объявления, если да, то покажет параметры объявления и предложит скопировать ссылку на него.
