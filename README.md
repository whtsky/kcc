# KCC_headless

[KindleComicConverter](https://github.com/ciromattia/kcc) sans GUI, PyQt and raven(Sentry).

## PYPI
**KCC** is also available on PyPI.
```
pip install KindleComicConverter_headless
```

### Standalone `kcc-c2e.py` usage:

```
Usage: kcc-c2e [options] comic_file|comic_folder

Options:
  MAIN:
    -p PROFILE, --profile=PROFILE
                        Device profile (Available options: K1, K2, K34, K578,
                        KDX, KPW, KV, KO, KoMT, KoG, KoGHD, KoA, KoAHD, KoAH2O,
                        KoAO, KoF) [Default=KV]
    -m, --manga-style   Manga style (right-to-left reading and splitting)
    -q, --hq            Try to increase the quality of magnification
    -2, --two-panel     Display two not four panels in Panel View mode
    -w, --webtoon       Webtoon processing mode
    --targetsize=TARGETSIZE
                        the maximal size of output file in MB.[Default=100MB
                        for webtoon and 400MB for others]
  OUTPUT SETTINGS:
    -o OUTPUT, --output=OUTPUT
                        Output generated file to specified directory or file
    -t TITLE, --title=TITLE
                        Comic title [Default=filename or directory name]
    -f FORMAT, --format=FORMAT
                        Output format (Available options: Auto, MOBI, EPUB,
                        CBZ, KFX) [Default=Auto]
    -b BATCHSPLIT, --batchsplit=BATCHSPLIT
                        Split output into multiple files. 0: Don't split 1:
                        Automatic mode 2: Consider every subdirectory as
                        separate volume [Default=0]

  PROCESSING:
    -u, --upscale       Resize images smaller than device's resolution
    -s, --stretch       Stretch images to device's resolution
    -r SPLITTER, --splitter=SPLITTER
                        Double page parsing mode. 0: Split 1: Rotate 2: Both
                        [Default=0]
    -g GAMMA, --gamma=GAMMA
                        Apply gamma correction to linearize the image
                        [Default=Auto]
    -c CROPPING, --cropping=CROPPING
                        Set cropping mode. 0: Disabled 1: Margins 2: Margins +
                        page numbers [Default=2]
    --cp=CROPPINGP, --croppingpower=CROPPINGP
                        Set cropping power [Default=1.0]
    --blackborders      Disable autodetection and force black borders
    --whiteborders      Disable autodetection and force white borders
    --forcecolor        Don't convert images to grayscale
    --forcepng          Create PNG files instead JPEG

  CUSTOM PROFILE:
    --customwidth=CUSTOMWIDTH
                        Replace screen width provided by device profile
    --customheight=CUSTOMHEIGHT
                        Replace screen height provided by device profile

  OTHER:
    -h, --help          Show this help message and exit
```

### Standalone `kcc-c2p.py` usage:

```
Usage: kcc-c2p [options] comic_folder

Options:
  MANDATORY:
    -y HEIGHT, --height=HEIGHT
                        Height of the target device screen
    -i, --in-place      Overwrite source directory
    -m, --merge         Combine every directory into a single image before splitting

  OTHER:
    -d, --debug         Create debug file for every split image
    -h, --help          Show this help message and exit
```

## CREDITS
**KCC** is made by [Ciro Mattia Gonano](http://github.com/ciromattia) and [Paweł Jastrzębski](http://github.com/AcidWeb).

## COPYRIGHT
Copyright (c) 2012-2019 Ciro Mattia Gonano and Paweł Jastrzębski.
**KCC** is released under ISC LICENSE; see LICENSE.txt for further details.
