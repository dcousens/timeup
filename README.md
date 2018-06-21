# timeup

## Installation
Uses [`ionicons`](http://ionicons.com/) (for the `notify-send` icon), `community/ttf-ionicons` on Arch.
Uses Python/bash.

## Usage
##### Start or stop a timer
``` bash
$ timeup
```

##### Generate a report (1 day)
``` bash
$ timeup report 12Apr

Task                     Duration
------------------------ --------------
me/timeup                2h 7m 43s
```

##### Generate a report (date to date, see [documentation](https://www.gnu.org/software/coreutils/manual/html_node/Examples-of-date.html))
``` bash
$ timeup report 12Apr 14Apr
```

or

``` bash
$ timeup report 12Apr-2018 12Apr-2019
```

or

``` bash
$ timeup report mytask
# or
$ timeup report 12Apr mytask
# or
$ timeup report 12Apr 14Apr mytask
```

##### Add untracked time
``` bash
$ timeup track me/timeup 10am 11am
```

or

``` bash
$ timeup track me/timeup 10minutes
```

# LICENSE [MIT](LICENSE)
