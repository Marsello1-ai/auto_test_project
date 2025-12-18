import pytest

pozitiv = ["Mars", "Marsello", "Shrek"]
negative = [None, 123]


@pytest.mark.happy_path()
def test_delete_mem(basic_created_mem, delete_mem):
    meme_id, token_id = basic_created_mem
    delete_mem.delete_mem(meme_id, token_id)
    delete_mem.check_status_code()


@pytest.mark.happy_path()
def test_get_authorize_token(get_authorize_token, get_valid_token):
    token_id = get_valid_token
    get_authorize_token.get_authorize(token_id)
    get_authorize_token.check_status_code()


@pytest.mark.happy_path()
def test_get_meme(get_meme, get_valid_token):
    token_id = get_valid_token
    get_meme.get_meme(token_id)
    get_meme.check_status_code()


@pytest.mark.happy_path()
def test_get_one_meme(get_one_meme, created_and_del_mem):
    meme_id, token_id = created_and_del_mem
    get_one_meme.get_one_meme(meme_id, token_id)
    get_one_meme.check_status_code()


@pytest.mark.happy_path()
@pytest.mark.parametrize('name', pozitiv)
def test_authorize(post_authorize, name):
    post_authorize.post_authorize(name)
    post_authorize.check_status_code()
    post_authorize.check_user_name(name)


@pytest.mark.happy_path()
def test_post_meme(get_valid_token, post_meme, delete_mem):
    token_id = get_valid_token
    meme_id = post_meme.post_meme(token_id)
    delete_mem.delete_mem(meme_id, token_id)
    post_meme.check_status_code()


@pytest.mark.happy_path()
def test_put_mem(put_meme, created_and_del_mem):
    meme_id, token_id = created_and_del_mem
    put_meme.put_meme(meme_id, token_id)
    put_meme.check_status_code()


@pytest.mark.negative()
def delete_mem_negative_meme_id(basic_created_mem, delete_mem):
    meme_id, token_id = basic_created_mem
    delete_mem.delete_mem_negative_meme_id(token_id)
    delete_mem.check_negative_status_code()
    delete_mem.delete_mem(meme_id, token_id)



@pytest.mark.negative()
def delete_mem_negative_authorize(basic_created_mem, delete_mem):
    meme_id, token_id = basic_created_mem
    delete_mem.delete_mem_negative_authorize(meme_id)
    delete_mem.check_negative_status_code_is_401()
    delete_mem.delete_mem(meme_id, token_id)



@pytest.mark.negative()
@pytest.mark.parametrize('name', negative)
def test_authorize_negative(post_authorize, name):
    post_authorize.post_authorize(name)
    post_authorize.check_negative_status_code()



