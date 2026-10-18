import pytest

#
# @pytest.fixture()
# # предусловия для теста
# def set_up():
#     print("enter system")


# чтобы предусловия выполнялись при запуске каждого отдельного теста,
# нужно прописать функцию фикстуры как аргумент def test_send_mail_1(set_up)
def test_send_mail_3():
    print("mail sent 3")


def test_send_mail_4():
    print("mail sent 4")

# test_send_mail()