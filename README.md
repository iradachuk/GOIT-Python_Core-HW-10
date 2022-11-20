# GOIT-Python_Core-HW-10

Репозиторій для домашнього завдання до модуля 10 (Основи роботи з класами)


## _Завдання_
У цій домашній роботі ми продовжимо розвивати нашого віртуального асистента з CLI інтерфейсом.

Наш асистент вже вміє взаємодіяти з користувачем за допомогою командного рядка, отримуючи команди та аргументи та виконуючи потрібні дії. У цьому завданні треба буде попрацювати над внутрішньою логікою асистента, над тим, як зберігаються дані, які саме дані і що з ними можна зробити.

Застосуємо для цих цілей об'єктно-орієнтоване програмування. Спершу виділимо декілька сутностей (моделей) з якими працюватимемо.

У **користувача** буде адресна книга або **книга контактів**. Ця книга контактів містить **записи**. Кожен **запис** містить деякий набір **полів**.

Таким чином ми описали сутності (класи), які необхідно реалізувати. Далі розглянемо вимоги до цих класів та встановимо їх взаємозв'язок, правила, за якими вони будуть взаємодіяти.

Користувач взаємодіє з **книгою контактів**, додаючи, видаляючи та редагуючи **записи**. Також користувач повинен мати можливість шукати в **книзі контактів записи** за одному або декількома критеріями (полям).

Про **поля** також можна сказати, що вони можуть бути обов'язковими (ім'я) та необов'язковими (телефон або email наприклад). Також **записи** можуть містити декілька **полів** одного типу (декілька телефонів наприклад). Користувач повинен мати можливість додавати/видаляти/редагувати **поля** у будь-якому записі.

В цій домашній роботі ви повинні реалізувати такі класи:

- Клас ```AddressBook```, який успадковується від ```UserDict```, та ми потім додамо логіку пошуку за записами до цього класу.
- Клас ```Record```, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля ```Name```.
- Клас ```Field```, який буде батьківським для всіх полів, у ньому потім реалізуємо логіку загальну для всіх полів.
- Клас ```Name```, обов'язкове поле з ім'ям.
- Клас ```Phone```, необов'язкове поле з телефоном та таких один запис (```Record```) може містити кілька.
## Критерії прийому
- Реалізовано всі класи із завдання.
- Записи ```Record``` у ```AddressBook``` зберігаються як значення у словнику. В якості ключів використовується значення ```Record.name.value```.
- ```Record``` зберігає об'єкт ```Name``` в окремому атрибуті.
- ```Record``` зберігає список об'єктів ```Phone``` в окремому атрибуті.
- ```Record``` реалізує методи для додавання/видалення/редагування об'єктів ```Phone```.
- ```AddressBook``` реалізує метод ```add_record```, який додає ```Record``` у ```self.data```.