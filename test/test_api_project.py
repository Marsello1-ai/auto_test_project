import pytest

from utils.test_data import (
    pozitiv_authorize,
    negative_authorize,
    pozitiv_payload_post_mem,
    negative_payload_post_mem,
    negative_payload_put_mem,
)


@pytest.mark.happy_path()
def test_delete_mem(basic_created_mem, delete_mem):
    meme_id, token_id = basic_created_mem
    delete_mem.delete_mem(meme_id, token_id)
    delete_mem.check_status_code_is_200()
    delete_mem.delete_mem(meme_id, token_id)
    delete_mem.check_negative_status_code_is_404()


@pytest.mark.happy_path()
def test_get_authorize_token(get_authorize_token, get_valid_token):
    token_id = get_valid_token
    get_authorize_token.get_authorize(token_id)
    get_authorize_token.check_status_code_is_200()


@pytest.mark.skip('Bag - долго отдает ответ или не отдает вовсе')
@pytest.mark.happy_path()
def test_get_meme(get_meme, get_valid_token):
    token_id = get_valid_token
    get_meme.get_meme(token_id)
    get_meme.check_status_code_is_200()
    get_meme.check_meme_list_not_empty()


@pytest.mark.happy_path()
def test_get_one_meme(get_one_meme, created_and_del_mem):
    meme_id, token_id = created_and_del_mem
    get_one_meme.get_one_meme(meme_id, token_id)
    get_one_meme.check_status_code_is_200()
    get_one_meme.check_meme_id_in_payload()


@pytest.mark.happy_path()
@pytest.mark.parametrize('name', pozitiv_authorize)
def test_authorize(post_authorize, name):
    post_authorize.post_authorize(name)
    post_authorize.check_status_code_is_200()
    post_authorize.check_user_name(name)
    post_authorize.check_authorize_token()


@pytest.mark.happy_path()
@pytest.mark.parametrize('payload', pozitiv_payload_post_mem)
def test_post_meme(get_valid_token, post_meme, delete_mem, payload):
    token_id = get_valid_token
    meme_id = post_meme.post_meme(token_id, payload)
    post_meme.check_status_code_is_200()
    post_meme.check_payload_post_meme()
    delete_mem.delete_mem(meme_id, token_id)


@pytest.mark.happy_path()
@pytest.mark.skip('Bag - id не int, а str')
def test_put_mem(put_meme, created_and_del_mem, payload=None):
    meme_id, token_id = created_and_del_mem
    put_meme.put_meme(meme_id, token_id, payload)
    put_meme.check_status_code_is_200()
    put_meme.check_payload_put_meme()


@pytest.mark.skip('Bag - должен отдавать 405, а отдает 400')
@pytest.mark.negative()
def delete_mem_negative_meme_id(basic_created_mem, delete_mem):
    meme_id, token_id = basic_created_mem
    delete_mem.delete_mem_negative_meme_id(token_id)
    delete_mem.check_negative_status_code_is_405()
    delete_mem.delete_mem(meme_id, token_id)


@pytest.mark.negative()
def delete_mem_negative_authorize(created_and_del_mem, delete_mem):
    meme_id, token_id = created_and_del_mem
    delete_mem.delete_mem(meme_id, token_id=None)
    delete_mem.check_negative_status_code_is_401()


@pytest.mark.negative()
def test_get_authorize_token_negative(get_authorize_token, get_valid_token):
    get_authorize_token.get_authorize(token='no_valid')
    get_authorize_token.check_negative_status_code_is_404()


@pytest.mark.negative()
def test_get_meme_negative(get_meme, get_valid_token):
    get_meme.get_meme(token_id=None)
    get_meme.check_negative_status_code_is_401()


@pytest.mark.negative()
def test_get_one_meme_negative_meme_id(get_one_meme, created_and_del_mem):
    meme_id, token_id = created_and_del_mem
    get_one_meme.get_one_meme_negative_meme_id(token_id)
    get_one_meme.check_negative_status_code_is_404()


@pytest.mark.negative()
def test_get_one_meme_negative_authorize(get_one_meme, created_and_del_mem):
    meme_id, token_id = created_and_del_mem
    get_one_meme.get_one_meme_negative_authorize(meme_id)
    get_one_meme.check_negative_status_code_is_401()


@pytest.mark.negative()
@pytest.mark.parametrize('name', negative_authorize)
def test_authorize_negative(post_authorize, name):
    post_authorize.post_authorize(name)
    post_authorize.check_negative_status_code_is_400()


@pytest.mark.negative()
@pytest.mark.parametrize('payload', negative_payload_post_mem)
def test_post_meme_negative(get_valid_token, post_meme, delete_mem, payload):
    token_id = get_valid_token
    meme_id = post_meme.post_meme(token_id, payload)
    post_meme.check_negative_status_code_is_400()
    delete_mem.delete_mem(meme_id, token_id)


@pytest.mark.negative()
@pytest.mark.parametrize('payload', negative_payload_put_mem)
def test_put_mem_negative_payload(put_meme, created_and_del_mem, payload):
    meme_id, token_id = created_and_del_mem
    payload["id"] = meme_id
    put_meme.put_meme(meme_id, token_id, payload)
    put_meme.check_negative_status_code_is_400()


@pytest.mark.negative()
def test_put_mem_negative_meme_id(put_meme, created_and_del_mem, payload=None):
    meme_id, token_id = created_and_del_mem
    meme_id = 1
    put_meme.put_meme(meme_id, token_id, payload)
    put_meme.check_negative_status_code_is_403()
