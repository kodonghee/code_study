class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data   # 노드가 저장하는 데이터
        self.next = None   # 다음 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:   # 링크드 리스트가 비어 있는 경우
            self.head = new_node
            self.tail = new_node
        else:   # 링크드 리스트가 비어 있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node


# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

# 링크드 리스트 출력
iterator = my_list.head

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next