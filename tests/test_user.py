import allure
from utils.user import get_user_by_name, get_posts_by_user_id


class TestUser:
    @allure.feature('Users')
    @allure.story('Looking for a user by a specific name')
    def test_find_user_by_name(self, client, username):
        user_data = get_user_by_name(client, username)
        with allure.step(f"Check that name of the user is {username}"):
            assert user_data["username"] == username, f"Username should be {username}, got {user_data['username']}"

    @allure.feature('Users')
    @allure.story('Looking for all posts of a specific user')
    def test_find_posts_of_user(self, client, username):
        user_data = get_user_by_name(client, username)
        with allure.step(f"Get the userId of {username}"):
            user_id = user_data["id"]

        posts_by_user = get_posts_by_user_id(client, user_id)
        with allure.step(f"Check that each post contains the correct userId"):
            for post in posts_by_user:
                assert post["userId"] == user_id, f"UserId should be {user_id}, but got {post['userId']}"
