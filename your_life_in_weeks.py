#!/usr/bin/env python3
import argparse
import datetime
from dateutil.relativedelta import relativedelta
import numpy as np
from PIL import Image, ImageDraw ## pillow package

def run(height, width, expectancy, birthday, output, bg, fg, border, margin_top, margin_bot, margin_left, margin_right):
	print("birth:", birthday)
	death = birthday + relativedelta(years=expectancy)
	print("death:", death)
	nweeks = abs(death-birthday).days // 7
	weeks_since_birth = abs(datetime.datetime.now() - birthday).days // 7
	print(nweeks, "weeks total")
	print(weeks_since_birth, "weeks since birth")


	grid_height = (height - (margin_top + margin_bot))
	grid_width = (width - (margin_left + margin_right))
	cell_size = int(np.floor(np.sqrt(grid_height * grid_width / nweeks)))
	while cell_size * cell_size * grid_width * grid_height < nweeks:
		cell_size = cell_size - 1
	n_per_row = int(np.floor(grid_width / cell_size))
	n_per_col = int(np.floor(grid_height / cell_size))
	w_remainder = grid_width - n_per_row * cell_size
	h_remainder = grid_height - n_per_col * cell_size
	w_offset = margin_left + w_remainder // 2
	h_offset = margin_top + h_remainder // 2

	im = Image.new('RGB', (width, height), color=border)
	draw = ImageDraw.Draw(im)
	for W in range(nweeks):
		if W <= weeks_since_birth:
			color = fg
		else:
			color = bg
		i = W // n_per_row
		j = W - (i*n_per_row)
		x = w_offset + j * cell_size
		y = h_offset + i * cell_size
		draw.rectangle([(x,y), (x + cell_size, y + cell_size)], fill=color, outline=border)
	im.save(output)

if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument('--height', help="Screen height in pixels", default=1080, type=int)
	ap.add_argument('--width', help="Screen width in pixels", default=1920, type=int)
	ap.add_argument('-x', '--expectancy', help="Life expectancy (in years)", required=True, type=int)
	ap.add_argument('--bg', '--background', help="Background color (Hex code)", default="#AAAAAA")
	ap.add_argument('--fg', '--foreground', help="Foreground color (Hex code)", default="#ED7014")
	ap.add_argument('--border', help="Border color", default="#000000")
	ap.add_argument('-b', '--birthday', help="Birthday (YYYY-MM-DD)", required=True, type=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
	ap.add_argument('-o', '--output', help="Output", required=True)
	ap.add_argument('--top', "--margin-top", help="Offset from top of screen (pixels)", default=0, type=int)
	ap.add_argument('--bot', "--margin-bottom", help="Offset from bottom of screen (pixels)", default=0, type=int)
	ap.add_argument('--left', "--margin-left", help="Offset from left of screen (pixels)", default=0, type=int)
	ap.add_argument('--right', "--margin-right", help="Offset from right of screen (pixels)", default=0, type=int)
	A = ap.parse_args()
	run(height=A.height,
		width=A.width,
		expectancy=A.expectancy,
		birthday=A.birthday,
		output=A.output,
		bg=A.bg,
		fg=A.fg,
		border=A.border,
		margin_top=A.top,
		margin_bot=A.bot,
		margin_left=A.left,
		margin_right=A.right)
