from utils.validators import email_validation


class TestExample:

    def test_get_user_by_name(self, client, username):
        res = client.get_user_by_name(username)
        assert res.status_code == 200
        user_data = res.json()[0]
        assert user_data["username"] == username
        # проверить на не пустоту

    def test_get_posts_by_user_id(self, client, username):
        # get the user_id by username
        user_result = client.get_user_by_name(username)
        assert user_result.status_code == 200
        user_data = user_result.json()[0]
        user_id = user_data["id"]

        # get the user's posts by user_id
        posts_by_user_result = client.get_posts_by_user_id(user_id)
        assert posts_by_user_result.status_code == 200
        # проверить на не пустоту
        posts_by_user = posts_by_user_result.json()
        for post in posts_by_user:
            assert post["userId"] == user_id

    def test_check_emails_in_comments(self, client, username):
        # get the user_id by username
        user_result = client.get_user_by_name(username)
        assert user_result.status_code == 200
        user_data = user_result.json()[0]
        user_id = user_data["id"]

        # get user's posts by user_id
        posts_by_user_result = client.get_posts_by_user_id(user_id)
        assert posts_by_user_result.status_code == 200
        # проверить на не пустоту
        posts_by_user = posts_by_user_result.json()

        # get comments of each post
        for post in posts_by_user:
            post_id = post["id"]
            comments = client.get_comments_by_post_id(post_id).json()
            for comment in comments:
                email = comment["email"]
                assert email_validation(email), f"The email {email} is not valid"

    def test_check_emails_in_comments_v2(self, client, username):
        # get the user_id by username
        user_result = client.get_user_by_name(username)
        assert user_result.status_code == 200
        user_data = user_result.json()[0]
        user_id = user_data["id"]

        # get user's posts by user_id
        posts_by_user_result = client.get_posts_by_user_id(user_id)
        assert posts_by_user_result.status_code == 200
        # проверить на не пустоту
        posts_by_user = posts_by_user_result.json()

        # get comments of each post
        for post in posts_by_user:
            post_id = post["id"]
            comments = client.get_comments_by_post_id_v2(post_id).json()
            for comment in comments:
                email = comment["email"]
                assert email_validation(email), f"The email {email} is not valid"
