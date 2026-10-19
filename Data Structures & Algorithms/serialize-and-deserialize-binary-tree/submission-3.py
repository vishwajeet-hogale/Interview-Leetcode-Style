class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def preorder(root):
            if root is None:
                res.append('N')
                return

            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
            return

        preorder(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        i = 0
        n = len(nodes)
        def build(node):
            nonlocal i
            if i >= n:
                return None

            if node == 'N':
                return None

            root = TreeNode(int(node))
            i += 1
            root.left = build(nodes[i])
            i += 1
            root.right = build(nodes[i])
            return root
        
        return build(nodes[0])