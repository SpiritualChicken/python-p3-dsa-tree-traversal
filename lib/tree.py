class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    if self.root is None:
      return None
    return self.depth_first_traversal(self.root, id)
     

  def depth_first_traversal(self, node, target_id):
        # Visit each node
        if node['id'] == target_id:
            return node
        for child in node['children']:
            # Visit each child node
            result = self.depth_first_traversal(child, target_id)
            if result:
                return result
        return None
