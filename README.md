microseasons-mastodon-bot
=========================

A simple bot made to post to a [Mastodon](https://joinmastodon.org/) instance when a new microseason begins. The project is a result of finding out about the 72 microseasons (more info below), and to get in a bit of Python practice.

The repository contains CSV files for the microseasons (and their 24 divisions), and works about as simply as I could make it.

You can read up on the 72 Microseasons at the following links:

* [Japan's 72 Microseasons](https://www.nippon.com/en/features/h00124/)
* [72 Seasons](https://naturalistweekly.com/72-seasons/)

Running it yourself
-------------------

You will need two ENV variables to store the Mastodon instance:

* `MASTODON_BASE_URL`: the base URL for your instance. In our case, it's <https://botsin.space/>
* `MASTODON_ACCESS_TOKEN`: you can get one from the "Development" section in your Mastodon Profile

More to come...
