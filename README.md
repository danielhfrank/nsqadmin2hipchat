## nsqadmin2hipchat.py

This is a reader for [NSQ][nsq] that takes in json messages of the [format emitted by nsqadmin][nsqadmin_notify] and posts them (in a human-friendly representation) to [Hipchat][hipchat]. To use it, nsqadmin should be configured to post notifications to nsqd as described in its readme file. Everything offered as-is with no promise of success - good luck.

```
usage: nsqadmin2hipchat.py [-h] --hipchat-auth-token HIPCHAT_AUTH_TOKEN
                           --hipchat-room-id HIPCHAT_ROOM_ID --nsq-topic
                           NSQ_TOPIC [--nsq-channel NSQ_CHANNEL] [-v]
                           (--nsqd-tcp-address NSQD_TCP_ADDRESS | --nsqlookupd-http-address NSQLOOKUPD_HTTP_ADDRESS)
```


[nsq]: https://github.com/bitly/nsq
[nsqadmin_notify]: https://github.com/bitly/nsq/tree/master/nsqadmin#admin-notifications
[hipchat]: http://hipchat.com
