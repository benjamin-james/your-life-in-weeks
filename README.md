# your-life-in-weeks
Desktop wallpaper generator highlighting the number of weeks in your life

An example script to be run by your window manager/display manager on unlock:

    #!/usr/bin/env bash
	HEIGHT=800
	WIDTH=1280
	WALLPAPER=$(mktemp --suffix=".png")
	python3 /PATH/TO/your_life_in_weeks.py --height ${HEIGHT} --width ${WIDTH} -x 80 -b 'YYYY-MM-DD' -o ${WALLPAPER}
	feh --bg-scale ${WALLPAPER}
