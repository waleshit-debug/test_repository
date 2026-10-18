import pytest


@pytest.fixture()
# предусловия для теста
def set_up():
    print("enter system")
    yield
    # приостанавливает выполнение функции, сохраняя её состояние
    # при следующем вызове продолжает работу с места остановки.
    print("exit system")


# чтобы предусловия выполнялись при запуске каждого отдельного теста,
# нужно прописать функцию фикстуры как аргумент def test_send_mail_1(set_up)
def test_send_mail_1(set_up):
    print("mail sent 1")


def test_send_mail_2():
    print("mail sent 2")

# test_send_mail()
