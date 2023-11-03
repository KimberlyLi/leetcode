# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        def helper(node):
            if node is None:
                result.append('x')
                return
            result.append(str(node.val))
            helper(node.left)
            helper(node.right)

        result = []
        helper(root)
        return ','.join(result)

    def deserialize(self, data):
        def helper():
            # retrieve next value in iterator
            val = next(data_iter)
            if val == 'x':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node

        # Initialize iterator in comma seperated string
        data_iter = iter(data.split(','))
        return helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))