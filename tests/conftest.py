import pytest

@pytest.fixture
def yes_form_data():
    return {
        'title': 'title',
        'category': 'fiction',
        'link': 'http://127.0.0.1'
    }


# @pytest.fixture
# def no_form_data():
#     return {
#         'title': 'title',
#         'category': 'fiction',
#         'link': 'link'
#     }