# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

# Create your views here.
class ClientListView(generic.ListView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        return context

class ClientJsonView(APIView):
    def get(self, request, format=None):
        clients = Client.objects.all()
        serialized = ClientSerializer(clients, many=True)
        return Response({'data':serialized.data})