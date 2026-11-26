[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/competitions/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/xyzar29/deadpan-forecasts-vortessel/rank.svg)](https://make.fun/competitions/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/xyzar29/deadpan-forecasts-vortessel/reward.svg)](https://make.fun/competitions/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

# Deadpan Forecasts: Vortessel

One deadpan weather forecast for a city that does not exist, written for
the make.fun competition
[Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/competitions/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c).

## The entry

> In Vortessel, expect a high of 61 and light rain, with a brief shower of
> office chairs over the downtown core around 3 p.m.

123 characters, one line, read flat like a real broadcast — the forecast
itself is ordinary, the one absurd detail (office chairs, downtown, 3 p.m.)
is delivered as if it were routine.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` writes exactly that line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(mode 0644), clearing only the output directory's contents, never the
directory itself.

## License

MIT — see [LICENSE](LICENSE).
