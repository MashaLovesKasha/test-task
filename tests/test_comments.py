import allure
from utils.validators import email_validation
from utils.user import get_user_by_name, get_posts_by_user_id


class TestComments:
    @allure.feature('Comments. Email validation')
    @allure.story('The request with a parameter in the pathname')
    def test_check_emails_in_comments_pathname_param(self, client, username):
        user_data = get_user_by_name(client, username)
        with allure.step(f"Get the userId of {username}"):
            user_id = user_data["id"]

        posts_by_user = get_posts_by_user_id(client, user_id)

        with allure.step(f"Get comments of each post"):
            for post in posts_by_user:
                post_id = post["id"]
                comments = client.get_comments_by_post_id(post_id).json()
                with allure.step(f"Check that each comment contains the valid email"):
                    for comment in comments:
                        email = comment["email"]
                        assert email_validation(email), f"The email {email} is not valid"

    @allure.feature('Comments. Email validation')
    @allure.story('The request with a query-parameter')
    def test_check_emails_in_comments_query_param(self, client, username):
        user_data = get_user_by_name(client, username)
        user_id = user_data["id"]

        posts_by_user = get_posts_by_user_id(client, user_id)

        with allure.step(f"Get comments of each post"):
            for post in posts_by_user:
                post_id = post["id"]
                comments = client.get_comments_by_post_id_query_param(post_id).json()
                with allure.step(f"Check that each comment contains the valid email"):
                    for comment in comments:
                        email = comment["email"]
                        assert email_validation(email), f"The email {email} is not valid"
