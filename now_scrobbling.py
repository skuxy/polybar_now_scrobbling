#!/usr/bin/env python
# -*_ coding: utf-8 -*-

import time
import requests

NOTHING = 'Nothing :('
API_KEY = ""
USERNAME = ''


def make_request():
    base_url = 'https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks'
    parameters = {
        'api_key':    API_KEY,
        'format':     'json',
        'limit':      '1',
        'nowplaying': 'true',
        'user':       USERNAME
    }
    return requests.get(base_url, parameters)


def process_result(response):
    response_json = response.json()
    return response_json['recenttracks']['track'][0]


def is_now_playing(track):
    if '@attr' in track:
        return track['@attr']['nowplaying'] == 'true'

    return False


def format_track(track):
    artist = track['artist']['#text']
    title = track['name']
    return '%s - %s' % (artist, title)


def main():
    while True:
        time.sleep(2)
        response = make_request()
        if response.status_code != 200:
            continue

        most_recent_track = process_result(response)

        if is_now_playing(most_recent_track):
            now_playing = format_track(most_recent_track)
            print(now_playing, flush=True)

        else:
            print(NOTHING, flush=True)


if __name__ == '__main__':
    main()
