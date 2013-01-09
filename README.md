## nsqadmin2hipchat.py

This is a reader for [NSQ][nsq] that takes in json messages of the [format emitted by nsqadmin][nsqadmin_notify] and posts them (in a human-friendly representation) to [Hipchat][hipchat]. To use it, nsqadmin should be configured to post notifications to nsqd as described in its readme file. Everything offered as-is with no promise of success - good luck.

```
usage: nsqadmin2hipchat.py [-h] --hipchat-auth-token HIPCHAT\_AUTH\_TOKEN
                           --hipchat-room-id HIPCHAT\_ROOM\_ID --nsq-topic
                           NSQ_TOPIC [--nsq-channel NSQ\_CHANNEL] [-v]
                           (--nsqd-tcp-address NSQD\_TCP\_ADDRESS | --nsqlookupd-http-address NSQLOOKUPD\_HTTP\_ADDRESS)
```


[nsq]: https://github.com/bitly/nsq
[nsqadmin_notify]: https://github.com/bitly/nsq/tree/master/nsqadmin#admin-notifications
[hipchat]: http://hipchat.com
