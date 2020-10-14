from django import http
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from django.views import View

from stock.models import Info, Focus


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class IndexDataView(View):
    def get(self, request):
        indexdata = Info.objects.all()
        # 查询集转json字典
        index_data_list = []
        for i in indexdata:
            my_dict = {}
            my_dict['id'] = i.id
            my_dict['code'] = i.code
            my_dict['short'] = i.short
            my_dict['chg'] = i.chg
            my_dict['turnover'] = i.turnover
            my_dict['price'] = str(i.price)
            my_dict['highs'] = str(i.highs)
            my_dict['time'] = i.time
            index_data_list.append(my_dict)
        return http.JsonResponse(index_data_list, safe=False)


class AddFocus(View):
    def get(self, request, id):
        try:
            Focus.objects.get(id=id)
        except Exception as e:
            # 找不到对象表示数据库没有该记录，可以关注该股票
            Focus.objects.create(id=id, note_info="")
            return http.HttpResponse("关注成功！")
        else:
            return http.HttpResponse("关注失败！您已经关注过了")


class CenterView(View):
    def get(self, request):
        return render(request, 'center.html')


class RedirectIndex(View):
    def get(self, request):
        ret_url = reverse('stock:index')
        return redirect(ret_url)


class CenterDataView(View):
    def get(self, request):
        id_list = Focus.objects.all()
        center_data_list = []
        for i in id_list:
            info_obj = Info.objects.get(id=i.id)
            my_dict = {}
            my_dict["code"] = info_obj.code
            my_dict["short"] = info_obj.short
            my_dict["chg"] = info_obj.chg
            my_dict["turnover"] = info_obj.turnover
            my_dict["price"] = str(info_obj.price)
            my_dict["highs"] = str(info_obj.highs)
            my_dict["note_info"] = i.note_info
            center_data_list.append(my_dict)
        print(center_data_list)
        return http.JsonResponse(center_data_list, safe=False)


class DelFocus(View):
    def get(self, request, code):
        # 根据code，获得id,删除focus中的该id对应的记录
        info_obj = Info.objects.get(code__exact=code)
        Focus.objects.filter(id=info_obj.id).delete()
        return http.HttpResponse("删除成功！")


class UpdateFocus(View):
    def get(self, request, code):
        info_obj = Info.objects.get(code__exact=code)
        focus_obj = Focus.objects.get(id=info_obj.id)
        context = {
            'code': code,
            'note_info': focus_obj.note_info
        }
        return render(request, "update.html", context)


class UpdateNoteInfo(View):
    def get(self, request, code, noteinfo):
        info_obj = Info.objects.get(code__exact=code)
        Focus.objects.filter(id=info_obj.id).update(note_info=noteinfo)
        return http.HttpResponse("更新成功！")
