# Описание работы программы и инструкция по запуску

## Краткое описание программы

Данная программа является консольной и предназначена для тестирования доступности серверов по HTTP протоколу.

## Детали работы программы

### Ключи, существующие в программе

Реализованная программа поддерживает следующие ключи:

1. Ключ –H/--hosts со значением хоста, на который будут выполняться запросы. Можно указать несколько адресов через запятую без пробелов;
2. Ключ –C/--count со значением количества запросов, которые будут отправлены на
каждый хост для выведения среднего значения (по умолчанию 1);
3. Ключ –F/--file, содержащий путь до файла со списком адресов, разбитый на строки. Одновременно может быть указан
только один из ключей: или –F, или -H;
4. Ключ –O/--output, содержащий путь до файла, куда нужно сохранить вывод. Если не указан, то вывод отправляется в
консоль.

Также информацию о поддерживаемых ключах можно получить, введя в консоли одну из двух команд:
```commandline
python main.py -h
python main.py --help
```

### Расположение файлов

Для  запуска программы при использовании ключа -F файл с хостами необходимо разместить в папке /resources.

При использовании ключа -O файл со статистикой создается в папке /resources.

## Инструкция по запуску

Для запуска программы необходимо открыть консоль, перейти в директорию проекта и ввести в консоль команду следующего вида:
```commandline
python main.py -H https://ya.ru,https://google.com -C 5
```

## Пример вывода в консоли

При запуске программы, используя команду
```commandline
python main.py -H https://ya.ru,https://google.com -C 5
```

Консоль будет содержать следующий вывод:

```commandline
Loading keys information
Creating parser and getting parsed arguments
Validating parsed arguments
Testing servers

==================================================
TESTING SERVER AVAILABILITY FOR https://ya.ru

Attempt 1: https://ya.ru status_code: 200, fail: False, response_time: 0.49408745765686035, error_message: None
Attempt 2: https://ya.ru status_code: 200, fail: False, response_time: 0.37572503089904785, error_message: None
Attempt 3: https://ya.ru status_code: 200, fail: False, response_time: 0.3790750503540039, error_message: None
Attempt 4: https://ya.ru status_code: 200, fail: False, response_time: 0.3827354907989502, error_message: None
Attempt 5: https://ya.ru status_code: 200, fail: False, response_time: 0.36780428886413574, error_message: None

==================================================
TESTING SERVER AVAILABILITY FOR https://google.com

Attempt 1: https://google.com status_code: 200, fail: False, response_time: 0.7712297439575195, error_message: None
Attempt 2: https://google.com status_code: 200, fail: False, response_time: 0.6841118335723877, error_message: None
Attempt 3: https://google.com status_code: 200, fail: False, response_time: 0.7235527038574219, error_message: None
Attempt 4: https://google.com status_code: 200, fail: False, response_time: 0.7141702175140381, error_message: None
Attempt 5: https://google.com status_code: 200, fail: False, response_time: 0.6939451694488525, error_message: None

Printing statistics

==================================================
TESTING SERVER AVAILABILITY RESULTS
==================================================

Host: https://ya.ru
  Total requests:   5
  Successful:       5
  Failed (400/500): 0
  Errors:           0
  Min time:         0.368s
  Max time:         0.494s
  Avg time:         0.400s

Host: https://google.com
  Total requests:   5
  Successful:       5
  Failed (400/500): 0
  Errors:           0
  Min time:         0.684s
  Max time:         0.771s
  Avg time:         0.717s

==================================================

```


## Дополнительно

Также в программе реализовано логирование.

Для изменения уровня логирования поменяйте соответствующий аргумент в строке 21 файла main.py.