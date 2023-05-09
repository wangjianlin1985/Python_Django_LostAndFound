from django.views.generic import View
from apps.BaseView import BaseView
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.Praise.models import Praise
from apps.LostFound.models import LostFound
from django.http import JsonResponse
from django.http import FileResponse
from apps.BaseView import ImageFormatException
from django.conf import settings
import pandas as pd
import os


class FrontAddView(BaseView):  # 前台表扬添加
    def get(self,request):
        lostFounds = LostFound.objects.all()  # 获取所有失物招领
        context = {
            'lostFounds': lostFounds,
        }

        # 使用模板
        return render(request, 'Praise/praise_frontAdd.html', context)

    def post(self, request):
        praise = Praise() # 新建一个表扬对象然后获取参数
        praise.lostFoundObj = LostFound.objects.get(lostFoundId=request.POST.get('praise.lostFoundObj.lostFoundId'))
        praise.title = request.POST.get('praise.title')
        praise.contents = request.POST.get('praise.contents')
        praise.addTime = request.POST.get('praise.addTime')
        praise.save() # 保存表扬信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class FrontModifyView(BaseView):  # 前台修改表扬
    def get(self, request, praiseId):
        context = {'praiseId': praiseId}
        return render(request, 'Praise/praise_frontModify.html', context)


