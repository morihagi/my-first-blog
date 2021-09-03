#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 20:26:43 2021

@author: Misato
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    ]