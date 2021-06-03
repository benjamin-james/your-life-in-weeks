#!/usr/bin/env python3
import argparse
import datetime
from dateutil.relativedelta import relativedelta
import numpy as np
from PIL import Image, ImageDraw

def run(height, width, expectancy, birthday, output, bg, fg, border, height_offset):
	print("birth:", birthday)
	death = birthday + relativedelta(years=expectancy)
	print("death:", death)
	nweeks = abs(death-birthday).days // 7
	weeks_since_birth = abs(datetime.datetime.now() - birthday).days // 7
	print(nweeks, "weeks total")
	print(weeks_since_birth, "weeks since birth")

	cell_size = int(np.floor(np.sqrt(height * width / nweeks)))
	while cell_size * cell_size * width * height < nweeks:
		cell_size = cell_size - 1
	n_per_row = int(np.floor(width / cell_size))
	n_per_col = int(np.floor(height / cell_size))

	im = Image.new('RGB', (width, height), color=0)
	draw = ImageDraw.Draw(im)
	for W in range(nweeks):
		if W <= weeks_since_birth:
			color = fg
		else:
			color = bg
		i = W // n_per_row
		j = W - (i*n_per_row)
		draw.rectangle([(j*cell_size,height_offset+i*cell_size), ((j+1)*cell_size, height_offset+(i+1)*cell_size)], fill=color, outline=border)
	im.save(output)

if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument('--height', help="Screen height in pixels", default=1080, type=int)
	ap.add_argument('--height-offset', help="Offset from top of screen (pixels)", default=0, type=int)
	ap.add_argument('--width', help="Screen width in pixels", default=1920, type=int)
	ap.add_argument('-x', '--expectancy', help="Life expectancy (in years)", required=True, type=int)
	ap.add_argument('--bg', '--background', help="Background color (Hex code)", default="#AAAAAA")
	ap.add_argument('--fg', '--foreground', help="Foreground color (Hex code)", default="#ED7014")
	ap.add_argument('--border', help="Border color", default="#000000")
	ap.add_argument('-b', '--birthday', help="Birthday (MDY)", required=True, type=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
	ap.add_argument('-o', '--output', help="Output", required=True)
	A = ap.parse_args()
	run(height=A.height,
		width=A.width,
		expectancy=A.expectancy,
		birthday=A.birthday,
		output=A.output,
		bg=A.bg,
		fg=A.fg,
		border=A.border,
		height_offset=A.height_offset)