class FrontListView(BaseView):  # 前台表扬查询列表
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        self.getCurrentPage(request)  # 获取当前要显示第几页
        # 下面获取查询参数
        lostFoundObj_lostFoundId = self.getIntParam(request, 'lostFoundObj.lostFoundId')
        title = self.getStrParam(request, 'title')
        addTime = self.getStrParam(request, 'addTime')
        # 然后条件组合查询过滤
        praises = Praise.objects.all()
        if lostFoundObj_lostFoundId != '0':
            praises = praises.filter(lostFoundObj=lostFoundObj_lostFoundId)
        if title != '':
            praises = praises.filter(title__contains=title)
        if addTime != '':
            praises = praises.filter(addTime__contains=addTime)
        # 对查询结果利用Paginator进行分页
        self.paginator = Paginator(praises, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        praises_page = self.paginator.page(self.currentPage)

        # 获取所有失物招领
        lostFounds = LostFound.objects.all()
        # 构造模板需要的参数
        context = {
            'lostFounds': lostFounds,
            'praises_page': praises_page,
            'lostFoundObj_lostFoundId': int(lostFoundObj_lostFoundId),
            'title': title,
            'addTime': addTime,
            'currentPage': self.currentPage,
            'totalPage': self.totalPage,
            'recordNumber': self.recordNumber,
            'startIndex': self.startIndex,
            'pageList': self.pageList,
        }
        # 渲染模板界面
        return render(request, 'Praise/praise_frontquery_result.html', context)


class FrontShowView(View):  # 前台显示表扬详情页
    def get(self, request, praiseId):
        # 查询需要显示的表扬对象
        praise = Praise.objects.get(praiseId=praiseId)
        context = {
            'praise': praise
        }
        # 渲染模板显示
        return render(request, 'Praise/praise_frontshow.html', context)


class ListAllView(View): # 前台查询所有表扬
    def get(self,request):
        praises = Praise.objects.all()
        praiseList = []
        for praise in praises:
            praiseObj = {
                'praiseId': praise.praiseId,
                'title': praise.title,
            }
            praiseList.append(praiseObj)
        return JsonResponse(praiseList, safe=False)


class UpdateView(BaseView):  # Ajax方式表扬更新
    def get(self, request, praiseId):
        # GET方式请求查询表扬对象并返回表扬json格式
        praise = Praise.objects.get(praiseId=praiseId)
        return JsonResponse(praise.getJsonObj())

    def post(self, request, praiseId):
        # POST方式提交表扬修改信息更新到数据库
        praise = Praise.objects.get(praiseId=praiseId)
        praise.lostFoundObj = LostFound.objects.get(lostFoundId=request.POST.get('praise.lostFoundObj.lostFoundId'))
        praise.title = request.POST.get('praise.title')
        praise.contents = request.POST.get('praise.contents')
        praise.addTime = request.POST.get('praise.addTime')
        praise.save()
        return JsonResponse({'success': True, 'message': '保存成功'})

class AddView(BaseView):  # 后台表扬添加
    def get(self,request):
        lostFounds = LostFound.objects.all()  # 获取所有失物招领
        context = {
            'lostFounds': lostFounds,
        }

        # 渲染显示模板界面
        return render(request, 'Praise/praise_add.html', context)

    def post(self, request):
        # POST方式处理图书添加业务
        praise = Praise() # 新建一个表扬对象然后获取参数
        praise.lostFoundObj = LostFound.objects.get(lostFoundId=request.POST.get('praise.lostFoundObj.lostFoundId'))
        praise.title = request.POST.get('praise.title')
        praise.contents = request.POST.get('praise.contents')
        praise.addTime = request.POST.get('praise.addTime')
        praise.save() # 保存表扬信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class BackModifyView(BaseView):  # 后台更新表扬
    def get(self, request, praiseId):
        context = {'praiseId': praiseId}
        return render(request, 'Praise/praise_modify.html', context)


class ListView(BaseView):  # 后台表扬列表
    def get(self, request):
        # 使用模板
        return render(request, 'Praise/praise_query_result.html')

    def post(self, request):
        # 获取当前要显示第几页和每页几条数据
        self.getPageAndSize(request)
        # 收集查询参数
        lostFoundObj_lostFoundId = self.getIntParam(request, 'lostFoundObj.lostFoundId')
        title = self.getStrParam(request, 'title')
        addTime = self.getStrParam(request, 'addTime')
        # 然后条件组合查询过滤
        praises = Praise.objects.all()
        if lostFoundObj_lostFoundId != '0':
            praises = praises.filter(lostFoundObj=lostFoundObj_lostFoundId)
        if title != '':
            praises = praises.filter(title__contains=title)
        if addTime != '':
            praises = praises.filter(addTime__contains=addTime)
        # 利用Paginator对查询结果集分页
        self.paginator = Paginator(praises, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        praises_page = self.paginator.page(self.currentPage)
        # 查询的结果集转换为列表
        praiseList = []
        for praise in praises_page:
            praise = praise.getJsonObj()
            praiseList.append(praise)
        # 构造模板页面需要的参数
        praise_res = {
            'rows': praiseList,
            'total': self.recordNumber,
        }
        # 渲染模板页面显示
        return JsonResponse(praise_res, json_dumps_params={'ensure_ascii':False})

class DeletesView(BaseView):  # 删除表扬信息
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        praiseIds = self.getStrParam(request, 'praiseIds')
        praiseIds = praiseIds.split(',')
        count = 0
        try:
            for praiseId in praiseIds:
                Praise.objects.get(praiseId=praiseId).delete()
                count = count + 1
            message = '%s条记录删除成功！' % count
            success = True
        except Exception as e:
            message = '数据库外键约束删除失败！'
            success = False
        return JsonResponse({'success': success, 'message': message})


class OutToExcelView(BaseView):  # 导出表扬信息到excel并下载
    def get(self, request):
        # 收集查询参数
        lostFoundObj_lostFoundId = self.getIntParam(request, 'lostFoundObj.lostFoundId')
        title = self.getStrParam(request, 'title')
        addTime = self.getStrParam(request, 'addTime')
        # 然后条件组合查询过滤
        praises = Praise.objects.all()
        if lostFoundObj_lostFoundId != '0':
            praises = praises.filter(lostFoundObj=lostFoundObj_lostFoundId)
        if title != '':
            praises = praises.filter(title__contains=title)
        if addTime != '':
            praises = praises.filter(addTime__contains=addTime)
        #将查询结果集转换成列表
        praiseList = []
        for praise in praises:
            praise = praise.getJsonObj()
            praiseList.append(praise)
        # 利用pandas实现数据的导出功能
        pf = pd.DataFrame(praiseList)
        # 设置要导入到excel的列
        columns_map = {
            'praiseId': '表扬id',
            'lostFoundObj': '招领信息',
            'title': '标题',
            'contents': '表扬内容',
            'addTime': '表扬时间',
        }
        pf = pf[columns_map.keys()]
        pf.rename(columns=columns_map, inplace=True)
        # 将空的单元格替换为空字符
        pf.fillna('', inplace=True)
        #设定文件名和导出路径
        filename = 'praises.xlsx'
        # 这个路径可以在settings中设置也可以直接手动输入
        root_path = settings.MEDIA_ROOT + '/output/'
        file_path = os.path.join(root_path, filename)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        # 将生成的excel文件输出到网页下载
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="praises.xlsx"'
        return response

