from utils.validators import email_validation
from utils.user import get_user_by_name, get_posts_by_user_id


class TestExample():

    def test_find_user_by_name(self, client, username):
        user_data = get_user_by_name(client, username)
        assert user_data["username"] == username, f"Username should be {username}, but got {user_data['username']}"

    def test_find_posts_of_user(self, client, username):
        # get the user_id by username
        user_data = get_user_by_name(client, username)
        user_id = user_data["id"]

        # get the user's posts by user_id
        posts_by_user = get_posts_by_user_id(client, user_id)
        for post in posts_by_user:
            assert post["userId"] == user_id, f"UserId should be {user_id}, but got {post['userId']}"

    def test_check_emails_in_comments(self, client, username):
        # get the user_id by username
        user_data = get_user_by_name(client, username)
        user_id = user_data["id"]

        # get user's posts by user_id
        posts_by_user = get_posts_by_user_id(client, user_id)

        # get comments of each post
        for post in posts_by_user:
            post_id = post["id"]
            comments = client.get_comments_by_post_id(post_id).json()
            for comment in comments:
                email = comment["email"]
                assert email_validation(email), f"The email {email} is not valid"

    def test_check_emails_in_comments_v2(self, client, username):
        # get the user_id by username
        user_data = get_user_by_name(client, username)
        user_id = user_data["id"]

        # get user's posts by user_id
        posts_by_user = get_posts_by_user_id(client, user_id)

        # get comments of each post
        for post in posts_by_user:
            post_id = post["id"]
            comments = client.get_comments_by_post_id_v2(post_id).json()
            for comment in comments:
                email = comment["email"]
                assert email_validation(email), f"The email {email} is not valid"
