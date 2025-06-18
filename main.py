import time
import snscrape.modules.twitter as sntwitter

# Yapper handles to monitor (replace with your targets)
yappers = ["@ChainlinkMongol", "@0xFeetPic", "@Amrit12005", "@0xCrash_", "@S_i_n_z_u"]  # Example: replace these

# Track last seen tweet per user
last_seen = {}

def check_new_tweets():
    for handle in yappers:
        query = f"from:{handle}"
        tweets = list(sntwitter.TwitterSearchScraper(query).get_items())
        if not tweets:
            continue
        latest_tweet = tweets[0]
        tweet_id = latest_tweet.id
        tweet_text = latest_tweet.content
        tweet_url = f"https://x.com/{handle[1:]}/status/{tweet_id}"

        if handle not in last_seen or tweet_id != last_seen[handle]:
            print(f"[NEW] {handle}: {tweet_text[:80]}...")
            print(f"URL: {tweet_url}")
            last_seen[handle] = tweet_id

if __name__ == "__main__":
    while True:
        print("Checking yappers...")
        check_new_tweets()
        time.sleep(15)  # Check every 15 seconds
