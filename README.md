🌐 Projekt "Korona Gór Polski" – Flask + SQLite

Ten projekt stanowi bazę do zajęć praktycznych dla studentów II roku kierunku Teleinformatyka na AGH.
W ramach kursu studenci uczą się podstaw obsługi relacyjnych baz danych w aplikacjach webowych z wykorzystaniem Flaska, SQLAlchemy i blueprintów.

🔄 Cel projektu

Projekt pokazuje, jak stworzyć aplikację internetową umożliwiającą:
    zarządzanie bazą danych szczytów Korony Gór Polski,
    rejestrowanie użytkowników i zdobytych przez nich gór,
    korzystanie z REST API i systemu szablonów HTML (Jinja2),
    rozdzielenie aplikacji na blueprinty: home, user_api, users

📂 Struktura projektu (fragment)

korona/
├── app/
│   ├── __init__.py          # fabryka aplikacji Flask
│   ├── models.py            # definicje tabel (User, Peak, PeakEntry)
│   ├── crud.py              # inicjacja tabeli Peak, przykładowe operacjie CRUD
│   ├── crud_relations.py    # inicjacja tabel User i PeakEntry, przykładowe operacjie CRUD
│   ├── home/                # blueprint: strona główna
│   ├── user_api/            # blueprint wykorzystujący REST API
│   ├── users/               # blueprint wykorzystujący renderowanie szablonów
│   ├── static/              # pliki CSS
│   └── templates/           # szablony HTML
├── instance/korona.db       # plik bazy danych SQLite
├── config.py                # konfiguracja Flask
├── run.py                   # uruchamianie aplikacji
├── requirements.txt         # zależności Pythona

🚀 Jak uruchomić projekt lokalnie

Stwórz środowisko wirtualne:

python -m venv venv
source venv/bin/activate      # (Linux/macOS)
venv\Scripts\activate         # (Windows)

1. Zainstaluj zależności:
pip install -r requirements.txt
wgraj do głównego katalogu projektu plik config.py umieszczony w katalogu Seminarium-5 na Teams'ach

2. Dodaj ustawienie zmiennej zmianną FLASK_APP do środowiska wirtualnego:
- jeśli używasz PowerShell to dodaj w pliku /venv/Scripts/Activate.ps1 tuż przed linią '# SIG # Begin signature block' dodaj następująca linię:
  $env:FLASK_APP = "migrate.py"
- jeśli używasz CMD to dodaj w pliku /venv/Scripts/activate.bat tuż przed linią :END dodaj następującą linię:
  set FLASK_APP=migrate.py


3. Załóż bazę danych korzystajac z migracji:
sprawdz czy jest ustawiona zmeinna FLASK_APP: $env:FLASK_APP -> powinno być: migrate.py. Jeśłi nie jest to ustaw: $env:FLASK_APP = "migrate.py"
kroki: 
flask db init
EDIT: flask db stamp head 
flask db migrate -m "Inicjalna baza danych"
flask db upgrade

4. Uruchamianie testowych aplikacji:
python -m app.crud --- wpisuje szczytu do tableli peaks
python -m app.crud_relations  ---wpisuje uzytkowników do tabeli user oraz wejścia do tablei peak_entry

5. Uruchom aplikację:
python run.py
Wejdź na: http://127.0.0.1:5000


📊 Tematy edukacyjne

W ramach projektu studenci poznają m.in.:
    relacyjne bazy danych i ORM (SQLAlchemy),
    migracje schematu (Flask-Migrate),
    blueprinty i organizacja kodu,
    obsługa formularzy i przesyłanie plików,
    bezpieczeństwo danych i walidacja wejścia,
    budowa i wykorzystanie REST API (GET, POST).

Projekt udostępniony do celów edukacyjnych – nie zawiera danych wrażliwych i może być rozwijany przez studentów.
W razie pytań proszę kontaktować się z prowadzeniem zajęć.

