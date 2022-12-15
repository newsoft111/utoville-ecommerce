from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from ..models import Profit as ProfitModel
from django.core.paginator import Paginator
from django.http import JsonResponse
from order.models import *
import json, re