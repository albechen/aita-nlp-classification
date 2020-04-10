#%%
import praw
import pandas as pd
import urllib.request
import json
from datetime import datetime
import time


reddit = praw.Reddit(
    client_id="kRAJROlrIHaWMw",
    client_secret="f1EXDzFpTw1AryR_3urQ9O6I3AQ",
    user_agent="AITA_scrape",
)

# %%
def return_pushshift_data(subreddit, early_before, late_after, min_comments, min_score):
    link = (
        "https://api.pushshift.io/reddit/search/submission/?subreddit=%s&sort_type=created_utc&sort=desc&size=1000&before=%ss&after=%ss&num_comments=>%s&score=>%s"
        % (subreddit, early_before, late_after, min_comments, min_score)
    )
    print(link)
    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read())
    data = data["data"]
    return data


def unix_to_date(unix):
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(unix))
    date_time = datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    return date_time


def pushshift_reddit_search(subreddit, min_comments, min_score, years_ago):
    early_before = 0
    late_after = years_ago * 365 * 60 * 60 * 24
    matches = 1000
    id_list = []
    while matches >= 1000:
        data = return_pushshift_data(
            subreddit, early_before, late_after, min_comments, min_score
        )
        matches = len(data)
        print(matches)
        for match in range(0, matches):
            id_list.append(data[match]["id"])

        if matches == 1000:
            unix_time = int(data[matches - 1]["created_utc"])
            last_time = unix_to_date(unix_time)
            now = unix_to_date(time.time())
            early_before = int((now - last_time).total_seconds() + 60)

    return id_list


id_list = pushshift_reddit_search(
    subreddit="AmItheAsshole", min_comments=20, min_score=100, years_ago=2
)
len(id_list)

# %%
import collections

print([item for item, count in collections.Counter(id_list).items() if count > 1])

# %%
posts = []
flair_list = [
    "Asshole",
    "Everyone Sucks",
    "No A-holes here",
    "Not the A-hole",
    "Not the A-hole",
]
for n in range(0, 10):
    ids = id_list[n]
    post = praw.models.Submission(reddit=reddit, id=ids)

    if (post.link_flair_text in flair_list) and (post.selftext != "[deleted]"):
        time = post.created
        time = datetime.fromtimestamp(time)

        posts.append(
            [
                post.link_flair_text,
                post.title,
                post.score,
                post.id,
                post.num_comments,
                post.selftext,
                time,
            ]
        )

posts = pd.DataFrame(
    posts,
    columns=["flair", "title", "score", "id", "num_comments", "body", "date", "url"],
)
posts

# %%
for n in range(0, len(id_list)):
    ids = id_list[n]
    post = praw.models.Submission(reddit=reddit, id=ids)
    count = 0
    if (post.link_flair_text in flair_list) and (post.selftext != "[deleted]"):
        count += 1

count

# %%
len(id_list)
