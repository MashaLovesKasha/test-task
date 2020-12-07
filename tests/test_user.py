import allure
from utils.validators import check_user_id, check_user_id_in_post, check_user_name


class TestUser:
    @allure.feature('Users')
    def test_find_user_by_name(self, user_api_client, username):
        user_data = user_api_client.get_user_by_name(username)
        data_user_name = user_data.get("username")
        check_user_name(data_user_name)
        with allure.step(f"Check that username of the found user is {username}"):
            assert data_user_name == username, f"Username should be {username}, got {user_data['username']}"

    @allure.feature('Users')
    def test_find_posts_of_user(self, user_api_client, username):
        user_data = user_api_client.get_user_by_name(username)
        user_id = user_data.get("id")
        check_user_id(user_id, username)

        posts_by_user = user_api_client.get_posts_by_user_id(user_id)
        with allure.step("Check that each post contains correct userId"):
            for post in posts_by_user:
                post_id = post.get("id")
                user_id_in_post = post.get("userId")
                check_user_id_in_post(post_id, user_id_in_post, user_id, post)
