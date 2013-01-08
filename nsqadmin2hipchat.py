#!/usr/bin/env python

import urllib
import json
import logging
import nsq
import argparse
import functools

def post_to_hipchat(txt, args):
    params = {
        'auth_token' : args.hipchat_auth_token,
        'from' : 'NSQ Admin',
        'color' : 'gray',
        'room_id' : args.hipchat_room_id,
        'message_format' : 'text',
        'message' : txt
    }
    url = "https://api.hipchat.com/v1/rooms/message"
    urllib.urlopen(url + urllib.urlencode(params))

action_text_map = {
    'create_topic' : 'Created',
    'create_channel' : 'Created',
    'delete_topic' : 'Deleted',
    'delete_channel' : 'Deleted',
    'empty_channel' : 'Emptied',
    'pause_channel' : 'Paused',
    'unpause_channel' : 'Unpaused'
}
def text_from_nsq_body(body, args):
    try:
        event = json.loads(body)
        topic_txt = 'topic %s' % event['topic']
        channel_txt = 'channel %s in ' % event['channel'] if event['channel'] else ''
        return action_text_map['action'] + " " + channel_txt + topic_txt
    except ValueError:
        logging.exception("Invalid json from nsq")


def process_message(message, args):
    msg_txt = text_from_nsq_body(message, args)
    post_to_hipchat(msg_txt, args)
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--hipchat-auth-token', required=True)
    parser.add_argument('--hipchat-room-id', required=True)
    parser.add_argument('--nsq-topic', required=True)
    parser.add_argument('--nsq-channel', default='nsqadmin2hipchat')
    sources = parser.add_mutually_exclusive_group(required=True)
    sources.add_argument('--nsqd-tcp-address', action='append')
    sources.add_argument('--nsqlookupd-http-address', action='append')
    args = parser.parse_args()
    tasks = {'post' : functools.partial(process_message, args=args)}
    kwargs = {
        'topic': args.nsq_topic,
        'channel': args.nsq_channel
    }
    if args.nsqlookupd_http_address:
        kwargs['lookupd_http_addresses'] = args.nsqlookupd_http_address
    else:
        kwargs['nsqd_tcp_addresses'] = args.nsqd_tcp_address
    r = nsq.Reader(tasks, **kwargs)
