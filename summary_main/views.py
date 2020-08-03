from django.shortcuts import render
from django.views.generic.base import View

from .models import About_me, Education, Languages, Interests, Experiences, Projects, Skill_prof


class show(View):
    def get(self, request):
        summary_main = About_me.objects.all()
        education = Education.objects.all()
        skill_level = Skill_prof.objects.all()
        language = Languages.objects.all()
        interests = Interests.objects.all()
        exp = Experiences.objects.all()
        prj = Projects.objects.all()

        return render(request, "summary_main/index.html", {'index': summary_main,
                                                           'educations': education,
                                                           'skill_prof': skill_level,
                                                           'languages': language,
                                                           'interest': interests,
                                                           'experienc': exp,
                                                           'projects': prj,
                                                           })




