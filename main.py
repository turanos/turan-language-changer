#!/usr/bin/env python3

import gi
import os
import locale
import requests
import subprocess
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gio
from locale import gettext as tr

# Tərcümə məlumatları
APPNAME = "turan-language-changer"
TRANSLATIONS_PATH = "/usr/share/locale"
SYSTEM_LANGUAGE = os.environ.get("LANG")

# Tərcümə funksiyaları
locale.bindtextdomain(APPNAME, TRANSLATIONS_PATH)
locale.textdomain(APPNAME)
locale.setlocale(locale.LC_ALL, SYSTEM_LANGUAGE)

# GTK Builder
builder = Gtk.Builder()
builder.set_translation_domain(APPNAME)
builder.add_from_file("/usr/share/turan/proqramlar/turan-language-changer/turan-language-changer.glade")

window = builder.get_object("window")

process_screen = builder.get_object("process")
finished_screen = builder.get_object("finished")
about_screen = builder.get_object("about")
window.show_all()


class Handler():
    def language_az(self, about):
      try:
          result = subprocess.run(["pkexec", "localectl", "set-locale", "LANG=az_AZ"], capture_output=True, text=True, timeout=300)
          if result.returncode == 0:
              finished_screen.show_all()
      except subprocess.TimeoutExpired:
          print("Exited")

    def language_tr(self, about):
      try:
          result = subprocess.run(["pkexec", "localectl", "set-locale", "LANG=tr_TR.UTF-8"], capture_output=True, text=True, timeout=300)
          if result.returncode == 0:
              finished_screen.show_all()
      except subprocess.TimeoutExpired:
          print("Exited")

    def language_tm(self, about):
      try:
          result = subprocess.run(["pkexec", "localectl", "set-locale", "LANG=tk_TM.UTF-8"], capture_output=True, text=True, timeout=300)
          if result.returncode == 0:
              finished_screen.show_all()
      except subprocess.TimeoutExpired:
          print("Exited")

    def language_uz(self, about):
      try:
          result = subprocess.run(["pkexec", "localectl", "set-locale", "LANG=uz_UZ.UTF-8"], capture_output=True, text=True, timeout=300)
          if result.returncode == 0:
              finished_screen.show_all()
      except subprocess.TimeoutExpired:
          print("Exited")

    def language_kz(self, about):
      try:
          result = subprocess.run(["pkexec", "localectl", "set-locale", "LANG=kk_KZ.UTF-8"], capture_output=True, text=True, timeout=300)
          if result.returncode == 0:
              finished_screen.show_all()
      except subprocess.TimeoutExpired:
          print("Exited")

    def language_kg(self, about):
      try:
          result = subprocess.run(["pkexec", "localectl", "set-locale", "LANG=ky_KG.UTF-8"], capture_output=True, text=True, timeout=300)
          if result.returncode == 0:
              finished_screen.show_all()
      except subprocess.TimeoutExpired:
          print("Exited")

    def language_en(self, about):
      try:
          result = subprocess.run(["pkexec", "localectl", "set-locale", "LANG=en_US.UTF-8"], capture_output=True, text=True, timeout=300)
          if result.returncode == 0:
              finished_screen.show_all()
      except subprocess.TimeoutExpired:
          print("Exited")

    def language_ru(self, about):
      try:
          result = subprocess.run(["pkexec", "localectl", "set-locale", "LANG=ru_RU.UTF-8"], capture_output=True, text=True, timeout=300)
          if result.returncode == 0:
              finished_screen.show_all()
      except subprocess.TimeoutExpired:
          print("Exited")

    def restart_computer(self, button):
       os.system("systemctl reboot")

    def about(self, button):
       about_screen.show_all()

builder.connect_signals(Handler())
Gtk.main()
