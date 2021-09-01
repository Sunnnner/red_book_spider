# coding:utf-8
from openpyxl import Workbook

Counter = {'小米': 128, '平板': 66, '买': 30, '🤤': 18, '视频': 14, '真的': 14, '省流': 11, '华为': 9, '适配': 9, '笔': 8, '希望': 8, '想': 8, '恰饭': 8, '推荐': 7, '评论': 6, '建议': 6, '屏幕': 6, '画画': 6, '萌叔': 6, '挺': 6, '体验': 5, '送': 5, '手机': 5, '键盘': 5, '感觉': 5, '安卓': 5, '电脑': 5, '东西': 5, '钱': 5, '镜子': 5, '圣经': 4, '区': 4, '软件': 4, '苹果': 4, '选择': 4, '哔哩': 4, '选': 4, '粉丝': 4, '广告': 4, '太': 4, '哈哈哈': 4, '做': 4, '官方': 3, '不用': 3, '公司': 3, '羡慕': 3, '刷': 3, '系统': 3, '产品': 3, '绘画': 3, '拉': 3, '喜欢': 3, '办公': 3, '需求': 3, '学习': 3, '本来': 3, '昨天': 3, '生活': 3, '吃': 3, '😂': 3, '饭': 3, '笑': 3, '适合': 3, '米粉': 3, '数码': 3, '生产力': 3, '抽个': 2, '叔叔': 2, '不懂事': 2, '&#': 2, '手持': 2, '频繁': 2, '一台': 2, '搜索': 2, '三千': 2, '接': 2, '游戏': 2, '软广': 2, '摸鱼': 2, '不错': 2, '抢': 2, '这是': 2, '全': 2, '贴合': 2, '画笔': 2, '接触': 2, '时能': 2, '笔尖': 2, '画': 2, '物体': 2, '距离感': 2, '糟糕': 2, '咬咬牙': 2, '你好': 2, '色差': 2, '太好': 2, '真心': 2, '值得': 2, '购买': 2, '小伙伴': 2, '后台': 2, '投稿': 2, '数据': 2, '研究': 2, '整合': 2, '所得': 2, '感谢': 2, '独家': 2, '赞助': 2, '下期': 2, '故事': 2, '铁汁们': 2, '关注': 2, '真': 2, '用户': 2, '触控笔': 2, '铁子': 2, '看着': 2, '前来': 2, '报道': 2, '拥有': 2, '创造': 2, '记笔记': 2, '同学': 2, '幻想': 2, '买来': 2, '笔记': 2, '骂': 2, '综艺': 2, '网课': 2, '灰': 2, '父母': 2, '看个': 2, '就够': 2, '没用': 2, '持续': 2, '吃灰中': 2, '对系统': 2, '始终': 2, '用不惯': 2, '退': 2, '小型': 2, '看待': 2, '随身携带': 2, '占用': 2, '空间': 2, '常备': 2, '商务': 2, '轻': 2, '越来越': 2, '镜粉': 2, '心中': 2, '最酷': 2, '站': 2, '米': 2, '底下': 2, '笑醒': 2, '好几个': 2, '阵营': 2, '中': 2, '很香': 2, '无脑': 2, '回事': 1, '不来': 1, '大嘴巴': 1, '子': 1, '狗': 1, '官': 1, '再恰': 1, '下次': 1, '两台': 1, '找': 1, '特码': 1, '俺儿': 1, '送给': 1, '效果': 1, '收回': 1, '这辈子': 1, '后悔': 1, '好巧': 1, '上午': 1, '几十个': 1, '主是': 1, '两个': 1, '艾特': 1, '说好': 1, '一千': 1, '打开': 1, '淘宝': 1, '识趣': 1, '一点': 1, '对标': 1, '段时间': 1, '出事': 1, '这时候': 1, '勇': 1, '怎么回事': 1, '一部': 1, '这新': 1, '外观': 1, '有点像': 1, '抢到': 1, '保护套': 1, '优惠价': 1, '一眼': 1, '迎来': 1, '弟弟': 1, '设计': 1, '吵': 1, '不行': 1, '价格': 1, '一共': 1, '生态': 1, '强': 1, '阶段': 1, '买到': 1, '笔记本': 1, '不到': 1, '确认': 1, '做防': 1, '误触': 1, '手': 1, '悬空': 1, '书写': 1, '里': 1, '拉到': 1, '屎': 1, '高端': 1, '咋样': 1, '反正': 1, '红米': 1, '支持': 1, '蓝牙': 1, '取色': 1, '快捷键': 1, '简单': 1, '涂鸦': 1, '画个': 1, '速写': 1, '正儿八经': 1, '地用': 1, '最优': 1, '解': 1, '搭配': 1, '优': 1, '动漫': 1, '有钱': 1, '折磨': 1, '难受': 1, '传下去': 1, '十三': 1, '用以': 1, '卧槽': 1, '摔成': 1, '这货': 1, '沉迷': 1, '玩': 1, '女朋友': 1, '要会': 1, '聊天': 1, '牛': 1, '逼': 1, '撩': 1, '妹妹': 1, '有用': 1, '方法': 1, '点': 1, '赞': 1, '算了算': 1, '太少': 1, '优化': 1, '崩溃': 1, '特': 1, '千人': 1, '千面': 1, '商城': 1, '一遍': 1, '奇迹': 1, '假装': 1, '神奇': 1, '实体店': 1, '收到': 1, '推送': 1, '早就': 1, '经验': 1, '朋友': 1, '善于': 1, '穿': 1, '没事': 1, '灵感': 1, '有时候': 1, '还会': 1, '有萌叔': 1, '陪伴': 1, '蜜汁': 1, '操作': 1, '讨厌': 1, '风评': 1, '不太好': 1, '少': 1, '接接': 1, '花': 1, '牺牲': 1, '勇敢': 1, '掐': 1, '业绩': 1, '几年': 1, '前': 1, '黑': 1, '历史': 1, '脚趾': 1, '扣出': 1, '崭新': 1, '三室两厅': 1, '欢声笑语': 1, '下午': 1, '真有': 1, '算了': 1, '跑': 1, '炮儿': 1, '完': 1, '种草': 1, '打钱': 1, '估计': 1, '夸夸': 1, '前边': 1, '儿看': 1, '雨豪': 1, '介绍': 1, '朵花': 1, '哈哈哈哈': 1, '自带': 1, '喜感': 1, '尴尬': 1, '券': 1, '显色': 1, '学生': 1, '梦娜': 1, '小米饭': 1, '贼': 1, '开心': 1, '没货': 1, '可惜': 1, '啊啊啊': 1, '链接': 1, '路由器': 1, '翼': 1, '刀': 1, '终于': 1, '恰到': 1, '指': 1, '加': 1, '几百元': 1, '扬声器': 1, '骁龙': 1, '赶紧': 1, '锻炼身体': 1, '锻炼': 1, '忍耐': 1, '告诉您': 1, '黑屏': 1, '几秒钟': 1, '亮': 1, '客服': 1, '封套': 1, '活着': 1, '装': 1, '钢化': 1, '膜': 1, '裸机': 1, '回复': 1, '消息': 1, '售后': 1, '垃圾': 1, '买过': 1, '区主买': 1, '区主': 1, '小心': 1, '疯': 1, '改成': 1, '批斗': 1, '大会': 1, '逢米': 1, '必反': 1, '一群': 1, '疯子': 1, '可怕': 1, '娱乐': 1, '表现': 1, '那句话': 1, '九成': 1, '偏门': 1, '冷门': 1, '问': 1, '一名': 1, '弹幕': 1, '好多': 1, '狗狗': 1, '原罪': 1, '玉米': 1, '众所周知': 1, '五在': 1, '优点': 1, '专业': 1, '搞': 1, '总恰': 1, '恰烂饭': 1, '稳定': 1, '搞怕': 1, '买不到': 1, '生气': 1, '贵': 1, '猫猫': 1, '善良': 1, '天真': 1, '爱': 1, '雷军': 1, '信': 1, '顺便': 1, '它长': 1, '无异': 1, '入手': 1, '➕': 1, '配置': 1, '确实': 1, '烂': 1, '爱奇艺': 1, '倒': 1, '写字': 1, '勉勉强强': 1, '接受': 1, '成': 1, '工具': 1, '算了吧': 1, '说米板': 1, '延迟': 1, '秒杀': 1, '代笔': 1, '无语': 1, '肯定': 1, '米板': 1, '先': 1, '追上': 1, '方向': 1, '努力': 1, '捧': 1, '捧杀': 1, '荣耀': 1, '新出': 1}


wb = Workbook()
ws = wb.active

ws.append([
    "词语",
    "词频"
])

for i in Counter.keys():
    ws.append([i, Counter[i]])

wb.save(r"D:\red_book\red_book_51wom\red_book_8月\red_book_08_31\xiaomi平板5_08_31_B站.xlsx")