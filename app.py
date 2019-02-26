from flask import request
from htmlparsing import Attr, Text
from toapi import Api, Item
import re
import time


api = Api()

@api.site('https://www.douguo.com')
@api.list('ul.recipe-list > li.item')
@api.route('/index', '/')
class Selected(Item):
    title = Text('.name')
    img = Attr('a > img', 'src')
    url = Attr('.name', 'href')


@api.site('https://www.douguo.com')
@api.route('/cookbook/{id}', '/cookbook/{id}.html')
class Cookbook(Item):
    title = Text('h2.title')
    img = Attr('.recipe-content > div > div > div > a > img', 'src')
    browse_count = Text('div.vcnum > span')
    collect_count = Text('div.vcnum > span.collectnum')
    intro = Text('p.intro')
    tip = Text('div.tips > p')


@api.site('https://www.douguo.com')
@api.list('div.stepcont')
@api.route('/cookbook/{id}', '/cookbook/{id}.html')
class Step(Item):
    img = Attr('img', 'src')
    step = Text('p')


@api.site('https://www.douguo.com')
@api.list('table.retamr  td')
@api.route('/cookbook/{id}', '/cookbook/{id}.html')
class Ingredients(Item):
    ingredient = Text('span')
    weight = Text('span.right')


@api.site('https://www.douguo.com')
@api.list('li.clearfix')
@api.route('/search/{keyword}/{page}', '/search/recipe/{keyword}/0/{page}')
@api.route('/search/{keyword}', '/search/recipe/{keyword}')
class Repic(Item):
    img = Attr('a.cook-img', 'style')
    url = Attr('a.cook-img', 'href')
    title = Text('div.cook-info > a.cookname')
    major = Text('div.cook-info > p.major')

    def clean_img(self, img):
        re_img = re.compile('background: url[(](.*)[)] no-repeat center center;background-size: cover;position: relative;')
        return re_img.match(img).groups()[0]


@api.site('https://www.douguo.com')
@api.route('/search/{keyword}/{page}', '/search/recipe/{keyword}/0/{page}')
@api.route('/search/{keyword}', '/search/recipe/{keyword}')
class Page(Item):

    current = Attr('div.mt20 > div.pages > a.anext', 'href')
    total = Attr('div.mt20 > div.pages > a.alast', 'href')

    def clean_total(self, total):
        return int(total.rsplit('/', 1)[1])

    def clean_current(self, current):
        print (current)
        return int(current.rsplit('/', 1)[1]) - 20

if __name__ == '__main__':
    api.run('0.0.0.0', debug=True)
