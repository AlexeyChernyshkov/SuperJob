# Swag Labs - тестовый магазин
## Архитектура: 

```SuperJob/
├── pages/
│   ├── main_page.py            # Файл содержащий информацию по странице "Главная странице"
│   ├── resume_create.py        # Файл содержащий информацию по странице "Создание резюме"
│   ├── locators.py             # Файл содержащий локаторы элементов страниц
│   ├── user_resume.py          # Файл содержащий информацию по странице "Резюме пользователя"
│   ├── users.py                # Файл содержащий информацию о пользователях
│   ├── employer_login.py       # Файл содержащий информацию по странице авторизации для работодателя
│   ├── detail_client_page.py   # Файл соджержащий информацию по детальной странице компании
│   ├── detail_cource_page.py   # Файл соджержащий информацию по детальной странице курсы
│   ├── detail_resume_page.py   # Файл соджержащий информацию по детальной странице резюме
│   ├── detail_vacancy_page.py  # Файл соджержащий информацию по детальной странице вакансии
│   ├── search_result_vacancy  # Файл соджержащий информацию по поиску вакансий
│   ├── search_result_resumes    # Файл соджержащий информацию по поиску резюме
│   ├── search_result_clients   # Файл соджержащий информацию по поиску компаний
│   └── search_result_courses     # Файл соджержащий информацию по поиску курсов
├── config.py                   # Файл с конфигурационными данными
├── tests.py                    # Файл с тестами для автоматизированного тестирования
└── Readme.md                   # Файл с описанием проекта и инструкциями
```


## Описание:

1. **`SuperJob/`**: Главная папка проекта.

2. **`pages/`**: Папка, содержащая файлы, связанные с веб-страницами.

    - **`Locators.py`**: Файл, содержащий локаторы элементов страниц. Локаторы используются для поиска и взаимодействия с элементами на веб-страницах.
    
    - **`main_page.py`**: Файл с классом для работы с "Главной страницей"

    - **`resume_create.py`**: Файл с классом (или классами) для работы со страницей создания резюме. Здесь могут быть методы для заполнения формы логина, отправки данных и проверки результатов.
   
    - **`user_resume.py`**: Файл с классом (или классами) для работы со страницей резюме тестового пользователя. Здесь могут быть методы для заполнения формы логина, отправки данных и проверки результатов. 
   
    - **`users.py`**: Файл содержащий тестовые данные для Пользователей
   
    - **`employer_login.py`**: Файл с классом (или классами) для работы со страницей авторизации работодателя. Здесь могут быть методы для заполнения формы логина, отправки данных и проверки результатов.
   
    - **`detail_client_page.py`**: Файл с классом (или классами) для работы с детальной страницей компании. Здесь могут быть методы для заполнения формы логина, отправки данных и проверки результатов. 
      
    - **`detail_cource_page.py`**: Файл с классом (или классами) для работы с детальной страницей курса. Здесь могут быть методы для заполнения формы логина, отправки данных и проверки результатов. 
      
    - **`detail_resume_page.py `**: Файл с классом (или классами) для работы с детальной страницей резюме. Здесь могут быть методы для заполнения формы логина, отправки данных и проверки результатов. 
      
    - **`detail_vacancy_page.py`**: Файл с классом (или классами) для работы с детальной страницей вакансии. Здесь могут быть методы для заполнения формы логина, отправки данных и проверки результатов. 
   
    - **`search_result_vacancy`**: Файл с классом (или классами) для работы со страницей поиска вакансии. Здесь могут быть методы для заполнения формы логина, отправки данных и проверки результатов. 
      
    - **`search_result_resumes`**: Файл с классом (или классами) для работы со страницей поиска резюме. Здесь могут быть методы для заполнения формы логина, отправки данных и проверки результатов. 
      
    - **`search_result_clients`**: Файл с классом (или классами) для работы со страницей поиска компаний. Здесь могут быть методы для заполнения формы логина, отправки данных и проверки результатов. 
      
    - **`search_result_courses`**: Файл с классом (или классами) для работы со страницей поиска курсов. Здесь могут быть методы для заполнения формы логина, отправки данных и проверки результатов. 
   
3. **`config.py`**: Файл с конфигурационными данными. Здесь может быть информация о URL-адресах, учетных данных, настройках тестирования и т. д.

4. **`tests.py`**: Файл с автоматизированными тестами. Здесь могут быть реализованы тест-кейсы, использующие классы и методы из файлов в папке `pages/`.

5. **`Readme.md`**: Файл с описанием проекта и инструкциями. Здесь могут быть указаны цели проекта, требования, инструкции по установке и запуску тестов, а также другая полезная информация для разработчиков и пользователей проекта.

Эта структура проекта помогает организовать код и ресурсы таким образом, чтобы проект был легко понятен и масштабируем.