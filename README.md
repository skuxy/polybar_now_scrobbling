# polybar_now_scrobbling
Script for outputting now scrobbling track to polybar

Modified idea from [0nse](https://github.com/0nse/now_playing/blob/master/now_playing.py)

To use this script you'll have to fetch Last FM API key, [go wild m8](https://www.last.fm/api/account/create)

Insert this key, along with your username, into empty USERNAME and API_KEY variables on the beginning of the script

Example snippet from polybar config file:

```
[module/now_playing]
type = custom/script

exec = "python3 $HOME/.scripts/now_playing.py"

tail = true

format = <label>
format-prefix = ""
format-prefix-foreground = ${colors.foreground}

label = %output:0:50%
```

![Example of this plugin in action](https://i.imgur.com/cZMv0yA.png "Example")
