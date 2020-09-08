from django.test import TestCase
from django.test import Client
from .models import Message

# Create your tests here.


class MessageTest(TestCase):
    """信息反馈平台测试用例类
    单元测试在运行过程中会创建一个虚拟数据库
    """
    def setUp(self) -> None:
        """初始化数据
        tip：所有的模型的数据操作均在虚拟db中完成
        """
        Message.objects.create(name='Lucy', content='死灰复燃')
        Message.objects.create(name='May', content='生生不息')

    def test_Message(self):
        """测试Message模型
        """
        info = Message.objects.get(name='Lucy')
        self.assertIsNotNone(info.timestamp)  # 测试查询数据准确性

    def test_post(self):
        """测试post请求保存数据
        """
        c = Client()
        data = {
            'name': 'Tim',
            'content': '删库到跑路'
        }
        res = c.post('/', data=data)
        status_code = res.status_code
        info = Message.objects.get(name='Tim')
        self.assertEqual(status_code, 302)  # 测试状态码302，表明完成post操作
        self.assertEqual(info.content, '删库到跑路')  # 测试新增数据准确性
