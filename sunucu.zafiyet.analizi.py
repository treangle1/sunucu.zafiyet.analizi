#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Zafiyet Analiz")
print("Sunucu Zafiye Analizi Aracına Hoşgeldin instagram = zumrudu_anka_team")
print("Bu Araç Treangle Tarafından Oluşturulmuştur      ")

hedefip = input("Hedef Ip girin : ")
os.system("nikto -h " + hedefip)