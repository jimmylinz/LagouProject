import pytest
import allure


def test_attach_txt():
    allure.attach("这是个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>首页</body>","这是个body",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach("E:\python_project\pythoncode\test_allure\photo\photo.jpg",
                       name="photo",attachment_type=allure.attachment_type.JPG)