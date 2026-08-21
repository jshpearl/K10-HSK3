# -*- coding: utf-8 -*-
import streamlit as st
import requests
import json
from datetime import datetime

# ==============================================================================
# HSK4 LUYỆN NGHE PHẦN 2 (2) - STREAMLIT APP
# ==============================================================================

# CẤU HÌNH TRANG WEB
st.set_page_config(
    page_title="HSK4 LUYỆN NGHE PHẦN 2 (2)",
    page_icon="🎧",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CẤU HÌNH LIÊN KẾT WEBHOOK ĐỂ LƯU ĐIỂM VỀ GOOGLE SHEETS
# Bạn hãy thay thế đường dẫn này bằng link Web App URL lấy từ Google Apps Script
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbxfZ7f292zc7Rcq8OdalCQIKl9WDY1fAc21pBMAmXFKr1qnQ3F8FeH-vJqIebuWKQ1U8A/exec"

# PHONG CÁCH GIAO DIỆN (UI/UX CHẤT LƯỢNG CAO, ĐỘ TƯƠNG PHẢN ĐẬM CỰC RÕ)
st.markdown("""
    <style>
    /* Tổng quan trang */
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }
    
    /* Ép tất cả các văn bản thông thường, chữ đáp án, chữ radio button hiển thị màu đen đậm */
    .stApp, .stMarkdown, p, div, span, label, .stRadio label, .stRadio div {
        color: #0f172a !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }
    
    /* Thiết kế tiêu đề chính màu xanh navy sang trọng */
    .header-box {
        text-align: center;
        padding: 24px;
        background-color: #ffffff;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        margin-bottom: 25px;
        border: 2px solid #cbd5e1;
    }
    .header-box h1 {
        color: #1e3b8a !important;
        font-size: 32px !important;
        font-weight: 800 !important;
        margin-bottom: 8px;
    }
    .header-box p {
        font-size: 16px !important;
        color: #475569 !important;
        font-weight: 600 !important;
    }
    
    /* Khung nhập tên màu trắng viền xanh nổi bật */
    .info-box {
        background-color: #ffffff !important;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px;
        border: 3px solid #1e3b8a !important;
    }
    .info-box label {
        color: #1e3b8a !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }
    
    /* Trình phát nhạc chất lượng cao, độ tương phản rõ rệt */
    .audio-wrapper {
        background: #f0f6ff !important;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
        border-left: 6px solid #1e3b8a !important;
        border-right: 1.5px solid #cbd5e1 !important;
        border-top: 1.5px solid #cbd5e1 !important;
        border-bottom: 1.5px solid #cbd5e1 !important;
    }
    .audio-wrapper h3 {
        font-size: 16px !important;
        font-weight: 700 !important;
        color: #1e3b8a !important;
    }
    .audio-wrapper p {
        font-size: 14px !important;
        color: #334155 !important;
        line-height: 1.4 !important;
    }
    
    /* Thẻ câu hỏi viền đậm cực kỳ dễ đọc */
    .question-card {
        background-color: #ffffff !important;
        border: 2.5px solid #94a3b8 !important; /* Viền xám tối rõ ràng */
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.04);
    }
    
    /* Huy hiệu câu số màu xanh navy đậm */
    .q-badge {
        background-color: #1e3b8a !important;
        color: #ffffff !important;
        padding: 4px 12px !important;
        font-size: 14px !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        display: inline-block;
        margin-bottom: 12px;
        box-shadow: 0 2px 4px rgba(30, 58, 138, 0.2);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 25px;
        color: #334155 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        border-top: 2px solid #cbd5e1;
    }
    </style>
""", unsafe_allow_html=True)

# TẠO GIAO DIỆN HEADER
st.markdown("""
    <div class="header-box">
        <h1>HSK4 LUYỆN NGHE PHẦN 2 (2)</h1>
        <p>根据听力内容选择正确答案</p>
    </div>
""", unsafe_allow_html=True)

# NHẬP HỌ TÊN HỌC VIÊN
st.markdown('<div class="info-box">', unsafe_allow_html=True)
student_name = st.text_input("👤 输入您的姓名 / Nhập họ và tên học viên:", key="student_name", placeholder="请输入姓名...")
st.markdown('</div>', unsafe_allow_html=True)

# DỮ LIỆU ĐỀ THI
exam_data = {
    "DE_16": {
        "title": "Bộ Đề 16",
        "audio_id": "1xUQ9THMhYgIkl9TIM0vLMMGdfpIuZYwg",
        "questions": [
            {
                "num": 11,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 借钱",
                    "B. 卖饼干",
                    "C. 找钥匙",
                    "D. 打印文章"
                ],
                "correct": "A",
                "script": "男：我带的钱不够，你能不能先借我一点儿，我明天还你。\n女：没问题。高老师，您要多少？\n问：男的在做什么？"
            },
            {
                "num": 12,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 汤",
                    "B. 咖啡",
                    "C. 葡萄酒",
                    "D. 牛奶糖"
                ],
                "correct": "A",
                "script": "女：这个鸡蛋汤味道怎么样？你尝一下？\n男：我尝了，稍微有点儿咸，是盐放多了吧？\n问：他们在谈什么？"
            },
            {
                "num": 13,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 游泳",
                    "B. 画画儿",
                    "C. 上钢琴课",
                    "D. 打羽毛球"
                ],
                "correct": "C",
                "script": "男：不想去上钢琴课了。\n女：为什么？你不是很喜欢弹钢琴吗？而且还弹得那么好。\n问：男的不想做什么？"
            },
            {
                "num": 14,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 出差",
                    "B. 爬长城",
                    "C. 去医院",
                    "D. 照顾奶奶"
                ],
                "correct": "C",
                "script": "女：经理，打扰您一下，我明天要去趟医院，我想请一天假可以吗？\n男：当然可以，怎么了？身体不舒服？\n问：女的请假要做什么？"
            },
            {
                "num": 15,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 最近很忙",
                    "B. 可以教他",
                    "C. 会打网球",
                    "D. 动作不标准"
                ],
                "correct": "B",
                "script": "男：你乒乓球打得真不错，有时间能教教我吗？\n女：没问题。我每周六都会来体育馆，到时候你来找我就行了。\n问：女的是什么意思？"
            },
            {
                "num": 16,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 寄信",
                    "B. 别迟到",
                    "C. 要仔细",
                    "D. 写总结"
                ],
                "correct": "B",
                "script": "女：明天早上八点半在东门集合，别迟到啊！\n男：放心吧，我一定准时到。\n问：女提醒男的是什么？"
            },
            {
                "num": 17,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 再加一列",
                    "B. 再算一遍",
                    "C. 减少字数",
                    "D. 继续申请"
                ],
                "correct": "A",
                "script": "男：孙小姐，表格我做好了，您看看有什么问题没。\n女：刚才和你说了，还要再加上一列“性别”。\n问：女的要求怎么做？"
            },
            {
                "num": 18,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 口渴",
                    "B. 坐地铁去",
                    "C. 放暑假了",
                    "D. 会踢足球"
                ],
                "correct": "B",
                "script": "男：从这儿到国家图书馆远吗？咱们怎么走？\n女：坐公交车大概得一个多小时，这会儿肯定堵车，我们还是坐地铁吧。\n问：女的是什么意思？"
            },
            {
                "num": 19,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 生气了",
                    "B. 出汗了",
                    "C. 没上班",
                    "D. 没带钥匙"
                ],
                "correct": "D",
                "script": "男：妈，你下班了吗？我没带钥匙。\n女：我很快就到家了，你先在门口等会儿吧。\n问：男怎么了？"
            },
            {
                "num": 20,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 很厚",
                    "B. 弄坏了",
                    "C. 收词多",
                    "D. 能听广播"
                ],
                "correct": "C",
                "script": "女：这两个电子词典样子差不多，左边这个怎么这么贵？\n男：那是新出的，收的词语更丰富，另外，它还有语法解释，所以贵一些。\n问：关于左边的电子词典，下列哪个正确？"
            },
            {
                "num": 21,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 杂志",
                    "B. 成绩单",
                    "C. 报名表",
                    "D. 记事本"
                ],
                "correct": "B",
                "script": "男：喂，姐，我找到你的成绩单了，给你寄过去吗？\n女：你还是发传真吧，我现在就要。\n问：男找到什么了？"
            },
            {
                "num": 22,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 没力气了",
                    "B. 方向不对",
                    "C. 完成任务了",
                    "D. 暂时去不了"
                ],
                "correct": "D",
                "script": "女：听说你寒假要去山西？\n男：是，我本来想放假就走，但恐怕得推迟了，老师让我翻译几篇文章。\n问：男的是什么意思？"
            },
            {
                "num": 23,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 很脏",
                    "B. 发烧了",
                    "C. 没精神",
                    "D. 肚子饿了"
                ],
                "correct": "C",
                "script": "男：小狗是不是生病了？怎么上去精神不太好。\n女：我猜可能是它刚换了新环境，还没有适应，熟悉了就好了。\n问：小狗怎么了？"
            },
            {
                "num": 24,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 还没举行",
                    "B. 非常热闹",
                    "C. 让人失望",
                    "D. 开得很顺利"
                ],
                "correct": "A",
                "script": "女：这次在上海举办的会议，还是你负责，我会再安排两个人帮助你。\n男：好的，经理。\n问：关于会议，可以知道什么？"
            },
            {
                "num": 25,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 吃饱了",
                    "B. 饺子不咸",
                    "C. 面包很硬",
                    "D. 菜不好吃"
                ],
                "correct": "B",
                "script": "男：今天的饺子盐放多了，有点儿咸。\n女：是吗？我觉得正好啊，一点儿也不咸。\n问：女的是什么意思？"
            }
        ]
    },
    "DE_17": {
        "title": "Bộ Đề 17",
        "audio_id": "1gFeLqmVTd70HSPnX4jyM5yPnDSEUrEeI",
        "questions": [
            {
                "num": 11,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 很香",
                    "B. 不甜",
                    "C. 太辣",
                    "D. 有点儿咸"
                ],
                "correct": "A",
                "script": "男：妈，你做的什么菜？好香啊！我尝尝。\n女：别用手拿，去拿筷子。\n问：男觉得菜怎么样？"
            },
            {
                "num": 12,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 想请假",
                    "B. 被表扬了",
                    "C. 受到邀请了",
                    "D. 要写计划书"
                ],
                "correct": "D",
                "script": "女：这次文化节活动由你负责，一定要办得热闹点儿。\n男：好，我们回去就会开会讨论，星期五之前把详细的计划书发给您。\n问：关于男，可以知道什么？"
            },
            {
                "num": 13,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 困了",
                    "B. 饿了",
                    "C. 生病了",
                    "D. 流泪了"
                ],
                "correct": "C",
                "script": "男：你现在感觉怎么样了？好像咳嗽没那么严重了。\n女：好多了，这种感冒药确实有用，头也不怎么疼了。\n问：女怎么了？"
            },
            {
                "num": 14,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 走路",
                    "B. 坐地铁",
                    "C. 骑自行车",
                    "D. 坐出租车"
                ],
                "correct": "B",
                "script": "女：快来不及了，我们打车过去吧？\n男：还是坐地铁吧，这会儿路上恐怕会堵车。\n问：男想怎么去那儿？"
            },
            {
                "num": 15,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 没吃饱",
                    "B. 要写日记",
                    "C. 在看电影",
                    "D. 在看小说"
                ],
                "correct": "D",
                "script": "男：已经两点了，你怎么还不睡觉。\n女：这本小说就剩十几页了，我想看看最后到底怎么样了。\n问：女为什么还不睡？"
            },
            {
                "num": 16,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 中午很冷",
                    "B. 空调坏了",
                    "C. 灯不亮了",
                    "D. 冰箱太旧了"
                ],
                "correct": "B",
                "script": "女：咱们办公室的空调是不是坏了？太热了。\n男：昨天就坏了，一直没人来修，我再打电话问问。\n问：柑橘对话，下列哪个正确？"
            },
            {
                "num": 17,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 800 元",
                    "B. 160 元",
                    "C. 640 元",
                    "D. 600 元"
                ],
                "correct": "C",
                "script": "女：这双鞋多少钱？\n男：原价 800 块钱，现在打八折。\n问：鞋子多少钱一双？"
            },
            {
                "num": 18,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 是他拿照相机",
                    "B. 很失望",
                    "C. 很后悔",
                    "D. 很激动"
                ],
                "correct": "B",
                "script": "女：真的是你拿了小王的照相机吗？\n男：连你也这样认为吗？\n问：根据这段话，可以知道男怎么了？"
            },
            {
                "num": 19,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 认真",
                    "B. 仔细",
                    "C. 马虎",
                    "D. 活泼"
                ],
                "correct": "C",
                "script": "男：你看看你，怎么又算错了，你总是这样，就不能认真点儿吗？\n女：对不起。\n问：根据对话，可以知道女怎么样？"
            },
            {
                "num": 20,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 不行",
                    "B. 可以帮忙照相",
                    "C. 照相机有问题",
                    "D. 照相机没有问题"
                ],
                "correct": "B",
                "script": "女：先生，你可以给我们照张相吗？\n男：没问题。\n问：男意思是什么？"
            },
            {
                "num": 21,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 去看电影",
                    "B. 去电影院",
                    "C. 去图书馆",
                    "D. 去教室"
                ],
                "correct": "C",
                "script": "男：你今晚和我一起去电影院看电影好吗？\n女：不行，有人在图书馆等我呢。\n问：女准备做什么？"
            },
            {
                "num": 22,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 坐地铁",
                    "B. 坐朋友的车",
                    "C. 坐公交车",
                    "D. 坐出租车"
                ],
                "correct": "B",
                "script": "男：我们明天怎么去公园，是坐公交还是地铁？\n女：我的一个朋友明天没事，说可以开车送我们去。\n问：他们怎么去公园？"
            },
            {
                "num": 23,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 男的发烧了",
                    "B. 小李出国了",
                    "C. 地址写错了",
                    "D. 手机修好了"
                ],
                "correct": "B",
                "script": "男：小李换号了吗？怎么手机总是打不通？\n女：他去国外出差了，月底才能回来，您有事儿就给他发电子邮件吧。\n问：根据对话，下列哪个正确？"
            },
            {
                "num": 24,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 还杂志",
                    "B. 买饮料",
                    "C. 别抽烟",
                    "D. 别迟到"
                ],
                "correct": "C",
                "script": "女：先生，我们这里禁止抽烟。\n男：啊，对不起，我没注意到，我这就到外面去。\n问：女提醒男的是什么？"
            },
            {
                "num": 25,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 同情男的",
                    "B. 比赛很有趣",
                    "C. 输赢不重要",
                    "D. 时间来得及"
                ],
                "correct": "C",
                "script": "男：只差一点儿就赢了，真替他感到可惜。\n女：他已经打出了自己最好的水平，无论结果怎么样，我们都应该为他高兴。\n问：女的是什么意思？"
            }
        ]
    },
    "DE_18": {
        "title": "Bộ Đề 18",
        "audio_id": "1oxh005THkJv34EkiugkVX-tfCz7bO_Iz",
        "questions": [
            {
                "num": 11,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 不好看",
                    "B. 有点儿贵",
                    "C. 要手洗",
                    "D. 只能干洗"
                ],
                "correct": "C",
                "script": "女：这件毛衣不错，挺适合你的。\n男：缺点就是不能放在洗衣机里洗，要是你愿意手洗我就买。\n问：这件毛衣怎么样？"
            },
            {
                "num": 12,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 能力不够",
                    "B. 没有耐心",
                    "C. 工作马虎",
                    "D. 不相信人"
                ],
                "correct": "B",
                "script": "男：小王这个人就是缺少耐心。\n女：其实他身上优点挺多的，工作认真，还很节约。\n问：小王有什么缺点？"
            },
            {
                "num": 13,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 头疼",
                    "B. 流泪",
                    "C. 咳嗽",
                    "D. 肚子疼"
                ],
                "correct": "C",
                "script": "男：你怎么咳嗽了？是不是感冒了？\n女：可能是因为我还没适应这里的空气吧。\n问：女怎么了？"
            },
            {
                "num": 14,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 酸的",
                    "B. 甜的",
                    "C. 辣的",
                    "D. 咸的"
                ],
                "correct": "A",
                "script": "男：这个酸菜鱼你怎么吃了一口就不吃了？\n女：我怕酸。没关系，别的菜不管甜的还是辣的我都可以吃。\n问：女不吃什么菜？"
            },
            {
                "num": 15,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 开会",
                    "B. 上课",
                    "C. 洗澡",
                    "D. 睡觉"
                ],
                "correct": "A",
                "script": "男：下午给你打了好几次电话，你怎么没接？\n女：不好意思，下午有一个很重要的会议，我不方便接。\n问：女下午在做什么？"
            },
            {
                "num": 16,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 借钱",
                    "B. 购物",
                    "C. 寄东西",
                    "D. 准备材料"
                ],
                "correct": "C",
                "script": "男：你这么忙，这个材料我去寄吧。\n女：那就麻烦你了，我先把钱给你吧。\n问：男想帮女做什么？"
            },
            {
                "num": 17,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 吃完了",
                    "B. 不吃辣",
                    "C. 吃多了",
                    "D. 有点儿贵"
                ],
                "correct": "C",
                "script": "男：你怎么不吃鱼？是不是怕辣？\n女：不是，我前几天老吃鱼，吃得有点儿多了，想多吃点儿菜。\n问：女为什么不吃鱼？"
            },
            {
                "num": 18,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 便宜",
                    "B. 好喝",
                    "C. 很近",
                    "D. 认识人"
                ],
                "correct": "B",
                "script": "女：那个咖啡馆的咖啡太贵了，你别去了。\n男：贵点儿没关系，味道好是最重要的。\n问：男为什么要去那个咖啡馆？"
            },
            {
                "num": 19,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 工作太忙了",
                    "B. 担心学不会",
                    "C. 家里没有琴",
                    "D. 怕影响邻居"
                ],
                "correct": "D",
                "script": "男：你钢琴弹得不错，怎么平时不弹呢？\n女：弹过几次，邻居说太吵了。我就不好意思弹了。\n问：女为什么不弹钢琴？"
            },
            {
                "num": 20,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 水平低",
                    "B. 太远了",
                    "C. 想轻松点儿",
                    "D. 来不及准备"
                ],
                "correct": "C",
                "script": "女：有人邀请你参加比赛，你为什么不接受呢？\n男：一准备比赛就又要紧张起来了，最近这段时间我想过过轻松的生活。\n问：男为什么不参加比赛？"
            },
            {
                "num": 21,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 不被信任",
                    "B. 工资太低",
                    "C. 研究生",
                    "D. 十分辛苦"
                ],
                "correct": "A",
                "script": "男：那家公司工资高，离开了多可惜啊！\n女：是有点儿可惜，可是经理总是不信任我，我觉得跟这样的人一起工作心情不愉快。\n问：女为什么离开公司？"
            },
            {
                "num": 22,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 很幽默",
                    "B. 唱得好",
                    "C. 有耐心",
                    "D. 样子好"
                ],
                "correct": "A",
                "script": "女：这个男演员一点儿也不帅，喜欢他的人却很多，真奇怪。\n男：一点儿也不奇怪，他虽然不帅，可是说话很幽滑，给大家带来了很多欢乐。\n, nhưng thực tế chuẩn phải là 幽默 )\n问：为什么人们喜欢这个演员？"
            },
            {
                "num": 23,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 离得近",
                    "B. 气氛好",
                    "C. 是一种运动",
                    "D. 上网不方便"
                ],
                "correct": "B",
                "script": "男：在网上买书多省事儿啊，去书店要多花好多时间。\n女：可是我喜欢书店的气氛，在书店里看看感兴趣的书，我的心情都特别愉快。\n问：女为什么去书店买书？"
            },
            {
                "num": 24,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 来早了",
                    "B. 有人了",
                    "C. 太贵了",
                    "D. 清楚了"
                ],
                "correct": "B",
                "script": "男：你好！请问这个座位有人吗？\n女：不好意思，坐这儿的人去卫生间了，一会儿还回来。\n问：女的是什么意思？"
            },
            {
                "num": 25,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 自己的很好",
                    "B. 不买这双鞋",
                    "C. 女的买多了",
                    "D. 不知道选什么"
                ],
                "correct": "B",
                "script": "女：看这双鞋，今年特别流行这样的。\n男：流行的不一定好，适合自己的才是最好的。我觉得你穿这样的不合适。\n问：男的是什么意思？"
            }
        ]
    },
    "DE_19": {
        "title": "Bộ Đề 19",
        "audio_id": "1nIsPcA239XEHI0BTFkk2RpW3zjLyY3nM",
        "questions": [
            {
                "num": 11,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 没说完",
                    "B. 没意思",
                    "C. 不会英语",
                    "D. 不用汉语"
                ],
                "correct": "D",
                "script": "男：这个词是什么意思？你能用汉语解释一下吗？\n女：恐怕我用汉语解释完以后，你更不明白了。我还是用英语说吧。\n问：女的是什么意思？"
            },
            {
                "num": 12,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 拒绝",
                    "B. 很好",
                    "C. 有信心",
                    "D. 考虑一下"
                ],
                "correct": "A",
                "script": "女：你和我一起翻译这本书，怎么样？\n男：翻译科学方面的书，要十分准确，我的水平还不够。\n问：男是什么意思？"
            },
            {
                "num": 13,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 鼓励儿子",
                    "B. 祝贺儿子",
                    "C. 批评儿子",
                    "D. 感谢儿子"
                ],
                "correct": "A",
                "script": "男：妈妈，我有点儿害怕，要是输了球怎么办？\n女：儿子，好好踢，妈妈相信你，你是个勇敢的人。\n问：根据对话，可以知道女在做什么？"
            },
            {
                "num": 14,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 无聊",
                    "B. 一般",
                    "C. 值得看",
                    "D. 看不懂"
                ],
                "correct": "C",
                "script": "女：你觉得这部电影怎么样？\n男：每个人看完以后都有自己的感觉。我只能告诉你，你要是不去电影院看肯定会后悔的。\n问：男觉得电影怎么样？"
            },
            {
                "num": 15,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 比赛",
                    "B. 看球",
                    "C. 说笑话",
                    "D. 打电脑"
                ],
                "correct": "B",
                "script": "男：这球打得真精彩！\n女：我都看了好几个小时了，也该让我看看我喜欢的节目了。\n问：男在干什么？"
            },
            {
                "num": 16,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 讨论问题",
                    "B. 买好礼物",
                    "C. 下班回家",
                    "D. 准备茶点"
                ],
                "correct": "D",
                "script": "女：后天九点开会，我八点五十到可以吗？\n男：最好提前半个小时到，我们还得提前准备好茶水、点心呢。\n问：他们要提前做什么？"
            },
            {
                "num": 17,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 想继续走",
                    "B. 他很健康",
                    "C. 他家很近",
                    "D. 有点儿累"
                ],
                "correct": "A",
                "script": "女：你看天突然这么黑，好像要下大雨了。我们别散步了，往回走吧。\n男：没关系，我带着伞呢。\n问：男主要是什么意思？"
            },
            {
                "num": 18,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 写书",
                    "B. 买东西",
                    "C. 看朋友",
                    "D. 打扫房子"
                ],
                "correct": "A",
                "script": "男：听说你打算买海边的房子？\n女：你是听谁说的？我只是想去海边住一两个月，把我的书写完，买房子干什么？\n问：女打算做什么？"
            },
            {
                "num": 19,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 都可以",
                    "B. 很不错",
                    "C. 不关心",
                    "D. 不合适"
                ],
                "correct": "D",
                "script": "女：我穿这条连衣裙怎么样？\n男：挺漂亮的，可是不够正式。\n问：男的是什么意思？"
            },
            {
                "num": 20,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 等人",
                    "B. 开车",
                    "C. 爬楼梯",
                    "D. 踢足球"
                ],
                "correct": "C",
                "script": "男：电梯怎么坏了？累死我了，休息一下再爬吧。\n女：已经爬了六层了，还有三层就到了。\n问：他们最可能在做什么？"
            },
            {
                "num": 21,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 产量少",
                    "B. 是进口的",
                    "C. 历史很长",
                    "D. 质量最好"
                ],
                "correct": "A",
                "script": "男：这个葡萄酒价格怎么这么高？\n女：因为产量很少。\n问：为什么这种酒很贵？"
            },
            {
                "num": 22,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 没人关心",
                    "B. 优秀的少",
                    "C. 组织很乱",
                    "D. 非常成功"
                ],
                "correct": "B",
                "script": "女：听说这次招聘报名的人不少啊！\n男：来的人确实挺多的，可是其中优秀的只有两三个，其他的基本上不合格。\n问：这次招聘，情况怎么样？"
            },
            {
                "num": 23,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 便宜",
                    "B. 安全",
                    "C. 服务好",
                    "D. 时间合适"
                ],
                "correct": "A",
                "script": "女：你为什么要买这个航空公司的机票？\n男：因为可以打七折。别的公司现在都是原价。\n问：男为什么买这个公司的机票？"
            },
            {
                "num": 24,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 打电话问",
                    "B. 少管点儿事",
                    "C. 写写东西",
                    "D. 用手机记事"
                ],
                "correct": "D",
                "script": "女：我最近老爱忘事，这是不是跟年龄有关系？\n男：那是因为你事儿太多了，又不用记事本。你可以把重要的事都写在手机里，这样就不会忘记了。\n问：男有什么意见？"
            },
            {
                "num": 25,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 看电影",
                    "B. 买礼物",
                    "C. 去饭馆吃",
                    "D. 在家请客"
                ],
                "correct": "D",
                "script": "男：明天是你的生日，我请你吃饭吧。\n女：明天我想请朋友来家里吃饭，我已经把菜都准备好了。\n问：女明天打算做什么？"
            }
        ]
    },
    "DE_20": {
        "title": "Bộ Đề 20",
        "audio_id": "19cUHi-Dsw4AcGrt-fiA5j9pFuAFxS-gV",
        "questions": [
            {
                "num": 11,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 考试",
                    "B. 打羽毛球",
                    "C. 去大使馆",
                    "D. 去朋友家"
                ],
                "correct": "C",
                "script": "男：小刘，明天咱们去打羽毛球怎么样？\n女：明天正好有事，我跟朋友约好了明天要去趟大使馆。\n问：明天小刘要做什么？"
            },
            {
                "num": 12,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 想",
                    "B. 不想",
                    "C. 过去了",
                    "D. 考虑一下"
                ],
                "correct": "A",
                "script": "女：春天了，天气逐渐暖和了，我们去公园看花吧。\n男：这个主意不错。\n问：男想去公园看花吗？"
            },
            {
                "num": 13,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 好多了",
                    "B. 完全好了",
                    "C. 还很严重",
                    "D. 更严重了"
                ],
                "correct": "A",
                "script": "男：你感冒好了吗？\n女：差不多了，就是偶尔还会咳嗽。\n问：女感冒怎么样了？"
            },
            {
                "num": 14,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 公司环境",
                    "B. 同事关系",
                    "C. 北方的气候",
                    "D. 北方的交通"
                ],
                "correct": "C",
                "script": "女：北方太干燥了，我觉得很不舒服。\n男：习惯了就好了，我刚来时跟你一样。\n问：女对什么不适应？"
            },
            {
                "num": 15,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 会议内容",
                    "B. 儿童健康",
                    "C. 注意健康",
                    "D. 内容怎么改"
                ],
                "correct": "A",
                "script": "男：今天会议的内容是“注意健康”，对吗？\n女：您怎么忘了？已经改成“儿童健康”了。\n问：他们在谈什么？"
            },
            {
                "num": 16,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 她病了",
                    "B. 风不大",
                    "C. 出汗好",
                    "D. 要及时擦汗"
                ],
                "correct": "D",
                "script": "女：现在风刮得这么大，出了汗要及时擦掉，小心感冒。\n男：没关系，我身体好，不会那么容易生病的。\n问：女的是什么意思？"
            },
            {
                "num": 17,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 认真",
                    "B. 写了好久",
                    "C. 想起来了",
                    "D. 忽然忘了"
                ],
                "correct": "C",
                "script": "男：你不是说你都忘了吗？怎么还写得这么清楚？\n女：连我自己也不敢相信，一拿起笔忽然就想起来了。\n问：女为什么写得那么清楚？"
            },
            {
                "num": 18,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 游泳",
                    "B. 爬山",
                    "C. 看书",
                    "D. 旅行"
                ],
                "correct": "C",
                "script": "女：听说小刘特别喜欢爬山和游泳，是真的吗？\n男：爬山？游泳？没错，不过他喜欢在书本里游，在书本上爬。\n问：小刘喜欢做什么？"
            },
            {
                "num": 19,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 超市",
                    "B. 机场",
                    "C. 地铁站",
                    "D. 火车上"
                ],
                "correct": "A",
                "script": "男：欢迎光临，请您在购物时照顾好自己的小孩，避免走失。\n女：谢谢，我会一直拉住孩子的手。\n问：他们可能在哪儿？"
            },
            {
                "num": 20,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 奇怪",
                    "B. 吃惊",
                    "C. 怀疑",
                    "D. 生气"
                ],
                "correct": "D",
                "script": "女：要想跟我们公司合作，条件就是这样的。\n男：你们也太不像话了，哪有这样谈生意的。\n问：根据对话，可以知道男说话时怎么样？"
            },
            {
                "num": 21,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 律师",
                    "B. 医生",
                    "C. 教师",
                    "D. 职员"
                ],
                "correct": "C",
                "script": "男：你们寒假放一个月呢，真羡慕你们！\n女：我们这个职业就有这点儿好处，但平时得为学生操心啊。\n问：女可能是做什么的？"
            },
            {
                "num": 22,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 邻居",
                    "B. 同事",
                    "C. 夫妻",
                    "D. 母子"
                ],
                "correct": "C",
                "script": "女：听邻居说今天超市鱼很便宜，儿子喜欢吃，你去买两条吧！\n男：没问题，下午我下了班就去买。\n问：他们是什么关系？"
            },
            {
                "num": 23,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 她请客",
                    "B. 她不想吃",
                    "C. 菜不好吃",
                    "D. 她有约会了"
                ],
                "correct": "B",
                "script": "男：这家饭馆儿的菜特别好吃，今天我请客，咱们好好儿吃一顿。\n女：这儿的菜是做得不错，但是我今天有点儿不舒服，还是改天吧。\n问：女的是什么意思？"
            },
            {
                "num": 24,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 接电话",
                    "B. 接她爸爸",
                    "C. 记电话号码",
                    "D. 联系她爸爸"
                ],
                "correct": "D",
                "script": "女：我昨天给爸爸打了一天电话，他都没接。\n男：你是不是记错电话号码了？\n问：从对话中我们知道女做什么了？"
            },
            {
                "num": 25,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 学习方法",
                    "B. 学习环境",
                    "C. 学习效果",
                    "D. 学习条件"
                ],
                "correct": "C",
                "script": "男：我总感觉上午学习比下午好，我一个上午能背好几篇课文，下午却不行。\n男：就是，我也这么认为。\n问：他们在谈论什么？"
            }
        ]
    },
    "DE_21": {
        "title": "Bộ Đề 21",
        "audio_id": "1HYXMBcvonZuk0dmZhJl0PQjg_RRug7Tk",
        "questions": [
            {
                "num": 26,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 空调",
                    "B. 冰箱",
                    "C. 洗衣机",
                    "D. 电脑"
                ],
                "correct": "A",
                "script": "女：咱们家这个空调太旧了。\n男：是，制冷效果不太好了。\n女：那咱们星期六去商店看看，买一台新的？\n男：行。\n问：他们打算买什么？"
            },
            {
                "num": 27,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 六月一号",
                    "B. 七月一号",
                    "C. 七月九号",
                    "D. 八月九号"
                ],
                "correct": "D",
                "script": "男：你工作找得怎么样了？\n女：挺顺利的，已经定下来了。\n男：太好了！祝贺你！什么时候正式上班？\n女：七月九号。\n问：关于女，可以知道什么？"
            },
            {
                "num": 28,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 那儿太热了",
                    "B. 那儿风太大",
                    "C. 那儿不漂亮",
                    "D. 那儿太冷了"
                ],
                "correct": "D",
                "script": "女：快放寒假了，你有什么安排？\n男：我打算去东北玩儿。\n女：东三省？那儿冬天多冷啊！你怎么会想去那儿玩儿？\n男：冷是冷，可是那儿冬天也很漂亮。\n问：女觉得东北怎么样？"
            },
            {
                "num": 29,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 售货员送的",
                    "B. 以前邻居一个阿姨送的",
                    "C. 爸爸送的",
                    "D. 朋友送的"
                ],
                "correct": "B",
                "script": "男：这个盒子好像坏了。\n女：是吗？你小心点儿，先放桌上吧。\n男：这里面是什么啊？\n女：是几个杯子，是以前邻居一个阿姨送我的。\n问：杯子是谁送的？"
            }
        ]
    },
    "DE_22": {
        "title": "Bộ Đề 22",
        "audio_id": "1wSZnrPeNBrlq4yNTKg7V4-1TaRrtiuPo",
        "questions": [
            {
                "num": 11,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 选项A",
                    "B. 选项B",
                    "C. 选项C",
                    "D. 选项D"
                ],
                "correct": "A",
                "script": "男：这是一段听力文本。\n女：是的，这是一段听力文本。\n问：关于他们，可以知道什么？"
            },
            {
                "num": 12,
                "question_text": "根据听力内容选择正确答案：",
                "options": [
                    "A. 选项A",
                    "B. 选项B",
                    "C. 选项C",
                    "D. 选项D"
                ],
                "correct": "B",
                "script": "男：这是第二段听力文本。\n女：是的。\n问：男的是什么意思？"
            }
        ]
    }
}

