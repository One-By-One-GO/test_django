# Django实现会议室管理系统项目

### 目前实现的主要功能:

1、用户能查询所有的会议室（包括已预订的、空闲的），并能进行预订，取消预订，预订会议室时间为一天，即该会议室被某个用户预定后，当天不能再被其他用户预订，会议室预订只能预订当天或者当天以后的，昨天及以前的会议室不能被预订
2、用户能创建会议室， 删除会议室，修改会议室名称，需要记录创建者名称，创建时间、修改时间、修改者名称

### 相应的API接口:

#### 第一个功能的接口:

```
url: http://127.0.0.1:8000/app1/meeting/
```

##### POST参数:

```
用户ID:		userid(int):              必填(目前需要自己传userid)
会议室名称:	  meetingname(varchar):     必填
```

##### PUT参数(body raw):

```
用户ID:          userid(int):                 必填
旧会议室名称:     createmeetingname(varchar):  必填
新会议室名称:     updatemeetingname(varchar):  必填
```

##### DELETE参数(body raw):

```
用户ID:           userid(int):                 必填
会议室名称:	      meetingname(varchar):        必填
是否删除(是1/否0): isdelete(int):               选填(默认1) 
```

##### 返回状态码:

```
status             msg
0                  正常
1                  会议室已存在
2                  会议室名称不能为空
3                  该会议室不存在
```

#### 第二个功能的接口:

##### GET参数:

```
会议室名称:         meetingname(varchar)        必填
预定日期:           date(datetime)              必填
```

##### POST参数:

```
用户ID:            userid(int):                 必填
会议室名称:         meetingname(varchar)         必填
预定日期:           date(datetime)               必填
```

##### 返回状态码:

```
status             msg
0                  预订成功
0                  已被预订
5                  请选择正确的时间
```

