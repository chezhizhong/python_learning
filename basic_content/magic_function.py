

class Cat:
    """
    这是一只猫的类
    """
    class_name = 'class name'

    def __init__(self, name):
        self.name = name
        self.__private_name = name
        print('我是一只猫，我叫%s' % self.name)

    def __del__(self):
        print('我被系统回收了')

    def __call__(self, *args, **kwargs):
        print(args[0] + args[1])

    def __str__(self):
        return '我是%s' % self.name

    def __len__(self):
        return 12

    def __iter__(self):
        return iter([1, 2, 3, 4])

    def __getitem__(self, item):
        if item == 'name':
            return self.name
        else:
            return None

    def __setitem__(self, key, value):
        if key == 'name':
            self.name = value

    def __delitem__(self, key):
        if key == 'name':
            del self.name

    def __add__(self, other):
        if isinstance(other, Cat):
            return [self, other]
        elif isinstance(other, list):
            other.append(self)
            return other

    def __sub__(self, other):
        return '减法'

    def __mul__(self, other):
        return '乘法'


def main():
    cat_obj = Cat('cristy')
    # print(cat_obj)
    # del cat_obj
    # print(cat_obj)
    print(cat_obj.__doc__)
    print(cat_obj.__module__)
    print(cat_obj.__class__)
    cat_obj(1, 2)
    print(callable(cat_obj))
    print(cat_obj.__dict__)  # 以字典的形式展示成员属性（不包括类属性）
    print(cat_obj.class_name)
    print(cat_obj)
    print(len(cat_obj))
    print([i for i in cat_obj])
    print(cat_obj['name'])
    cat_obj['name'] = 'sniper'
    print(cat_obj['name'])
    # del cat_obj['name']
    # print(cat_obj['name'])


if __name__ == '__main__':
    main()
