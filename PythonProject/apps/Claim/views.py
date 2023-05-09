from django.views.generic import View
from apps.BaseView import BaseView
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.Claim.models import Claim
from apps.LostFound.models import LostFound
from django.http import JsonResponse
from django.http import FileResponse
from apps.BaseView import ImageFormatException
from django.conf import settings
import pandas as pd
import os


class FrontAddView(BaseView):  # 前台认领添加
    def get(self,request):
        lostFounds = LostFound.objects.all()  # 获取所有失物招领
        context = {
            'lostFounds': lostFounds,
        }

        # 使用模板
        return render(request, 'Claim/claim_frontAdd.html', context)

    def post(self, request):
        claim = Claim() # 新建一个认领对象然后获取参数
        claim.lostFoundObj = LostFound.objects.get(lostFoundId=request.POST.get('claim.lostFoundObj.lostFoundId'))
        claim.personName = request.POST.get('claim.personName')
        claim.claimTime = request.POST.get('claim.claimTime')
        claim.contents = request.POST.get('claim.contents')
        claim.addTime = request.POST.get('claim.addTime')
        claim.save() # 保存认领信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class FrontModifyView(BaseView):  # 前台修改认领
    def get(self, request, claimId):
        context = {'claimId': claimId}
        return render(request, 'Claim/claim_frontModify.html', context)


