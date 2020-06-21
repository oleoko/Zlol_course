# Zlol_course
Оригінальна програма by Pavlo Zhavoronkov and Pavlo Hluschenko

Programming course practical tasks  
Задача #1  
Написати парсер для логів аpache2:  
Вивести топ айпі за кількістю запитів  	
Вивести найпопулярнiйшi сторiнки  
Вивід має бути красивий, без скобочок  
  
Файл логів, який треба розпарсити:    
http://telegra.ph/Sample-log-01-27    
  
To learn:  
File read  	
Work with strings(String.split() and etc.)  
Data structures: Dictionaries  
  
Задача #2  
Написати парсер сайту https://www.cvedetails.com/  
Аргументом з командного рядка брати 	CVE (   )  	
Витягувати наступну інформацію: 		  
CVE		  
CVSS SCORE		  
Confidentiality Impact  		
Integrity Impact  		
Availability Impact  		
Access Complexity  		
Authentication  	
Gained Access	  	
Vulnerability type(s)  	`
CWE ID  
Products affected  	
Vendor  	
Ігнорувати інформацію в дужках  
  
Advanced:  
Зберегти їх в окремий файл/базу даних  
Не повторюватись в структурі даних, в якій зберігаєте результати  
Парсити для декількох CVE з аргумента командного рядка  
  
To learn:  
Requests  
HTML parsing (Beautiful Soup or equivalent)  
Data structures  
File write  
DB/Serialization  
  
Задача #3 (Треба оновити ІР для задачі)  
Написати баннер грабер:  
Список айпішок має братись з файлу.  
Порт, який має грабатись, має братись з аргументу команд-лайну.  
Вивести результати в файл.  
Якщо вказаний 80 порт, то замість банер 	грабінгу має надсилатись гет запит  
  
Апійшки для сканування:  
http://telegra.ph/IPs-to-scan-02-23  
  
Стаття про банер грабінг в вікі:   
https://www.wikiwand.com/en/Banner_grabbing  
  
Violent python:  
https://www.csee.umbc.edu/wp-content/uploads/2014/05/ViolentPython-ICEW-2014.pdf  
  
Робота з аргументами командної строки:  
http://www.tutorialspoint.com/python/python_command_line_arguments.htm   
  
Робота протоколу HTTP:  
https://ru.m.wikipedia.org/wiki/HTTP  
  
To learn:  
Sockets  
args  
TCP/IP basics  
HTTP basics
  
Задача #4  
Написати веб сервер, використовуючи бібліотеку socket і протокол TCP/IP:  
Программа має надавати доступ до файлів в директорії, з якої вона була запущена.  
Має бути можливість ходити по директоріях  
Advanced:  
При переході на файл відтворювати зміст  
  
To learn:  
Sockets bind  
TCP/IP  
Directories walk  
HTTP basics  
  
Задача #5(?)  
ВИКОРИСТАННЯ ЦІЄЇ ПРОГРАМИ ЗА РАМКАМИ НАВЧАЛЬНОГО КУРСУ КАРАЄТЬСЯ ККУ  
Брутфорсер вордпрессу:  
Встановити віртуальну машину з WordPress  
Написати брутфорсер логінів WordPress ( SERVER_IP/wp-login форма )  
Логіни та паролі брати з різних файлів  
  
Advanced:  
Отримувати список логінів автоматично 	https://hackertarget.com/wordpress-user-enumeration/  
Брати як аргумент з командного рядка файл зі списком серверів, які треба 	брутфорсити  
Зберегти знайдені логіни і паролі до них в файлі  
  
To learn:  
VM configuration  
Requests  
Work with files  
WordPress exploit  
HTML parsing  
  
Задача #6(???)  
ВИКОРИСТАННЯ ЦІЄЇ ПРОГРАМИ ЗА РАМКАМИ НАВЧАЛЬНОГО КУРСУ КАРАЄТЬСЯ ККУ  
Криптолокер:  
Написати програму, яка буде знаходити 	всі файли окрім system32 і файлів скрипта і шифрувати їх.  
Встановити на віртуальну машину Windows.  
Для шифрування має використовуватись будь-який симетричний шифр, оригінальний 	файл має ПЕРЕЗАПИСУВАТИСЬ.  	
Написати дешифратор.  
  
Advanced:  
Написати сервер, який буде зберігати та відтворювати ключі для дешифрування. (спробуйте Flask або щось інше)  
Змінити заставку екрана після дешифрування 	з якимось текстом  
Зробити програму багатопоточною  
  
To learn:  
Cryptolocking  
Client-server relations  
Web framework   	
Multiprocessing  
  
Задача #7(?????)  
MMT Monitoring and management tool. (комплект з клієнта та сервера)  
Клієнт(агент) встановлюється на декілька машин, та отримує команди з сервера.  
По команді від сервера:  
Зробити скріншот і відправити на 	сервер.  
Виконати якусь команду командної строки.  	
Показати повний список всіх директорій 	клієнта.  		
Запустити перехват натиснутих клавіш, та передавати їх на сервер до отримання команди СТОП.  
Обмін даними має бути за протоколом http, кожен клієнт має шифрувати дані в транзіті своїм ключем  
  
Advanced level:  
Додати наступні команди:  
Передати з клієнта на сервер файл. 	  	
Показати всі процеси, які виконуються на клієнті.  
Зупинити процесс.  
Скачати та зберегти файл.  
Скачати файл, зберегти в %TEMP% та виконати.  
Запуск VNC сервера.  
Встановити новий кореневий сертифікат.  
Реалізувати комунікацію через HTTPS  

To learn:  
Client-server advanced  
System functions  
OOP basics  
Objects serialization (pickle, json etc.)  
Malware theory  
