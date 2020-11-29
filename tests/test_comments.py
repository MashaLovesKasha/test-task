import allure
from utils.validators import check_user_id, check_email
from utils.user import get_user_by_name, get_posts_by_user_id


class TestComments:
    @allure.feature('Comments. Email validation')
    def test_check_emails_in_comments_pathname_param(self, client, username):
        user_data = get_user_by_name(client, username)
        user_id = user_data.get("id")
        check_user_id(user_id, username)

        posts_by_user = get_posts_by_user_id(client, user_id)
        check_email(posts_by_user, client.get_comments_by_post_id)

    @allure.feature('Comments. Email validation')
    def test_check_emails_in_comments_query_param(self, client, username):
        user_data = get_user_by_name(client, username)
        user_id = user_data.get("id")
        check_user_id(user_id, username)

        posts_by_user = get_posts_by_user_id(client, user_id)
        check_email(posts_by_user, client.get_comments_by_post_id_query_param)
