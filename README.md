# stepik_course_task
diploma project

full instruction in russian how to avoid environment mistakes and make a review for this project below

# 1. Скачайте к себе проект, либо скачав и распаковав архив, либо склонировав репозитарий.
# Просмотрите содержимое файла README.md, возможно, там будут какие-нибудь полезные комментарии для проверки.
# Здесь можно, например, указать ОС и версию Python, с которой Вы работаете. 
# 2. Деактивируйте текущее виртуальное окружение, если вы в нем находитесь. 
# Вспомнить, как работать с виртуальными окружениями можно на этом шаге (для Windows):
# https://stepik.org/lesson/25969/step/2?unit=196192
# 3. Создайте новое виртуальное окружение.
# 4. Перейдите в папку вновь созданного окружения:
# cd \path\to\new_virtual_env\Scripts
# 5. Активируйте данное виртуальное окружение.
# 6. Установите пакеты в окружение из файла requirements.txt, который должен быть в скачанном проекте:
# pip install -r \path\to\requirements.txt
# 7. Убедитесь, что путь к chromedriver.exe прописан в PATH, либо скопируйте этот файл в текущую папку Scripts из шага 4.
# 8. Запустите тесты командой:
# pytest -v --tb=line --language=en -m need_review \path\to\test_product_page.py       - в конце указать полный путь к файлу
# 9. Проверьте, что все тесты прошли успешно.
# 10. Если же тесты не запускаются, не спешите ставить 0 баллов и с чувством выполненного долга переходить к следующей рецензии.
# Попробуйте сначала разобраться, в чем заключается ошибка. Возможно, дело в путях к файлам в импорте -- тогда попробуйте поставить / убрать точку в начале и / или добавить / удалить пустой файл __init__.py в корневой папке и / или подпапках.
# Или может проблема в том, что автор перед коммитом случайно добавил какой-нибудь лишний символ файл и не проверил перед отправкой.
# Или возможны еще другие варианты.
