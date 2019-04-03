import logging

logger = logging.getLogger(__name__)

class Order(object):
   
   def __init__(self, order_id, reordered):
        self.order_id = order_id
        self.reordered = self._validate_reorder(reordered)

   def _validate_reorder(self, reorder):
      if isinstance(reorder, bool):
         return reorder
      elif isinstance(reorder, str):
         try:
            reorder = (reorder == "1")
            return reorder
         except:
            logger.error("Re-order variable is not of type Boolean")
      else:
         logger.error("Reorder variable is not of type Boolean")
         return None
    
