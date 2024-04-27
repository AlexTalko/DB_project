from config import config
from src.db_hh import HeadHunter
from src.func import (proc_company_data,
                      proc_vacs_data,
                      create_database,
                      save_data_employers_to_database,
                      save_data_vacancies_to_database)


def main():
    # создаем экземпляр класса для подключения к API hh.ru
    hh = HeadHunter()

    # создаем список искомых компаний
    company_list = ['ВТБ', 'Ozon', 'Яндекс', 'Роснефть', 'СБЕР', 'Пятерочка', 'Аптеки ВИТА']

    # загружаем информацию о компаниях
    comp = hh.get_company(company_list)

    # загружаем информацию о вакансиях найденных компаний
    vacs = hh.get_company_vacancies(comp)

    # преобразуем полученные данные для сохранения в бд
    companies = proc_company_data(comp)
    vacancies = proc_vacs_data(vacs)

    # создаем базу данных 'hh_vacancies' и таблицы для сохранения данных о компаниях их вакансиях
    params = config()
    database_name = 'hh_vacancies'
    create_database(database_name, params)

    # сохраняем данные о компаниях их вакансиях в бд
    save_data_employers_to_database(companies, database_name, params)
    save_data_vacancies_to_database(vacancies, database_name, params)


if __name__ == '__main__':
    main()
