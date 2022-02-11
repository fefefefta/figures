from django.utils import timezone
from .models import Circle
from mysite.settings import PATH_TO_ARCHIVES, PATH_TO_IMAGES, PATH_TO_ORDINARY, PATH_TO_RARE, PATH_TO_UNIQUE
from random import sample, choice
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import zipfile
import uuid
import os
		

def generate_ordinary(amount):
	colors = {
		'red': (214, 47, 47),
		'blue': (66, 84, 189),
		'pink': (201, 87, 188),
		'green': (39, 179, 104),
		'black': (38, 34, 36),
		'yellow': (38, 34, 36),
	}
	background = (255, 255, 255)

	labels = [
		'Круг.\nОбычный.',
		'Некоторый\nкруг',
		'just a\nregular\neveryday\ncircle-\nmotherfucker',
		'Я просто\nкруг...',
		'А ведь\nмог быть\nредким...',
		'жив\nцел\nовал*\n*круг',
		'не путать с\nокружностью',
		'да, я\nвлажная мечта\nчеловека',
		'Кружок',
		'слава богу\nне квадрат...',
		'',
	]

	ord_circles_exist = Circle.objects.filter(ftype='O').count()
	for num in range(1, amount+1):
		path = PATH_TO_ORDINARY + '/ordinary' + str(num+ord_circles_exist) + '.png'
		img = Image.new('RGB', (250, 250), background)
		draw = ImageDraw.Draw(img)
		color = choice(list(colors.values()))
		draw.ellipse((50, 50, 200, 200), color)
		label = choice(labels)
		font = ImageFont.truetype("UbuntuMono-B.ttf", size=16)
		draw.text((85, 95), label, font=font, fill=(242, 242, 242))	
		img.save(path, 'PNG')
	print("Готово.")


def generate_rare(batch, amount_of_each): 
	collection_name = "двуцветия.vol.I"	
	collection_num = "1"

	circle_pattern_models = [
		{
			'background': (230, 2, 2),
		    'circle': (250, 205, 19),
		    'style': 'IRONMAN',
		},
		{
			'background': (236, 50, 50),
		    'circle': (1, 69, 255),
		    'style': 'кони',
		},
		{
			'background': (255, 224, 1),
		    'circle': (1, 81, 255),
		    'style': 'Столица мира',
		},
		{
			'background': (0, 0, 0),
		    'circle': (247, 247, 247),
		    'style': 'чб',
		},
		{
			'background': (230, 114, 255),
		    'circle': (0, 0, 0),
		    'style': '2007',
		},
		{
			'background': (197, 180, 170),
		    'circle': (140, 114, 98),
		    'style': 'Латте',
		},
		{
			'background': (33, 127, 207),
		    'circle': (31, 50, 118),
		    'style': 'Подводный мир',
		},
		{
			'background': (24, 10, 69),
		    'circle': (251, 203, 44),
		    'style': 'Солнце',
		},
		{
			'background': (248, 197, 204),
		    'circle': (248, 197, 204),
		    'style': 'невидимка',
		},
		{
			'background': (87, 150, 53),
		    'circle': (174, 200, 29),
		    'style': 'Природа',
		},
	]

	circle_num = 1
	for pattern in circle_pattern_models:
		for num in range(1, amount_of_each+1):
			path = PATH_TO_RARE + '/rare' + collection_num + \
				'_' + str(batch) + '_' + str(circle_num) + '.png'
			circle_num += 1	

			img = Image.new('RGB', (350, 350), pattern['background'])
			draw = ImageDraw.Draw(img)
			draw.ellipse((60, 60, 290, 290), pattern['circle'])

			text1 = 'коллекция: ' + collection_name + '\nстиль: ' + pattern['style']
			text2 = 'unique_code: ' + str(batch) + '_' + str(circle_num)	
			font = ImageFont.truetype("UbuntuMono-B.ttf", size=18)
			draw.text((10, 10), text1, font=font, fill=(242, 242, 242))	
			draw.text((10, 322), text2, font=font, fill=(242, 242, 242))	

			img.save(path, 'PNG')
	print("Готово.")


	
def create_model(ftype):
	if ftype == 'O':
		path = PATH_TO_ORDINARY
	elif ftype == 'R':
		path = PATH_TO_RARE
	elif ftype == 'U':
		path = PATH_TO_UNIQUE
	else:
		raise ValueError("No type like that.")
	
	for img in os.listdir(path):
		Circle(name=img, ftype=ftype, image=PATH_TO_IMAGES + '/' + img).save()
		os.replace(path + '/' + img, PATH_TO_IMAGES + '/' + img)


def make_archive(user, amount_of_circles):
	chosen_circles = sample(Circle.get_free_figures(), amount_of_circles)

	archive_uuid = uuid.uuid4()
	archive_name = str(archive_uuid) + '.zip' 
	path_to_archive = Path(PATH_TO_ARCHIVES, archive_name)
	with zipfile.ZipFile(path_to_archive, 'w') as zf:
		for circle in chosen_circles:
			zf.write(circle.image.path, circle.name)
			circle.owner = user
			circle.sending_date = timezone.now()
			circle.save()

	return archive_name		


