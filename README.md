Файл содержит описание класса юнитов и армии. Чтобы запустить скачайте файл main.py и запустите его с помощью python 3.4 (python3.4 main.py). Также там содержатся юниттесты.
Чтобы установить игру, распакуйте архив Game_itog и запустите файл KEK, нужно чтобы рядом в той же директории лежала папка Things, там будут текстуры. Также прилагаются исходники кода: файлы main.py, unit.py, onnject.py, action.py. В unit.py реализованы паттерны фабрики, абстрактной фабрики и компановщика (общее здоровье и общяя защита), наблюдатель (spells, которая меняет всех юнитов и значения армии). В object.py - декоратор (mulicaast). В action реализован паттерн посетитель (все типы взаимодествий в одном классе). Паттерн комманд решил не реализовывать, так как все запросы вполне ограничиваются клавишами и мышкой. 
Игра - пошаговая стратегия с возможностью создавать разных юнитов, а также по ходу игры получить очень сильного уинкального четвертового юнита - Кураму. В верхних левой и правой клетке абстрактные замки со значением здоровья и денег. Игру можно закончить, нажав ескейп, крестик или снизив здоровья какого-то из замков ниже 0. На поле есть деньги, генерирующиеся каждый раз в рандомном количестве и рандомном месте. Посередине всегда находится яйцуо, скормив которому достаточно воинов можно получить Кураму. На кнопки 1, 2, 3 можно создать мечника, лучника и вора. На кнопки a, d, m можно скастовать увеличение аттаки, защиты и мультикаст (кастует все сразу, но за большую цену). После того, как первый игрок сделал свое действие, ход переходит ко второму. Двойным нажатием на юнита его можно удалить, юнита можно передвинуть, нажав на него и тыкнувв доступную для хода клетку. Удачной игры)
