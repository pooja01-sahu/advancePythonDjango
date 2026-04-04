from django.shortcuts import render
from .BaseCtl import BaseCtl
from ..utility.DataValidator import DataValidator
from ..models import Role
from ..service.RoleService import RoleService


class RoleCtl(BaseCtl):

    def display(self, request, params={}):
        res = render(request, self.get_template(), {"form": self.form})
        return res

    def submit(self, request, params={}):
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_template(self):
        return "Role.html"

    def get_service(self):
        return RoleService()
