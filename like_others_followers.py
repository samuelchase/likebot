
import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''
insta_password = ''

# restriction data
dont_likes = ['sex', 'nude', 'naked', 'beef', 'pork', 'seafood',
              'egg', 'chicken', 'cheese', 'sausage', 'lobster',
              'fisch', 'schwein', 'lamm', 'rind', 'kuh',
              'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
              'meal', 'food', 'eat', 'pancake', 'cake', 'dessert',
              'protein', 'essen', 'mahl', 'breakfast', 'lunch',
              'dinner', 'turkey', 'truthahn', 'plate', 'bacon',
              'sushi', 'burger', 'salmon', 'shrimp', 'steak',
              'schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
              'breakfast', 'dinner', 'lunch']


like_tag_list = [u'sadhguru', u'sadhguruquotes', u'innerengineering',
                 u'yogisofinstagram', u'travelcouples', u'spiritualcouples']

# ignore_users = ['user1', 'user2', 'user3']

""" Prevent commenting on and unfollowing your good friends (the images will
still be liked)...
"""
friends = ['miss.nonum']

""" Prevent posts that contain...
"""
ignore_list = []

# TARGET data
""" Set similar accounts and influencers from your niche to target...
"""
targets = ['sadhguru', 'deepikamehtayoga', 'yoga.guide', 'sadhgurus_quotes',
           '_hananelazaar', 'spiritdaughter', 'awake_spiritual', 'thetravelduos', 'creativetravelcouples',
           'thetwobohemians', 'findingmorgantyler', 'chelseasyoga', 'jacobmanningyoga']

""" Skip all business accounts, except from list given...
"""
target_business_categories = ['Artist', 'Public Figure']

# COMMENT data
comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  disable_image_load=True,
                  multi_logs=True)

# friends = session.grab_following(username="soma.yoga.life", amount="full", live_match=False, store_locally=False)
# friends += session.grab_followers(username="soma.yoga.life", amount="full", live_match=False, store_locally=False)


# let's go! :>
with smart_run(session):
    # HEY HO LETS GO
    # general settings

    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)
    # session.set_ignore_users(ignore_users)
    session.set_simulation(enabled=True)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=50000,
                                    max_following=3000,
                                    min_followers=25,
                                    min_following=25,
                                    min_posts=50)

    session.set_skip_users(skip_private=True,
                           skip_no_profile_pic=True,
                           skip_business=True,
                           dont_skip_business_categories=[
                               target_business_categories])

    session.set_user_interact(amount=3, randomize=True, percentage=80,
                              media='Photo')
    session.set_do_like(enabled=True, percentage=90)
    session.like_by_tags(like_tag_list, randomize=True, amount=100, media='Photo')
    # session.set_do_comment(enabled=True, percentage=15)
    # session.set_comments(comments, media='Photo')
    # session.set_do_follow(enabled=True, percentage=40, times=1)

    # activities

    # FOLLOW+INTERACTION on TARGETED accounts
    """ Select users form a list of a predefined targets...
    """
    number = random.randint(3, 5)
    random_targets = targets

    if len(targets) <= number:
        random_targets = targets

    else:
        random_targets = random.sample(targets, number)

    session.interact_user_followers(targets, amount=3, randomize=True, percentage=100)

    # """ Interact with the chosen targets...
    # """
    # session.follow_user_followers(random_targets,
    #                               amount=random.randint(30, 60),
    #                               randomize=True, sleep_delay=600,
    #                               interact=True)
    #
    # # UNFOLLOW activity
    # """ Unfollow nonfollowers after one day...
    # """
    # session.unfollow_users(amount=random.randint(75, 100),
    #                        InstapyFollowed=(True, "nonfollowers"),
    #                        style="FIFO",
    #                        unfollow_after=24 * 60 * 60, sleep_delay=600)
    #
    # """ Unfollow all users followed by InstaPy after one week to keep the
    # following-level clean...
    # """
    # session.unfollow_users(amount=random.randint(75, 100),
    #                        InstapyFollowed=(True, "all"), style="FIFO",
    #                        unfollow_after=168 * 60 * 60, sleep_delay=600)
    #
    # """ Joining Engagement Pods...
    # """
    # session.join_pods()




    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes=(57, 585),
                               peak_comments=(21, 182),
                                peak_follows=(48, None),
                                 peak_unfollows=(35, 402),
                                  peak_server_calls=(None, 4700))






#
# session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
# session.set_do_follow(enabled=False, percentage=70)
# session.set_do_like(enabled=False, percentage=70)
# session.set_comments(["Cool", "Super!"])
# session.set_do_comment(enabled=True, percentage=80)
# session.interact_user_followers(['natgeo'], amount=10, randomize=True)
