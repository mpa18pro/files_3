import os

#Создание списка имен файлов
f_names = ['1.txt', '2.txt', '3.txt']

##Подсчет количества строк в файле
def calc_lines(f_names):
    f_lines = dict.fromkeys(f_names) #Создание словаря "имя файла:количество строк"
#Открытие файлов и создание списка содержимого файлов
    for name in f_names:
      f_path = os.path.join(os.getcwd(), name) #Определение пути до файла
      with open(f_path, 'r', encoding = 'UTF-8') as f: #Открытие файла
          f_raw = f.read() #Чтение файла
          f_str = f_raw.split('\n') #Разбиение файла на строки
#Подсчет количества строк в файле
      l_counter = 0
      for n in f_str:
          if n:
              l_counter += 1
      f_lines[name] = l_counter
    return f_lines

#Сортировка файла по значениям количества строк
def sort_lines(f_lines):
    sorted_values = sorted(f_lines.values()) #Сортировка списка значений
    f_sorted = {}
    for i in sorted_values:
        for k in f_lines.keys():
            if f_lines[k] == i:
                f_sorted[k] = f_lines[k]
                break
    return f_sorted

#Запись исходных файлов в новый
def united_files():
    l_quant = calc_lines(f_names)
    sorted_lines = sort_lines(l_quant)
    f_w_path = os.path.join(os.getcwd(), 'f_res.txt') #Путь до файла записи
    f_res = open(f_w_path, 'w') #Открытие файла записи
    for _name in sorted_lines.keys():
        f_r_path = os.path.join(os.getcwd(), _name) #Определение пути до файла чтения
        f_res.write(f'{_name}\n') #Запись в файл имени файла
        f_res.write(f'{str(sorted_lines[_name])}\n') #Запись в файл количества строк в файле
        with open(f_r_path, 'r', encoding = 'UTF-8') as f: #Открытие файла чтения
            f_data = f.read() #Чтение содержимого файла
        f_res.write(f'{f_data}\n\n') #Запись содержимого в файл записи
    f_res.close()
    return f_res


united_files()