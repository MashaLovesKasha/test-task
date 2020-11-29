import allure
from utils.user import get_user_by_name, get_posts_by_user_id
from utils.validators import check_user_id, check_user_id_in_post, check_user_name


class TestUser:
    @allure.feature('Users')
    def test_find_user_by_name(self, client, username):
        user_data = get_user_by_name(client, username)
        data_user_name = user_data.get("username")
        check_user_name(data_user_name)
        with allure.step(f"Check that username of the found user is {username}"):
            assert data_user_name == username, f"Username should be {username}, got {user_data['username']}"

    @allure.feature('Users')
    def test_find_posts_of_user(self, client, username):
        user_data = get_user_by_name(client, username)
        user_id = user_data.get("id")
        with allure.step(f"Check id of {username}"):
            check_user_id(user_id)

        posts_by_user = get_posts_by_user_id(client, user_id)
        with allure.step("Check that each post contains correct userId"):
            for post in posts_by_user:
                post_id = post.get("id")
                user_id_in_post = post.get("userId")
                check_user_id_in_post(post_id, user_id_in_post, user_id, post)
