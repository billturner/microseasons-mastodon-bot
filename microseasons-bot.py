from mastodon import Mastodon
import os
import sqlite3

def get_current_microseason() -> int:
    # TODO: make this a DB table lookup?
    if os.path.exists('current-microseason.txt'):
        return 1
    else:
        return 0

if __name__ == "__main__":
    # Get ENV variables, or fail

    # set up db connection
    # conn = sqlite3.connect("microseasons-data.db")

    # First, determine if there is a post/ID
    current_microseason = get_current_microseason()

    # Find current post/ID
    microseason = 12;

    # If they are different, post tweet
    if current_microseason == microseason:
        print('No change. No post.')
    else:
        print("Let's find a new one.")
        # Let's also get the current microseason division

        # Make post with microseason & division

        # Update the lock file

    print('All done.')
