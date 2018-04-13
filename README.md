# timeup

Start or stop a timer
``` bash
$ timeup
```

Generate a report (1 day)
``` bash
$ timeup report 12Apr

Task                     Duration
------------------------ --------------
me/timeup                2h 7m 43s
```

Generate a report (date to date)
``` bash
$ timeup report 12Apr 14Apr

...
```

Uses [`ionicons`](http://ionicons.com/) (for the `notify-send` icon), `community/ttf-ionicons` on Arch