class FrontListView(BaseView):  # 前台认领查询列表
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        self.getCurrentPage(request)  # 获取当前要显示第几页
        # 下面获取查询参数
        lostFoundObj_lostFoundId = self.getIntParam(request, 'lostFoundObj.lostFoundId')
        personName = self.getStrParam(request, 'personName')
        claimTime = self.getStrParam(request, 'claimTime')
        # 然后条件组合查询过滤
        claims = Claim.objects.all()
        if lostFoundObj_lostFoundId != '0':
            claims = claims.filter(lostFoundObj=lostFoundObj_lostFoundId)
        if personName != '':
            claims = claims.filter(personName__contains=personName)
        if claimTime != '':
            claims = claims.filter(claimTime__contains=claimTime)
        # 对查询结果利用Paginator进行分页
        self.paginator = Paginator(claims, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        claims_page = self.paginator.page(self.currentPage)

        # 获取所有失物招领
        lostFounds = LostFound.objects.all()
        # 构造模板需要的参数
        context = {
            'lostFounds': lostFounds,
            'claims_page': claims_page,
            'lostFoundObj_lostFoundId': int(lostFoundObj_lostFoundId),
            'personName': personName,
            'claimTime': claimTime,
            'currentPage': self.currentPage,
            'totalPage': self.totalPage,
            'recordNumber': self.recordNumber,
            'startIndex': self.startIndex,
            'pageList': self.pageList,
        }
        # 渲染模板界面
        return render(request, 'Claim/claim_frontquery_result.html', context)


class FrontShowView(View):  # 前台显示认领详情页
    def get(self, request, claimId):
        # 查询需要显示的认领对象
        claim = Claim.objects.get(claimId=claimId)
        context = {
            'claim': claim
        }
        # 渲染模板显示
        return render(request, 'Claim/claim_frontshow.html', context)


class ListAllView(View): # 前台查询所有认领
    def get(self,request):
        claims = Claim.objects.all()
        claimList = []
        for claim in claims:
            claimObj = {
                'claimId': claim.claimId,
            }
            claimList.append(claimObj)
        return JsonResponse(claimList, safe=False)


class UpdateView(BaseView):  # Ajax方式认领更新
    def get(self, request, claimId):
        # GET方式请求查询认领对象并返回认领json格式
        claim = Claim.objects.get(claimId=claimId)
        return JsonResponse(claim.getJsonObj())

    def post(self, request, claimId):
        # POST方式提交认领修改信息更新到数据库
        claim = Claim.objects.get(claimId=claimId)
        claim.lostFoundObj = LostFound.objects.get(lostFoundId=request.POST.get('claim.lostFoundObj.lostFoundId'))
        claim.personName = request.POST.get('claim.personName')
        claim.claimTime = request.POST.get('claim.claimTime')
        claim.contents = request.POST.get('claim.contents')
        claim.addTime = request.POST.get('claim.addTime')
        claim.save()
        return JsonResponse({'success': True, 'message': '保存成功'})

class AddView(BaseView):  # 后台认领添加
    def get(self,request):
        lostFounds = LostFound.objects.all()  # 获取所有失物招领
        context = {
            'lostFounds': lostFounds,
        }

        # 渲染显示模板界面
        return render(request, 'Claim/claim_add.html', context)

    def post(self, request):
        # POST方式处理图书添加业务
        claim = Claim() # 新建一个认领对象然后获取参数
        claim.lostFoundObj = LostFound.objects.get(lostFoundId=request.POST.get('claim.lostFoundObj.lostFoundId'))
        claim.personName = request.POST.get('claim.personName')
        claim.claimTime = request.POST.get('claim.claimTime')
        claim.contents = request.POST.get('claim.contents')
        claim.addTime = request.POST.get('claim.addTime')
        claim.save() # 保存认领信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class BackModifyView(BaseView):  # 后台更新认领
    def get(self, request, claimId):
        context = {'claimId': claimId}
        return render(request, 'Claim/claim_modify.html', context)


class ListView(BaseView):  # 后台认领列表
    def get(self, request):
        # 使用模板
        return render(request, 'Claim/claim_query_result.html')

    def post(self, request):
        # 获取当前要显示第几页和每页几条数据
        self.getPageAndSize(request)
        # 收集查询参数
        lostFoundObj_lostFoundId = self.getIntParam(request, 'lostFoundObj.lostFoundId')
        personName = self.getStrParam(request, 'personName')
        claimTime = self.getStrParam(request, 'claimTime')
        # 然后条件组合查询过滤
        claims = Claim.objects.all()
        if lostFoundObj_lostFoundId != '0':
            claims = claims.filter(lostFoundObj=lostFoundObj_lostFoundId)
        if personName != '':
            claims = claims.filter(personName__contains=personName)
        if claimTime != '':
            claims = claims.filter(claimTime__contains=claimTime)
        # 利用Paginator对查询结果集分页
        self.paginator = Paginator(claims, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        claims_page = self.paginator.page(self.currentPage)
        # 查询的结果集转换为列表
        claimList = []
        for claim in claims_page:
            claim = claim.getJsonObj()
            claimList.append(claim)
        # 构造模板页面需要的参数
        claim_res = {
            'rows': claimList,
            'total': self.recordNumber,
        }
        # 渲染模板页面显示
        return JsonResponse(claim_res, json_dumps_params={'ensure_ascii':False})

class DeletesView(BaseView):  # 删除认领信息
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        claimIds = self.getStrParam(request, 'claimIds')
        claimIds = claimIds.split(',')
        count = 0
        try:
            for claimId in claimIds:
                Claim.objects.get(claimId=claimId).delete()
                count = count + 1
            message = '%s条记录删除成功！' % count
            success = True
        except Exception as e:
            message = '数据库外键约束删除失败！'
            success = False
        return JsonResponse({'success': success, 'message': message})


class OutToExcelView(BaseView):  # 导出认领信息到excel并下载
    def get(self, request):
        # 收集查询参数
        lostFoundObj_lostFoundId = self.getIntParam(request, 'lostFoundObj.lostFoundId')
        personName = self.getStrParam(request, 'personName')
        claimTime = self.getStrParam(request, 'claimTime')
        # 然后条件组合查询过滤
        claims = Claim.objects.all()
        if lostFoundObj_lostFoundId != '0':
            claims = claims.filter(lostFoundObj=lostFoundObj_lostFoundId)
        if personName != '':
            claims = claims.filter(personName__contains=personName)
        if claimTime != '':
            claims = claims.filter(claimTime__contains=claimTime)
        #将查询结果集转换成列表
        claimList = []
        for claim in claims:
            claim = claim.getJsonObj()
            claimList.append(claim)
        # 利用pandas实现数据的导出功能
        pf = pd.DataFrame(claimList)
        # 设置要导入到excel的列
        columns_map = {
            'claimId': '认领id',
            'lostFoundObj': '招领信息',
            'personName': '认领人',
            'claimTime': '认领时间',
            'addTime': '发布时间',
        }
        pf = pf[columns_map.keys()]
        pf.rename(columns=columns_map, inplace=True)
        # 将空的单元格替换为空字符
        pf.fillna('', inplace=True)
        #设定文件名和导出路径
        filename = 'claims.xlsx'
        # 这个路径可以在settings中设置也可以直接手动输入
        root_path = settings.MEDIA_ROOT + '/output/'
        file_path = os.path.join(root_path, filename)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        # 将生成的excel文件输出到网页下载
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="claims.xlsx"'
        return response

