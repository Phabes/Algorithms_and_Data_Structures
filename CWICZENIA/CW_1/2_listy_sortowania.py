class Node():
    def __init__(self, val, next):
        self.val = val
        self.next = next


def to_list(p):
    arr = []
    while p is not None:
        arr.append(p.val)
        p = p.next
    print(arr)


def insert(l, val):
    p = l
    if p.next is None:
        p.next = Node(val, None)
        return p

    prev = p
    p = p.next
    while p is not None and p.val < val:
        prev = p
        p = p.next
    q = Node(val, prev.next)
    prev.next = q
    return l


def remove_max(first):
    curr = first.next
    prev = first
    curr_max = curr
    prev_max = prev
    while curr is not None:
        if curr.val > curr_max.val:
            curr_max = curr
            prev_max = prev
        prev, curr = curr, curr.next
    prev_max.next = curr_max.next
    return (first, curr_max.val)


def selection(first):
    new_list = None
    while first.next is not None:
        max_val = remove_max(first)[1]
        new_list = Node(max_val, new_list)
    new_list = Node("*", new_list)
    return new_list


def minMax(T):
    mini=maxi=T[0]
    for i in range(0,len(T)-1,2):
        if T[i]>T[i+1]:
            if maxi<T[i]:
                maxi=T[i]
            if mini>T[i+1]:
                mini=T[i+1]
        else:
            if maxi<T[i+1]:
                maxi=T[i+1]
            if mini>T[i]:
                mini=T[i]
    return mini,maxi


def reverse(first):
    new_list = None
    curr = first.next
    while curr is not None:
        new_list = Node(curr.val, new_list)
        curr = curr.next
    return Node("*", new_list)


# p = Node("*", Node(5, Node(2, Node(10, Node(3, None)))))
p = Node("*", Node(5,Node(2,Node(8,Node(10,Node(3,None))))))
to_list(p)
# p = insert(p, 4)
# p = insert(p, 2)
# p = insert(p, 3)
# p = insert(p, 6)
to_list(reverse(p))


def rev_without(first):
    p=first
    count=0
    while p is not None:
        count+=1
        p=p.next
    p=first
    curr=0
    while p is not None:
        q=first
        now=count-curr-1
        curr2=0
        while curr2<now:
            curr2+=1
            q=q.next
        if curr<=curr2:
            p.val,q.val=q.val,p.val
        curr+=1
        p=p.next

# rev_without(p)
# to_list(p)

p = Node("*", Node(5,Node(2,Node(8,Node(10,Node(3,None))))))
to_list(p)
# p = Node("*", Node(5, Node(2, Node(10, Node(3, None)))))


def rev_with(first):
    p=first
    count=0
    while p is not None:
        count+=1
        p=p.next
    p=first.next
    curr=1
    while p is not None:
        q=first.next
        now=count-curr-1
        curr2=0
        while curr2<now:
            curr2+=1
            q=q.next
        if curr<=curr2:
            p.val,q.val=q.val,p.val
        curr+=1
        p=p.next

# rev_with(p)
# to_list(p)