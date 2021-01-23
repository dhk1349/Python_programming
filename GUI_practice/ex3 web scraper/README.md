----

참고

qlistview를 통해서 여러 항목을 출력(보관)할 컨테이너를 만들 수 있다. 

self.imagelist는 designer에서 미리 초기화한 qlistview 객체임.

갯수가 많아서 창의 범위를 벗어나면 저절로 스크롤이 생김



예제코드

sample=['apple', 'pen','pineapple']
        model=QStandardItemModel()
        for k in range(10):
            for s in sample:
                model.appendRow(QStandardItem(s))
        self.imagelist.setModel(model)

----

주의해야할 점

onclick함수를 사용하는 객체와 클릭 시 트리거 되는 함수의 이름이 같으면 에러가 나니까 까먹지 말 것

ex) self.search.clicked.connect(self.search) :arrow_right: 에러

ex) self.search.clicked.connect(self._search) :arrow_right: 에러:x:



