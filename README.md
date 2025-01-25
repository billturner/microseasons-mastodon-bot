microseasons-mastodon-bot
=========================

A simple bot made to post to a [Mastodon](https://joinmastodon.org/) instance (and now [Bluesky](https://bsky.app/)) when a new microseason begins. The project is a result of finding out about the 72 microseasons (more info below), and to get in a bit of Python practice.

The repository contains CSV files for the microseasons (and their 24 divisions), and works about as simply as I could make it.

You can read up on the 72 Microseasons at the following links:

- [Japan's 72 Microseasons](https://www.nippon.com/en/features/h00124/)
- [72 Seasons](https://naturalistweekly.com/72-seasons/)
- [More info on the bot](https://linktr.ee/microseasons)

Running it yourself
-------------------

You will need four ENV variables to store the Mastodon and Bluesky credentials:

- `MASTODON_BASE_URL`: the base URL for your instance. In our case, it's <https://mas.to/>
- `MASTODON_ACCESS_TOKEN`: you can get one from the "Development" section in your Mastodon Profile
- `BSKY_USER`: the email address used for signing up for the Bluesky account
- `BSKY_PASSWORD`: the password for the email address/account above

Acknowledgements

- Many, many thanks and <3 to [Colin Mitchell](https://muffin.industries/@colin) for hosting this bot on https://botsin.space/ for so long.
- Thanks for the [Bluesky posting instructions](https://python.plainenglish.io/creating-your-first-post-with-python-and-the-bluesky-api-c20726835d7d) by Filip Melka.

TODO

- Conditionally post to Mastodon or Bluesky, based on what ENV variables are provided
- Clean up code a bit, putting the content creation, and separate posting into different files.
