def test_delete_mem(basic_created_mem, delete_mem):
    meme_id, token_id = basic_created_mem
    delete_mem.delete_mem(meme_id, token_id)
    delete_mem.check_status_code()


def test_get_authorize_token(get_authorize_token, basic_authorize_method):
    token_id = basic_authorize_method
    get_authorize_token.get_authorize(token_id)
    get_authorize_token.check_status_code()


def test_get_meme(get_meme, basic_authorize_method):
    token_id = basic_authorize_method
    get_meme.get_meme(token_id)
    get_meme.check_status_code()


def test_get_one_meme(get_one_meme, created_and_del_mem):
    meme_id, token_id = created_and_del_mem
    get_one_meme.get_one_meme(meme_id, token_id)
    get_one_meme.check_status_code()


def test_authorize(post_authorize):
    post_authorize.post_authorize()
    post_authorize.check_status_code()


def test_post_meme(basic_authorize_method, post_meme, delete_mem):
    token_id = basic_authorize_method
    meme_id = post_meme.post_meme(token_id)
    delete_mem.delete_mem(meme_id, token_id)
    post_meme.check_status_code()


def test_put_mem(put_meme, created_and_del_mem):
    meme_id, token_id = created_and_del_mem
    put_meme.put_meme(meme_id, token_id)
    put_meme.check_status_code()
