from calendar import isleap
from datetime import date, datetime, timedelta
from mastodon import Mastodon
from atproto import Client
import os
import sqlite3
import sys

DEBUG = False

def get_active_microseason(conn) -> int:
    cursor = conn.cursor()
    query = cursor.execute(
        "SELECT id FROM microseasons WHERE active = 1;"
    )
    result = query.fetchone();
    cursor.close()

    if result:
        return result[0];
    else:
        return 0;

def get_current_division(conn, division_id: int):
    division_sql = f"""
        SELECT description, description_jp FROM divisions
        WHERE id = {division_id};
    """
    cursor = conn.cursor()
    query = cursor.execute(division_sql)
    result = query.fetchone()
    cursor.close()

    return result

def get_current_microseason(conn):
    is_leap_year = isleap(date.today().year)
    start_day_column = 'leap_start_day' if is_leap_year else 'start_day'
    end_day_column = 'leap_end_day' if is_leap_year else 'end_day'
    current_sql = f"""
        SELECT * FROM microseasons
        WHERE (
            CAST(strftime('%j', 'now') as INTEGER) >= {start_day_column}
        ) AND (
            CAST(strftime('%j', 'now') as INTEGER) <= {end_day_column}
        );
    """

    cursor = conn.cursor()
    query = cursor.execute(current_sql)
    result = query.fetchone()
    cursor.close()

    return result

def reset_active_microseason(conn, current_id: int) -> None:
    cursor = conn.cursor()
    cursor.execute('UPDATE microseasons SET active = 0;')
    cursor.execute(f'UPDATE microseasons SET active = 1 WHERE id = {current_id};')
    conn.commit()
    cursor.close()

def get_end_date(microseason) -> str:
    is_leap_year = isleap(date.today().year)
    current_year = date.today().year
    end_day = microseason[5] if is_leap_year else microseason[3]

    will_end = datetime(current_year, 1, 1) + timedelta(end_day - 1)

    return will_end.strftime('%B %-d')

def post_to_mastodon(mastodon_base_url, mastodon_access_token, new_post):
    mastodon = Mastodon(
        access_token = mastodon_access_token,
        api_base_url = mastodon_base_url
    )
    mastodon.toot(new_post)

def post_to_bluesky(bsky_user, bsky_password, new_post):
    bsky_client = Client()
    bsky_client.login(bsky_user, bsky_password)

    # first, clear the extra newlines
    new_post = new_post.replace('\n\n\n', '\n\n')

    bsky_client.send_post(new_post)

if __name__ == "__main__":
    # Get ENV variables, or fail
    mastodon_base_url = os.getenv('MASTODON_BASE_URL')
    mastodon_access_token = os.getenv('MASTODON_ACCESS_TOKEN')
    bsky_user = os.getenv('BSKY_USER')
    bsky_password = os.getenv('BSKY_PASSWORD')
    if not mastodon_base_url and not mastodon_access_token:
        sys.exit('One of the following ENV variables are missing: MASTODON_BASE_URL, MASTODON_ACCESS_TOKEN, BSKY_USER, or BSKY_PASSWORD. Exiting.')

    # set up db connection
    conn = sqlite3.connect("microseasons.db")

    # First, determine if there is a post/ID
    active_microseason = get_active_microseason(conn)
    print(f'Found record: {active_microseason}')

    # Find current post/ID
    current_microseason = get_current_microseason(conn)

    # If they are different, post tweet
    if active_microseason == current_microseason[0]:
        print('Current microseason is the same. No update needed.')
    else:
        print("The microseason has changed. Let's post a new one.")
        # Get the current microseason division
        microseason_division = get_current_division(conn, current_microseason[1])

        # Make post with microseason & division
        new_post = f'A new microseason in the "{microseason_division[0]}" '
        new_post += f'({microseason_division[1]}) division has begun:\n\n\n'
        new_post += f'{current_microseason[6]} ({current_microseason[7]})\n\n\n'
        new_post += f'This microseason will last until '
        new_post += f'{get_end_date(current_microseason)}.'
        print(new_post)

        if not DEBUG:
            # post to Mastodon
            post_to_mastodon(mastodon_base_url, mastodon_access_token, new_post)

            # post to Bluesky
            post_to_bluesky(bsky_user, bsky_password, new_post)

            # Update the db with currently active microseason
            reset_active_microseason(conn, current_microseason[0])

    conn.close()
    print('\n\nAll done.')
