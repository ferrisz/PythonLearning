#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import requests
import xlwt
from bs4 import BeautifulSoup


class ScieSpider(object):
    def __init__(self, path=u""):
        self.page_base_url = "http://www.scie.uestc.edu.cn/main.php?action=viewTeacher&id="
        self.site_url = "http://www.scie.uestc.edu.cn/"
        self.items = ["sex", "birth", "position", "title", "email"]
        self.work_book = xlwt.Workbook()
        self.sheet = self.work_book.add_sheet('sheet 1')
        self.cursor = 0
        self.pic_path = path + u"pic/"

    def request(self, url, type):
        try:
            r = requests.get(url)
        except Exception, e:
            print e
        if type == "html":
            return r.text
        if type == "img":
            return r.content

    def parse_html(self, html):
        info = defaultdict(str)

        def gets(key, value):
            try:
                info[key] = value.contents[1].string
            except IndexError:
                info[key] = None

        soup = BeautifulSoup(html, "lxml")
        content = soup.find(id="right")
        try:
            info["name"] = content.find("h3").string.split()[0]
        except IndexError:
            return False
        info["photo_url"] = self.site_url + content.find("img")["src"]
        detail = content.find_all("li")[0:5]
        map(gets, self.items, detail)
        return info

    def save_data(self, data):
        if not data:
            return False
        col = 0
        for key in data:
            self.sheet.write(self.cursor, col, data[key])
            col += 1
        self.cursor += 1
        photo = self.request(data["photo_url"], "img")
        with open(self.pic_path + data["name"] + ".jpg", "wb") as img:
            img.write(photo)

        return True

    def start(self, top_num):
        for teacher_id in range(1, top_num):
            html_url = self.page_base_url + str(teacher_id)
            html = self.request(html_url, "html")
            data = self.parse_html(html)
            result = self.save_data(data)
            if result:
                print "get teacher_id:%s info success" % teacher_id
        self.work_book.save('info.xls')
        return True

if __name__ == "__main__":
    scie = ScieSpider()
    scie.start(150)
