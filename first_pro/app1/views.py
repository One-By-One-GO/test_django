from django.views import View
from django.shortcuts import HttpResponse
from app1 import models
from datetime import datetime
from dateutil.parser import parse
import json, time


class CreateMeeting(View):

    def post(self, request):
        data = {'status': 0, 'msg': '正常'}
        userid = request.POST.get('userid')
        meeting_name = request.POST.get('meetingname')
        if not meeting_name:
            data = {'status': 3, 'msg': '会议室名称不能为空'}
            json_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(json_data)
        meetingname = models.Meeting.objects.filter(meeting_name=meeting_name, is_delete=0).first()
        if not meetingname:
            models.Meeting.objects.create(meeting_name=meeting_name, create_userid=userid, update_userid=userid)
            json_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(json_data)
        data = {'status': 2, 'msg': '会议室已存在'}
        json_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_data)

    def put(self, request):
        data = {'status': 0, 'msg': '正常'}
        body = json.loads(request.body)
        userid = body.get('userid')
        create_meeting_name = body.get('createmeetingname')
        update_meeting_name = body.get('updatemeetingname')
        if not update_meeting_name:
            data = {'status': 3, 'msg': '会议室名称不能为空'}
            json_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(json_data)
        meetingname = models.Meeting.objects.filter(meeting_name=create_meeting_name, is_delete=0).first()
        if meetingname:
            models.Meeting.objects.filter(meeting_name=create_meeting_name, is_delete=0).\
                update(meeting_name=update_meeting_name, update_userid=userid)
            json_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(json_data)
        data = {'status': 4, 'msg': '该会议室不存在'}
        json_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_data)

    def delete(self, request):
        data = {'status': 0, 'msg': '正常'}
        body = json.loads(request.body)
        userid = body.get('userid')
        meeting_name = body.get('meetingname')
        is_delete = body.get('isdelete') or 1
        if not meeting_name:
            data = {'status': 3, 'msg': '会议室名称不能为空'}
            json_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(json_data)
        meetingname = models.Meeting.objects.filter(meeting_name=meeting_name, is_delete=0).first()
        if meetingname:
            models.Meeting.objects.filter(meeting_name=meeting_name, is_delete=0).\
                update(update_userid=userid, is_delete=is_delete)
            json_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(json_data)
        data = {'status': 4, 'msg': '该会议室不存在'}
        json_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_data)


class SelectMeeting(View):
    def get(self, request):
        data = {'status': 0, 'msg': '未预定'}
        meeting_name = request.GET.get('meetingname')
        date = request.GET.get('date')
        result = models.Reserve.objects.filter(meeting_id__meeting_name=meeting_name, reserve_time=date).first()
        if not result:
            data = {'status': 0, 'msg': '已预定'}
        json_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_data)

    def post(self, request):
        now = datetime.now()
        data = {'status': 0, 'msg': '预订成功'}
        meeting_name = request.POST.get('meetingname')
        userid = request.POST.get('userid')
        date = request.POST.get('date')
        if time.mktime(parse(date).timetuple()) < time.mktime(now.timetuple()):
            data = {'status': 5, 'msg': '请选择正确的时间'}
            json_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(json_data)
        result = models.Reserve.objects.filter(meeting_id__meeting_name=meeting_name, reserve_time=date).first()
        if not result:
            meeting_name = models.Meeting.objects.filter(meeting_name=meeting_name, is_delete=0).first()
            models.Reserve.objects.create(meeting_id=meeting_name.id, reserve_userid=userid, reserve_time=date)
            json_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(json_data)
        data = {'status': 4, 'msg': '已被预订'}
        json_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_data)


