import pandas as pd
from facebook_scraper import get_posts
import b64


def main():
    fb_users = ['NikkyHaley', 'VivekGRamaswamy', 'coreysongs', 'DonaldTrump', 'williamsonmarianne']

    for user in fb_users:
        print(f"Started getting posts for {user}")
        fb_posts_by_user_as_csv(user)
        print(f"Finished getting posts for {user}")


def fb_posts_by_user_as_csv(user):
    fb_posts = []
    for i, post in enumerate(get_posts('nintendo', pages=10, cookies='cookies.txt')):
        encoded_text = b64.encode(post['post_text'])
        fb_posts.append([encoded_text, post['time'], post['post_url']])

    fb_posts_df = pd.DataFrame(fb_posts, columns=['Text', 'DateTime', 'Url'])
    fb_posts_df.to_csv(f"fb_{user}.csv", index=False)


# def fb_posts_by_user_as_csv(fb_username, count_max):
#     fb_posts = []
#     for i, fb_post in enumerate(snfacebook.FacebookUserScraper(fb_username).get_items()):
#         if i > count_max:
#             break
#         fb_posts.append([fb_post.date, b64.encode(fb_post.content), fb_post.cleanUrl])
#
#     fb_posts_df = pd.DataFrame(fb_posts, columns=['DateTime', 'Text', 'CleanUrl'])
#     fb_posts_df.to_csv(f"fb_{fb_username}.csv", index=False)


main()
