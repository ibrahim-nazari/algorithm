

def same_bst(first_tree,second_tree):
    if len(first_tree) !=len(second_tree):
        return False
    if not first_tree and not second_tree:
        return True
    if first_tree[0] !=second_tree[0]:
        return False
    
    def  get_subtree(tree):
        root=tree[0]
        left=[num for num in tree[1:] if num < root]
        right=[num for num in tree[1:] if num >= root]
        return left,right

    left1,right1=get_subtree(first_tree)
    left2,right2=get_subtree(second_tree)

    return same_bst(left1,left2) and same_bst(right1,right2)





def main():
    t=int(input())
    for _ in range(t):
        first_tree=list(map(int,input().split(",")))
        second_tree=list(map(int,input().split(",")))
        print(same_bst(first_tree,second_tree))


if __name__ == "__main__":
    main()