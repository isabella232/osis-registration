##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2021 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
import datetime

from django.utils.translation import gettext_lazy as _

from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput

CURRENT_YEAR = datetime.date.today().year

class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = "captcha.html"

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label=_('First name'), max_length=100, required=True)
    last_name = forms.CharField(label=_('Last name'), max_length=100, required=True)
    email = forms.CharField(label=_('Email'), max_length=100, required=True)
    birth_date = forms.DateField(
        initial=datetime.datetime.now(),
        label=_('Date of birth'),
        required=True,
        widget=forms.SelectDateWidget(
            years=range(CURRENT_YEAR-100, CURRENT_YEAR+1)
        ),
    )
    captcha = CaptchaField(
        widget=CustomCaptchaTextInput()
    )
