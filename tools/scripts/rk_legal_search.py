import webbrowser
import sys

def open_legal_databases(iin_bin):
    print(f"\n[+] Открываем официальные реестры для проверки ИИН/БИН: {iin_bin}")
    print("[*] Сайты госорганов защищены от роботов. Пожалуйста, введите номер вручную или вставьте через Ctrl+V на открывшихся страницах.")
    
    # Железобетонные стартовые страницы проверок, которые никогда не выдадут 404
    urls = [
        # 1. Минюст РК (АИС ОИП) — Главная страница поиска должников и запретов
        "https://aisoip.adilet.gov.kz/",
        
        # 2. Судебный кабинет РК — Официальный поиск судебных дел
        "https://sud.gov.kz/rus/content/poisk-sudebnyh-del",
        
        # 3. Реестр благонадежности налогоплательщиков РК (КГД)
        "https://kgd.gov.kz/ru/services/taxpayer_search",
        
        # 4. Электронное правительство (eGov) — Проверки юридических лиц и контрагентов
        "https://egov.kz/cms/ru/services/passports/legal_entities"
    ]
    
    # Открываем стабильные вкладки
    for url in urls:
        webbrowser.open(url)
    
    print("\n[+] Все официальные вкладки успешно запущены в браузере!")

if __name__ == "__main__":
    print("====================================================")
    print("   РК: СТАБИЛЬНЫЙ ЗАПУСК ГОСУДАРСТВЕННЫХ РЕЕСТРОВ   ")
    print("====================================================")
    
    user_input = input("Введите ИИН или БИН для проверки: ").strip()
    
    if len(user_input) == 12 and user_input.isdigit():
        open_legal_databases(user_input)
    else:
        print("[-] Ошибка: Номер должен состоять строго из 12 цифр.")
