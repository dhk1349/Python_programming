# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 03:31:43 2020

@author: dhk1349
"""

import cx_Oracle

#한글 지원 방법
import os
os.putenv('NLS_LANG', '.UTF8')

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
connection = cx_Oracle.connect('admin','ehdgns4232','lolgg.culykwl5fmgv.ap-northeast-2.rds.amazonaws.com/orcl')

cursor = connection.cursor()

cursor.execute("""
   select *
   from emp""",
)

for name in cursor:
   print("테스트 이름 리스트 : ", name)