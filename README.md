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

Generate a report (date to date, see [documentation](https://www.gnu.org/software/coreutils/manual/html_node/Examples-of-date.html))
``` bash
$ timeup report 12Apr 14Apr

...
```

or

``` bash
$ timeup report 12Apr-2018 12Apr-2019

...
```

Uses [`ionicons`](http://ionicons.com/) (for the `notify-send` icon), `community/ttf-ionicons` on Arch
