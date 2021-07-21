class Order:
    def __init__(self, price, size, order_id):
        self.price = price
        self.size = size
        self.order_id = order_id

class Level:
    def __init__(self, price, orderlist = []):
        self.price = price
        self.orderlist = order_list
        self.size = sum(order.size for order in order_list)
    
    def add_order(self,order):
        self.order_list.append(order)
        self.size += order.size
    
    def cancel_order(self,order,size):
        if size == order.size:
            self.order_list.remove(order)
            self.size -= order.size
        else:
            assert(size < order.size)
            order.size -= size
class Ordertree:
    def __init__(self,isbid,depth):
        self.price_map = SortedDict()
        self.price = self.price_map.keys()
        self.order_map = {}
#         self.volume  = 0
#         self.num_orders = 0
        self.depth = depth
        self.isbid = isbid
    
    def get_price_list(self,price):
        return self.price_map[price]
    
    def get_order(self,order_id):
        return self.order_map[order_id]

    def create_level(self,price):
        new_level = Level(price)
        self.price_map[price] = new_level
        while len(self.price_map) > self.depth:
            if isbid:
                self.price_map.popitem(0)
            else:
                self.price_map.popitem()
                
    def remove_price(self,price):
        def self.price_map[price]
    
    def insert_order(self,order_id,price,size):
        if order.price not in self.price_map:
            self.create_level(price)
        order = Order(price,size,order_id)
        self.price_map[order.price].add_order(order)
        self.order_map[order_id] = order
    
        
    def remove_order(self, order_id, size):
        order = self.order_map[order_id]
        level = self.price_map[order.price]
        level.cancel_order(order)
        del self.order_map[order_id]
        
    class Orderbook:
    def __init__(self,depth, feed):
        self.depth = depth
        self.ask = Ordertree(False, self.depth)
        self.bid = Ordertree(True, self.depth)
        self.feed = feed

    def process(self,mesg):
        if mesg['Ev'] == 'SYM':
            if mesg['Status'] == 'eHalted':
                print(f'{mesg['Sym']} market is still closed')
            elif mesg['Status'] == 'eAuction':
                print(f'{mesg['Sym']} begins auction')
            else:
                print(f'{mesg['Sym']} begins trading')
        elif mesg['Ev'] == 'eExchSpec_HwaBaoImbalanceUpdate':
            pass
        elif mesg['Ev'] == 'NewLevel':
            
     class Orderbook:
    def __init__(self):
        self.level_tree = bintrees.FastRBTree()
        self.price_map = {}
        self.order_map = {}
        self.received_orders = {}
        
    def receive(self,order_id,price ,size):
        self.received_orders[order_id] = order(price,size,order_id)
    
    def create_level(self,price):
        new_level = level(price)
        self.price_tree.insert(price, new_level)
        self.price_map[price] = new_level
    
    def remove_price(self,price):
        self.price_tree.remove(new_level)
        def self.price_map[price]
    
    def insert_order(self, price, size, order_id):
        if price not in self.price_map:
            self.create_leve(price)
        new_order = order(price, size, order_id)
        self.price_tree[price].append(new_order)
        
                