# TẠO CÁC TABS ĐỀ THI
tab_keys = list(exam_data.keys())
tab_titles = [exam_data[k]["title"] for k in tab_keys]

tabs = st.tabs(tab_titles)

for idx, tab_key in enumerate(tab_keys):
    with tabs[idx]:
        data = exam_data[tab_key]
        
        # Trình phát Audio và Nút liên kết Drive dự phòng
        stream_url = f"https://docs.google.com/uc?export=download&id={data['audio_id']}"
        st.markdown(f"""
            <div class="audio-wrapper">
                <h3>🎵 听力音频播放器 / TRÌNH PHÁT BÀI NGHE - {data['title'].upper()}</h3>
                <p style="font-size: 13px; color: #334155 !important; margin: 5px 0 0 0;">
                    💡 <b>LƯU Ý QUAN TRỌNG:</b> Nếu trình phát bên dưới bị xoay vòng hoặc báo lỗi không phát được (do trình duyệt của bạn đang chặn Cookie/Quyền riêng tư), bạn hãy nhấn nút <b>"Mở file nghe dự phòng"</b> bên cạnh để nghe trực tiếp cực kỳ mượt mà từ Google Drive nhé!
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Sắp xếp trình phát và nút dự phòng song song
        col_audio, col_link = st.columns([3, 2])
        with col_audio:
            st.audio(stream_url, format="audio/mpeg")
        with col_link:
            st.markdown("<div style='margin-top: 6px;'></div>", unsafe_allow_html=True)
            st.link_button(
                "🔗 Mở file nghe dự phòng (Google Drive)",
                f"https://drive.google.com/file/d/{data['audio_id']}/view?usp=sharing",
                use_container_width=True
            )
        st.write("---")
        
        # State lưu đáp án đã chọn của tab hiện tại
        if f"answers_{tab_key}" not in st.session_state:
            st.session_state[f"answers_{tab_key}"] = {}
        if f"submitted_{tab_key}" not in st.session_state:
            st.session_state[f"submitted_{tab_key}"] = False
            
        submitted = st.session_state[f"submitted_{tab_key}"]
        
        # Form câu hỏi
        user_answers = {}
        for q in data["questions"]:
            st.markdown(f'<span class="q-badge">第 {q["num"]} 题</span>', unsafe_allow_html=True)
            st.write(f"**{q['question_text']}**")
            
            # Format các options cho radio button
            options = q["options"]
            
            # Lấy đáp án cũ đã chọn nếu có
            default_val = None
            if q["num"] in st.session_state[f"answers_{tab_key}"]:
                saved_ans = st.session_state[f"answers_{tab_key}"][q["num"]]
                for i, opt in enumerate(options):
                    if opt.startswith(saved_ans):
                        default_val = i
                        break
                        
            # Tạo Widget Radio Button
            selected_option = st.radio(
                label=f"q_{tab_key}_{q['num']}",
                options=options,
                index=default_val if default_val is not None else 0,
                key=f"widget_{tab_key}_{q['num']}",
                disabled=submitted,
                label_visibility="collapsed"
            )
            
            # Lưu câu trả lời của người dùng (chỉ lấy ký tự đầu A, B, C, D)
            user_char = selected_option[0] if selected_option else None
            user_answers[q["num"]] = user_char
            
            # Hiển thị giải thích / kết quả và Script nếu đã nộp bài
            if submitted:
                correct_char = q["correct"]
                if user_char == correct_char:
                    st.success("✓ 回答正确 (Đúng rồi!)")
                else:
                    st.error(f"✗ 回答错误。正确答案是：{correct_char}")
                    
                    # Hiện Script hội thoại cho câu trả lời sai
                    with st.expander("🔍 查看听力文本 (Xem Script)"):
                        st.markdown(f"**听力文本 (Transcript):**")
                        st.code(q["script"], language="markdown")
            st.write("")
            
        st.write("---")
        
        # Nút nộp bài riêng cho từng Tab
        if not submitted:
            if st.button(f"Nộp Bài {data['title']}", key=f"btn_submit_{tab_key}"):
                if not student_name.strip():
                    st.warning("⚠️ 请先输入您的姓名！/ Vui lòng nhập họ tên ở khung phía trên trước khi nộp bài.")
                else:
                    st.session_state[f"answers_{tab_key}"] = user_answers
                    st.session_state[f"submitted_{tab_key}"] = True
                    st.rerun()
        else:
            # Chấm điểm và hiển thị kết quả
            correct_count = 0
            total_qs = len(data["questions"])
            saved_answers = st.session_state[f"answers_{tab_key}"]
            
            for q in data["questions"]:
                if saved_answers.get(q["num"]) == q["correct"]:
                    correct_count += 1
                    
            # Trình bày đúng mẫu text yêu cầu
            result_text = f"""
- Chúc mừng bạn đã hoàn thành bộ đề {data['title']}!

Điểm số của bạn là: {correct_count}/{total_qs}

Nhớ nghe lại chỗ mình làm chưa đúng nhaaa~
"""
            st.info(result_text)
            
            # GỬI ĐIỂM VỀ GOOGLE SHEETS QUA WEBHOOK (Apps Script)
            if WEBHOOK_URL and "xxxxxxxxx" not in WEBHOOK_URL:
                with st.spinner("⏳ Đang gửi kết quả bài làm về Google Sheets..."):
                    try:
                        payload = {
                            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                            "studentName": student_name,
                            "examCode": data["title"],
                            "score": f"{correct_count}/{total_qs}"
                        }
                        response = requests.post(WEBHOOK_URL, json=payload, timeout=10)
                        if response.status_code == 200:
                            st.success("✅ Điểm số đã được đồng bộ tự động lên Google Sheets của cô thành công!")
                        else:
                            st.warning(f"⚠️ Không thể gửi điểm tự động lên Sheet (Lỗi mạng HTTP: {response.status_code}). Học viên hãy chụp ảnh màn hình kết quả này gửi riêng cho cô nhé!")
                    except Exception as e:
                        st.error(f"❌ Đồng bộ điểm thất bại do lỗi kết nối: {str(e)}. Học viên hãy chụp ảnh màn hình kết quả điểm số này gửi cho cô nhé!")

# CĂN GIỮA DÒNG CHỮ Ở FOOTER
st.markdown("""
    <div class="footer">
        黄宝玉老师
    </div>
""", unsafe_allow_html=True)
