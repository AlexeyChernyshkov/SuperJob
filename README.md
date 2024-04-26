# Superjob.ru — IT-сервис по поиску работы и подбору сотрудников. 
## Архитектура: 
```
SuperJob/
├── locators/              # Директория с локаторами всех тестируемых страниц
│   ├── common_locators.py                         # Общие локаторы для всех страниц
│   ├── detail_client_page_locators.py             # Локаторы детальной страницы компании
│   ├── detail_course_page_locators.py             # Локаторы детальной страницы курса
│   ├── detail_resume_page_locators.py             # Локаторы детальной страницы резюме
│   ├── detail_vacancy_page_locators.py            # Локаторы детальной страницы вакансии
│   ├── main_page_locators.py                      # Локаторы для общего элемента страницы header
│   ├── resume_create_page_locators.py             # Локаторы страницы создания резюме
│   ├── search_result_clients_page_locators.py     # Локаторы страницы результатов поиска компании 
│   ├── search_result_courses_page_locators.py     # Локаторы страницы результатов поиска курса
│   ├── search_result_resumes_page_locators.py     # Локаторы страницы результатов поиска резюме 
│   └── search_result_vacancy_page_locators.py     # Локаторы страницы результатов поиска вакансии
│
├── pages/              # Директория с методами для всех тестируемых страниц
│   ├── base_page.py                               # Общие методы для всех страниц
│   ├── detail_client_page.py                      # Методы для детальной страницы компании
│   ├── detail_cource_page.py                      # Методы для детальной страницы курса
│   ├── detail_resume_page.py                      # Методы для детальной страницы резюме
│   ├── detail_vacancy_page.py                     # Методы для детальной страницы вакансии
│   ├── main_page.py                               # Методы для общего элемента страницы header
│   ├── resume_create_page.py                      # Методы для страницы "Создание резюме"
│   ├── search_result_clients_page.py              # Методы для страницы поиска компаний
│   ├── search_result_courses_page.py              # Методы для страницы поиска курсов
│   ├── search_result_resumes_page.py              # Методы для страницы поиска резюме
│   └── search_result_vacancy_page.py              # Методы для страницы поиска вакансий
│
├── tests/              # Директория с автотестами
│   ├── test_detail_clients_page.py                # Тест детальной страницы компании
│   ├── test_detail_courses_page.py                # Тест детальной страницы курса
│   ├── test_detail_resume_page.py                 # Тест детальной страницы резюме
│   ├── test_detail_vacancy_page.py                # Тест детальной страницы вакансии
│   ├── test_main_page.py                          # Тест общего элемента страницы header
│   ├── test_resume_create_page.py                 # Тест для страницы "Создание резюме"
│   ├── test_search_result_clients_page.py         # Тест страницы поиска компании 
│   ├── test_search_result_courses_page.py         # Тест страницы поиска курса
│   ├── test_search_result_resume_page.py          # Тест страницы поиска резюме
│   └── test_search_result_vacancy_page.py         # Тест страницы поиска вакансий
│
├── user_data/          # Директория для хранения скриншотов
│   ├── Djamal_ava.jpg        # Изображение пользователя для теста создания резюме
│   └── users.py              # Данные пользователей для авторизации
│
├── conftest.py         # Файл с конфигурационными данными для тестов
├── README.md           # Файл с описанием проекта и инструкциями
└── requirements.txt    # Файл, содержащий настройки виртуального окружения

```


## Описание:

1. **`SuperJob/`**: Главная директория проекта.

2. **`locators/`**: Директория с локаторами всех тестируемых страниц

    - **`common_locators.py`**: Общие локаторы для всех страниц
    
    - **`detail_client_page_locators.py`**: Локаторы детальной страницы компании

    - **`detail_course_page_locators.py`**: Локаторы детальной страницы курса

    - **`detail_resume_page_locators.py`**: Локаторы детальной страницы резюме
   
    - **`detail_vacancy_page_locators.py`**: Локаторы детальной страницы вакансии 
   
    - **`main_page_locators.py`**: Локаторы для общего элемента страницы header
   
    - **`resume_create_page_locators.py`**: Локаторы страницы создания резюме 
      
    - **`search_result_clients_page_locators.py`**: Локаторы страницы результатов поиска компании 
      
    - **`search_result_courses_page_locators.py `**: Локаторы страницы результатов поиска курса 
      
    - **`search_result_resumes_page_locators.py`**: Локаторы страницы результатов поиска резюме  
   
    - **`search_result_vacancy_page_locators`**: Локаторы страницы результатов поиска вакансии

3. **`pages/`**: Директория с методами для всех тестируемых страниц

    - **`base_page.py`**: Общие методы для всех страниц
    
    - **`detail_client_page.py`**: Методы для детальной страницы компании

    - **`detail_cource_page.py`**: Методы для детальной страницы курса

    - **`detail_resume_page.py`**: Методы для детальной страницы резюме
   
    - **`detail_vacancy_page.py`**: Методы для детальной страницы вакансии 
   
    - **`main_page.py`**: Методы для общего элемента страницы header
   
    - **`resume_create_page.py`**: Методы для страницы "Создание резюме" 
      
    - **`search_result_clients_page.py`**: Методы для страницы поиска компаний 
      
    - **`search_result_courses_page.py `**: Методы для страницы поиска курсов 
      
    - **`search_result_resumes_page.py`**: Методы для страницы поиска резюме 
   
    - **`search_result_vacancy_page`**: Методы для страницы поиска вакансий 
  
4. **`tests/`**: Директория с автотестами

    - **`test_detail_clients_page.py`**: Тест детальной страницы компании

    - **`test_detail_courses_page.py`**: Тест детальной страницы курса

    - **`test_detail_resume_page.py`**: Тест детальной страницы резюме

    - **`test_detail_vacancy_page.py`**: Тест детальной страницы вакансии

    - **`test_main_page.py`**: Тест общего элемента страницы header

    - **`test_resume_create_page.py`**: Тест для страницы "Создание резюме"

    - **`test_search_result_clients_page.py`**: Тест страницы поиска компании 

    - **`test_search_result_courses_page.py`**: Тест страницы поиска курса

    - **`test_search_result_resume_page.py`**: Тест страницы поиска резюме

    - **`test_search_result_vacancy_page.py`**: Тест страницы поиска вакансий
 
5. **`tests/`**: Директория для хранения скриншотов

    - **`Djamal_ava.jpg`**: Изображение пользователя для теста создания резюме

    - **`users.py`**: Данные пользователей для авторизации

6. **`conftest.py`**: Файл с конфигурационными данными для тестов

7. **`README.md`**: Файл с описанием проекта и инструкциями

8. **`requirements.txt`**: Файл, содержащий настройки виртуального окружения

Эта структура проекта помогает организовать код и ресурсы таким образом, чтобы проект был легко понятен и масштабируем.