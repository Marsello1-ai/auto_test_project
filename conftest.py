import pytest
from endpoint.delete_mem import MethodDeleteMem
from endpoint.get_authorize_token import MethodGetAuthorize
from endpoint.get_meme import MethodGetMeme
from endpoint.get_one_meme import MethodGetOneMeme
from endpoint.post_authorize import MethodPostAuthorize
from endpoint.post_meme import MethodPostMeme
from endpoint.put_meme import MethodPutMeme
from utils.token_manager import TokenManager


@pytest.fixture()
def delete_mem():
    return MethodDeleteMem()


@pytest.fixture()
def get_authorize_token():
    return MethodGetAuthorize()


@pytest.fixture()
def get_meme():
    return MethodGetMeme()


@pytest.fixture()
def get_one_meme():
    return MethodGetOneMeme()


@pytest.fixture()
def post_authorize():
    return MethodPostAuthorize()


@pytest.fixture()
def post_meme():
    return MethodPostMeme()


@pytest.fixture()
def put_meme():
    return MethodPutMeme()


@pytest.fixture(scope="session")
def token_manager():
    return TokenManager()


@pytest.fixture()
def get_valid_token(token_manager):
    return token_manager.get_valid_token()


@pytest.fixture()
def basic_created_mem(get_valid_token, post_meme):
    token_id = get_valid_token
    meme_id = post_meme.post_meme(token_id)
    return meme_id, token_id


@pytest.fixture()
def created_and_del_mem(get_valid_token, post_meme, delete_mem):
    token_id = get_valid_token
    meme_id = post_meme.post_meme(token_id)
    yield meme_id, token_id
    delete_mem.delete_mem(meme_id, token_id)
