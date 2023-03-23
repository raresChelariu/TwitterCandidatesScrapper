import snscrape.modules.facebook as snfacebook
import pandas as pd
import b64


def main():
    fb_users = ['NikkyHaley', 'VivekGRamaswamy', 'coreysongs', 'DonaldTrump', 'williamsonmarianne']

    for user in fb_users:
        fb_posts_by_user_as_csv(fb_username=user, count_max=1000)


def fb_posts_by_user_as_csv(fb_username, count_max):
    fb_posts = []
    for i, fb_post in enumerate(snfacebook.FacebookUserScraper(username=fb_username).get_items()):
        if i > count_max:
            break
        fb_posts.append([fb_post.date, b64.encode(fb_post.content), fb_post.cleanUrl])

    fb_posts_df = pd.DataFrame(fb_posts, columns=['DateTime', 'Text', 'CleanUrl'])
    fb_posts_df.to_csv(f"fb_{fb_username}.csv", index=False)


main()
