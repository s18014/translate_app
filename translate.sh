#!/bin/bash

base=$(cd $(dirname $0); pwd)

zenity --notification --text=検索中\\n$(xsel) --timeout=1

python3 ~/bin/translate/rewrite.py

zenity --title=辞書 --width=400 --height=300 --text-info --html --filename=${base}/translate/tmp.html --timeout=30
