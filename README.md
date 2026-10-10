# Omarchy themes for Vivaldi

Every official [Omarchy](https://omarchy.org/) theme, as a Vivaldi browser theme,
so the browser matches the desktop. Omarchy themes its own apps, but not Vivaldi.

Built from Omarchy 4.0.4-1 — 22 themes.

## Install

Download a `.zip` from [`themes/`](themes/), then in Vivaldi:
_Settings > Themes > Import Theme..._ and pick it.

Vivaldi will not open files from inside `~/.config` or other system folders, so
keep the archives somewhere like `~/Downloads`.

## Themes

| File | Theme | Mode | Toolbars | Tab bar | Highlight | Start Page |
|---|---|---|---|---|---|---|
| `catppuccin-latte.zip` | Catppuccin Latte | light | `#eff1f5` | `#e3e4e8` | `#1e66f5` | `1-color-fade.png` |
| `catppuccin.zip` | Catppuccin | dark | `#1e1e2e` | `#161622` | `#89b4fa` | `1-totoro.png` |
| `ethereal.zip` | Ethereal | dark | `#060B1E` | `#040816` | `#7d82d9` | `1-cosmic.jpg` |
| `everforest.zip` | Everforest | dark | `#2d353b` | `#21272c` | `#7fbbb3` | `1-tree-tops.jpg` |
| `flexoki-light.zip` | Flexoki Light | light | `#FFFCF0` | `#f2efe4` | `#205EA6` | `1-orb.png` |
| `gruvbox.zip` | Gruvbox | dark | `#282828` | `#1e1e1e` | `#7daea3` | `1-the-backwater.jpg` |
| `hackerman.zip` | Hackerman | dark | `#0B0C16` | `#080910` | `#82FB9C` | `1-synth-scape.jpg` |
| `kanagawa.zip` | Kanagawa | dark | `#1f1f28` | `#17171e` | `#dcd7ba` | `1-kanagawa.jpg` |
| `last-horizon.zip` | Last Horizon | dark | `#0c0b0c` | `#090809` | `#b59790` | `1-eyes-wide.jpg` |
| `lumon.zip` | Lumon | dark | `#16242d` | `#101b21` | `#8bc9eb` | `01-united-in-severance.jpg` |
| `lupine.zip` | Lupine | light | `#fafafa` | `#ececec` | `#3264eb` | `01-cherry-blossom-bokeh.jpg` |
| `matte-black.zip` | Matte Black | dark | `#121212` | `#0d0d0d` | `#e68e0d` | `0-ship-at-sea.jpg` |
| `miasma.zip` | Miasma | dark | `#222222` | `#191919` | `#78824b` | `01-nature-of-fear.jpg` |
| `nord.zip` | Nord | dark | `#2e3440` | `#222730` | `#81a1c1` | `0-black-moon.jpg` |
| `osaka-jade.zip` | Osaka Jade | dark | `#111c18` | `#0c1512` | `#509475` | `1-glowing-city.jpg` |
| `retro-82.zip` | Retro-82 | dark | `#05182e` | `#031222` | `#faa968` | `1-in-the-groove.jpg` |
| `ristretto.zip` | Ristretto | dark | `#2c2525` | `#211b1b` | `#f38d70` | `0-launch.png` |
| `rose-pine.zip` | Rose Pine | light | `#faf4ed` | `#ede7e1` | `#56949f` | `1-funky-shapes.jpg` |
| `solitude.zip` | Solitude | dark | `#101315` | `#0c0e10` | `#798186` | `1-on-pole.jpg` |
| `tokyo-night.zip` | Tokyo Night | dark | `#1a1b26` | `#13141c` | `#7aa2f7` | `0-winding-road.jpg` |
| `vantablack.zip` | Vantablack | dark | `#000000` | `#090909` | `#8d8d8d` | `0-dot-hands.jpg` |
| `white.zip` | White | light | `#ffffff` | `#f5f5f5` | `#6e6e6e` | `1-white.jpg` |

## How a palette maps onto Vivaldi

Each theme is read from its `colors.toml`:

| Vivaldi | Omarchy | |
|---|---|---|
| Background | `background` | Toolbars, panels, address field |
| Accent | `dark_background` | Tab bar — one step off the toolbars |
| Foreground | `foreground` | Text |
| Highlight | `accent` | Focus and selection |

The Start Page shows the theme's first background, scaled to 2560px WebP.
Pages are never allowed to tint the tab bar, and there is no transparency, blur
or contrast boost — Vivaldi's contrast setting draws light strokes around the
chrome. Corners are a 4px radius.

## Rebuilding

The archives are generated, not hand-made, so they can follow Omarchy as its
themes change. With Omarchy and ImageMagick installed:

```bash
python3 build.py                          # every theme in /usr/share/omarchy/themes
python3 build.py --only nord tokyo-night  # just these
python3 build.py --themes ~/my/themes     # another themes directory
```

Your own Omarchy themes in `~/.config/omarchy/themes` work too, as long as they
ship a `colors.toml`.

## Credits

The palettes and backgrounds come from the Omarchy themes, and belong to their
original authors and artists. This repository only repackages them for Vivaldi;
the build script is MIT licensed.

Unofficial — not affiliated with Omarchy or Vivaldi.
