class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mpathSum = -float('inf')
        def recurse(root):
            nonlocal mpathSum
            if root is None:
                return 0

            lnode = max(0, recurse(root.left))
            rnode = max(0, recurse(root.right))

            s = root.val + lnode + rnode
            mpathSum = max(s, mpathSum)
            return root.val + max(lnode, rnode)

        recurse(root)
        return mpathSum