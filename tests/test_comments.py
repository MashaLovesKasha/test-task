import allure
from utils.validators import check_user_id, check_email


class TestComments:
    @allure.feature('Comments. Email validation')
    def test_check_emails_in_comments_pathname_param(self, user_api_client, username):
        user_data = user_api_client.get_user_by_name(username)
        user_id = user_data.get("id")
        check_user_id(user_id, username)

        posts_by_user = user_api_client.get_posts_by_user_id(user_id)
        check_email(posts_by_user, user_api_client.get_comments_by_post_id)

    @allure.feature('Comments. Email validation')
    def test_check_emails_in_comments_query_param(self, user_api_client, username):
        user_data = user_api_client.get_user_by_name(username)
        user_id = user_data.get("id")
        check_user_id(user_id, username)

        posts_by_user = user_api_client.get_posts_by_user_id(user_id)
        check_email(posts_by_user, user_api_client.get_comments_by_post_id_query_param)
