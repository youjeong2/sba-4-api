'''
n : bool fn
n + afn = pn
n + afn 
nn = bool + act
ann = bool + act + cost
dnn = ann + ann + ....

cnn = dnn + convolution => image 
rnn = dnn + recurrent  => order => context => nlp
lstm = rnn + time => sequential => prediction

best practice

플라스크 개발환경

template 을 리턴 -> legacy 방식
json 을 리턴 -> restful 방식 -> API 서버


wsgi 방식으로 전환
1. RESTful 로 전환
2. setup.py 생성, setuptools 를 활용한 설정
3. root - folder 생성 
   - package : __init__.py (O)
   - directory : __init__.py (X)



rnn
lstm

앞의 결과가 뒤의 결과에 영향을 준다.
-> 조건부 확률 (베이지안)
'''

'''
어플리케이션이 SQLAlchemy ORM을 사용한다면, 
객체에 바인딩된 쿼리를 위해서 Session 객체를 사용해야 한다. 
이는 session.add(), session.rollback(), session.commit(), session.close()를 통해 
트랜잭션을 단일 작업 단위로 관리하기 좋고, 
이러한 특징을 통해 Python의 Context Manager 패턴을 사용하기에도 좋다.
'''