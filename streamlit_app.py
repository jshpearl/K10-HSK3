import streamlit as st
import random

# --- DANH SÁCH ẢNH GIF CHÚC MỪNG ---
gif_urls = [
    "https://i.pinimg.com/originals/fc/d6/fb/fcd6fb686facbcaf97f4602e6be6e04c.gif",
    "https://i.pinimg.com/originals/63/fa/7b/63fa7b8ceef65ed89ffefd2a834811ff.gif",
    "https://i.pinimg.com/originals/24/86/37/248637585fe5c57890aea979eb38bbbf.gif",
    "https://i.pinimg.com/originals/06/a6/c0/06a6c008c8d9b9f98fdf583373e8d87b.gif",
    "https://i.pinimg.com/originals/e9/54/8f/e9548f99211cb5a4999a68c0ff6d2862.gif",
    "https://i.pinimg.com/originals/11/82/59/118259993924863bd3f6457da365e2ac.gif",
    "https://i.pinimg.com/originals/47/65/fb/4765fbd8b250194051468ec3a0085a12.gif",
    "https://i.pinimg.com/originals/87/62/b8/8762b8ed3f80980481df7d73afa2fcff.gif",
    "https://i.pinimg.com/originals/be/62/73/be627352f3f42519bb417efd5556eabf.gif",
    "https://i.pinimg.com/originals/4a/e1/5a/4ae15a7a77842a2111db77ce3a802114.gif",
    "https://i.pinimg.com/originals/70/88/dc/7088dcfbb6d5004f62a260264d99ed2d.gif",
    "https://i.pinimg.com/originals/6b/c6/ed/6bc6edef34fb9e763f12aaf74b25310a.gif",
    "https://i.pinimg.com/originals/15/41/0f/15410fa493fdaf97e895647a102d9d5c.gif",
    "https://i.pinimg.com/originals/6f/d1/5a/6fd15a59ca0af6fddf6779ffbf050e82.gif"
]

# --- 1. KHO DỮ LIỆU TỔNG HỢP 300 TỪ (12 NHÓM) ---
vocab_db = [
    # --- Nhóm 1 ---
    {"h": "熊猫", "p": "xióngmāo", "m": "Gấu trúc"},
    {"h": "刚才", "p": "gāngcái", "m": "Vừa nãy"},
    {"h": "蓝", "p": "lán", "m": "Màu xanh da trời"},
    {"h": "终于", "p": "zhōngyú", "m": "Cuối cùng thì"},
    {"h": "简单", "p": "jiǎndān", "m": "Đơn giản"},
    {"h": "礼物", "p": "lǐwù", "m": "Quà tặng"},
    {"h": "愿意", "p": "yuànyì", "m": "Sẵn lòng/Bằng lòng"},
    {"h": "洗手间", "p": "xǐshǒujiān", "m": "Nhà vệ sinh"},
    {"h": "西", "p": "xī", "m": "Phía Tây"},
    {"h": "经理", "p": "jīnglǐ", "m": "Giám đốc/Quản lý"},
    {"h": "历史", "p": "lìshǐ", "m": "Lịch sử"},
    {"h": "画", "p": "huà", "m": "Vẽ/Bức tranh"},
    {"h": "故事", "p": "gùshì", "m": "Câu chuyện"},
    {"h": "还是", "p": "háishi", "m": "Hoặc là (câu hỏi)/Vẫn"},
    {"h": "低", "p": "dī", "m": "Thấp"},
    {"h": "以前", "p": "yǐqián", "m": "Trước đây"},
    {"h": "几乎", "p": "jīhū", "m": "Hầu như/Suýt nữa"},
    {"h": "检查", "p": "jiǎnchá", "m": "Kiểm tra"},
    {"h": "结婚", "p": "jiéhūn", "m": "Kết hôn"},
    {"h": "记得", "p": "jìde", "m": "Nhớ"},
    {"h": "经常", "p": "jīngcháng", "m": "Thường xuyên"},
    {"h": "解决", "p": "jiějué", "m": "Giải quyết"},
    {"h": "借", "p": "jiè", "m": "Mượn/Vay"},
    {"h": "决定", "p": "juédìng", "m": "Quyết định"},
    {"h": "可爱", "p": "kě'ài", "m": "Đáng yêu"},
    
    # --- Nhóm 2 ---
    {"h": "阿姨", "p": "āyí", "m": "Dì/Cô"},
    {"h": "突然", "p": "tūrán", "m": "Đột nhiên"},
    {"h": "干净", "p": "gānjìng", "m": "Sạch sẽ"},
    {"h": "明白", "p": "míngbai", "m": "Hiểu/Rõ ràng"},
    {"h": "胖", "p": "pàng", "m": "Béo"},
    {"h": "相信", "p": "xiāngxìn", "m": "Tin tưởng"},
    {"h": "太阳", "p": "tàiyáng", "m": "Mặt trời"},
    {"h": "打算", "p": "dǎsuàn", "m": "Dự định/Kế hoạch"},
    {"h": "发现", "p": "fāxiàn", "m": "Phát hiện"},
    {"h": "同事", "p": "tóngshì", "m": "Đồng nghiệp"},
    {"h": "兴趣", "p": "xìngqù", "m": "Hứng thú/Sở thích"},
    {"h": "舒服", "p": "shūfu", "m": "Thoải mái/Dễ chịu"},
    {"h": "变化", "p": "biànhuà", "m": "Thay đổi/Biến hóa"},
    {"h": "饮料", "p": "yǐnliào", "m": "Đồ uống"},
    {"h": "特别", "p": "tèbié", "m": "Đặc biệt"},
    {"h": "相同", "p": "xiāngtóng", "m": "Giống nhau"},
    {"h": "奇怪", "p": "qíguài", "m": "Kỳ lạ"},
    {"h": "热情", "p": "rèqíng", "m": "Nhiệt tình"},
    {"h": "必须", "p": "bìxū", "m": "Bắt buộc/Phải"},
    {"h": "只有", "p": "zhǐyǒu", "m": "Chỉ có"},
    {"h": "总是", "p": "zǒngshì", "m": "Luôn luôn"},
    {"h": "担心", "p": "dānxīn", "m": "Lo lắng"},
    {"h": "举行", "p": "jǔxíng", "m": "Tổ chức/Cử hành"},
    {"h": "世界", "p": "shìjiè", "m": "Thế giới"},
    {"h": "准备", "p": "zhǔnbèi", "m": "Chuẩn bị"},

    # --- Nhóm 3 ---
    {"h": "草", "p": "cǎo", "m": "Cỏ"},
    {"h": "层", "p": "céng", "m": "Tầng/Lớp"},
    {"h": "差", "p": "chà", "m": "Kém/Tồi"},
    {"h": "声音", "p": "shēngyīn", "m": "Âm thanh/Tiếng nói"},
    {"h": "衬衫", "p": "chènshān", "m": "Áo sơ mi"},
    {"h": "成绩", "p": "chéngjì", "m": "Thành tích/Kết quả"},
    {"h": "城市", "p": "chéngshì", "m": "Thành phố"},
    {"h": "迟到", "p": "chídào", "m": "Đến muộn"},
    {"h": "出现", "p": "chūxiàn", "m": "Xuất hiện"},
    {"h": "厨房", "p": "chúfáng", "m": "Nhà bếp"},
    {"h": "除了", "p": "chúle", "m": "Ngoài... ra"},
    {"h": "词典", "p": "cídiǎn", "m": "Từ điển"},
    {"h": "聪明", "p": "cōngming", "m": "Thông minh"},
    {"h": "打扫", "p": "dǎsǎo", "m": "Quét dọn/Vệ sinh"},
    {"h": "蛋糕", "p": "dàngāo", "m": "Bánh ngọt"},
    {"h": "当然", "p": "dāngrán", "m": "Đương nhiên"},
    {"h": "灯", "p": "dēng", "m": "Đèn"},
    {"h": "地方", "p": "dìfang", "m": "Địa điểm/Nơi chốn"},
    {"h": "地铁", "p": "dìtiě", "m": "Tàu điện ngầm"},
    {"h": "地图", "p": "dìtú", "m": "Bản đồ"},
    {"h": "电梯", "p": "diàntī", "m": "Thang máy"},
    {"h": "电子邮件", "p": "diànzǐ yóujiàn", "m": "Email"},
    {"h": "东", "p": "dōng", "m": "Phía Đông"},
    {"h": "冬", "p": "dōng", "m": "Mùa đông"},
    {"h": "放", "p": "fàng", "m": "Đặt/Để/Thả"},

    # --- Nhóm 4 ---
    {"h": "动物", "p": "dòngwù", "m": "Động vật"},
    {"h": "短", "p": "duǎn", "m": "Ngắn"},
    {"h": "段", "p": "duàn", "m": "Đoạn/Khoảng"},
    {"h": "锻炼", "p": "duànliàn", "m": "Tập thể dục/Rèn luyện"},
    {"h": "多么", "p": "duōme", "m": "Biết bao nhiêu"},
    {"h": "饿", "p": "è", "m": "Đói"},
    {"h": "耳朵", "p": "ěrduo", "m": "Cái tai"},
    {"h": "发", "p": "fā", "m": "Gửi (email, tin nhắn)"},
    {"h": "放心", "p": "fàngxīn", "m": "Yên tâm"},
    {"h": "分", "p": "fēn", "m": "Phút/Điểm"},
    {"h": "附近", "p": "fùjìn", "m": "Lân cận/Gần đây"},
    {"h": "复习", "p": "fùxí", "m": "Ôn tập"},
    {"h": "敢", "p": "gǎn", "m": "Dám"},
    {"h": "感冒", "p": "gǎnmào", "m": "Cảm cúm"},
    {"h": "根据", "p": "gēnjù", "m": "Căn cứ vào"},
    {"h": "跟", "p": "gēn", "m": "Cùng/Với"},
    {"h": "更", "p": "gèng", "m": "Càng/Hơn"},
    {"h": "公共汽车", "p": "gōnggòng qìchē", "m": "Xe buýt"},
    {"h": "公斤", "p": "gōngjīn", "m": "Kilôgam (kg)"},
    {"h": "公司", "p": "gōngsī", "m": "Công ty"},
    {"h": "公园", "p": "gōngyuán", "m": "Công viên"},
    {"h": "关", "p": "guān", "m": "Đóng/Tắt"},
    {"h": "关系", "p": "guānxi", "m": "Quan hệ/Liên quan"},
    {"h": "关心", "p": "guānxīn", "m": "Quan tâm"},
    {"h": "关于", "p": "guānyú", "m": "Về/Liên quan đến"},

    # --- Nhóm 5 ---
    {"h": "国家", "p": "guójiā", "m": "Quốc gia"},
    {"h": "果汁", "p": "guǒzhī", "m": "Nước trái cây"},
    {"h": "过去", "p": "guòqù", "m": "Quá khứ/Trước đây"},
    {"h": "害怕", "p": "hàipà", "m": "Sợ hãi"},
    {"h": "航班", "p": "hángbān", "m": "Chuyến bay"},
    {"h": "黑板", "p": "hēibǎn", "m": "Bảng đen"},
    {"h": "后来", "p": "hòulái", "m": "Sau đó (quá khứ)"},
    {"h": "护照", "p": "hùzhào", "m": "Hộ chiếu"},
    {"h": "花", "p": "huā", "m": "Hoa/Tiêu (tiền, thời gian)"},
    {"h": "坏", "p": "huài", "m": "Hỏng/Xấu"},
    {"h": "欢迎", "p": "huānyíng", "m": "Chào mừng"},
    {"h": "环境", "p": "huánjìng", "m": "Môi trường"},
    {"h": "换", "p": "huàn", "m": "Đổi/Thay"},
    {"h": "黄", "p": "huáng", "m": "Màu vàng"},
    {"h": "会议", "p": "huìyì", "m": "Cuộc họp/Hội nghị"},
    {"h": "或者", "p": "huòzhě", "m": "Hoặc là (trần thuật)"},
    {"h": "机会", "p": "jīhuì", "m": "Cơ hội"},
    {"h": "极", "p": "jí", "m": "Cực kỳ"},
    {"h": "季节", "p": "jìjié", "m": "Mùa"},
    {"h": "见面", "p": "jiànmiàn", "m": "Gặp mặt"},
    {"h": "健康", "p": "jiànkāng", "m": "Khỏe mạnh"},
    {"h": "讲", "p": "jiǎng", "m": "Nói/Giảng/Kể"},
    {"h": "角", "p": "jiǎo", "m": "Hào (tiền tệ)"},
    {"h": "脚", "p": "jiǎo", "m": "Bàn chân"},
    {"h": "接", "p": "jiē", "m": "Đón/Nhận (điện thoại)"},

    # --- Nhóm 6 ---
    {"h": "街道", "p": "jiēdào", "m": "Đường phố"},
    {"h": "节目", "p": "jiémù", "m": "Chương trình/Tiết mục"},
    {"h": "节日", "p": "jiérì", "m": "Ngày lễ"},
    {"h": "结束", "p": "jiéshù", "m": "Kết thúc"},
    {"h": "久", "p": "jiǔ", "m": "Lâu (thời gian)"},
    {"h": "旧", "p": "jiù", "m": "Cũ"},
    {"h": "句子", "p": "jùzi", "m": "Câu văn"},
    {"h": "渴", "p": "kě", "m": "Khát"},
    {"h": "刻", "p": "kè", "m": "Khắc (15 phút)"},
    {"h": "客人", "p": "kèrén", "m": "Khách"},
    {"h": "空调", "p": "kōngtiáo", "m": "Điều hòa"},
    {"h": "口", "p": "kǒu", "m": "Nhân khẩu/Miệng"},
    {"h": "哭", "p": "kū", "m": "Khóc"},
    {"h": "裤子", "p": "kùzi", "m": "Cái quần"},
    {"h": "筷子", "p": "kuàizi", "m": "Đôi đũa"},
    {"h": "老", "p": "lǎo", "m": "Già/Cũ"},
    {"h": "离开", "p": "líkāi", "m": "Rời khỏi"},
    {"h": "脸", "p": "liǎn", "m": "Khuôn mặt"},
    {"h": "辆", "p": "liàng", "m": "Chiếc/Cái (xe)"},
    {"h": "聊天", "p": "liáotiān", "m": "Tán gẫu"},
    {"h": "了解", "p": "liǎojiě", "m": "Hiểu rõ"},
    {"h": "邻居", "p": "línjū", "m": "Hàng xóm"},
    {"h": "留学", "p": "liúxué", "m": "Du học"},
    {"h": "楼", "p": "lóu", "m": "Tòa nhà/Tầng"},
    {"h": "绿", "p": "lǜ", "m": "Màu xanh lá cây"},

    # --- Nhóm 7 ---
    {"h": "马", "p": "mǎ", "m": "Con ngựa"},
    {"h": "满意", "p": "mǎnyì", "m": "Hài lòng"},
    {"h": "帽子", "p": "màozi", "m": "Cái mũ"},
    {"h": "米", "p": "mǐ", "m": "Gạo/Mét"},
    {"h": "面包", "p": "miànbāo", "m": "Bánh mì"},
    {"h": "面条", "p": "miàntiáo", "m": "Mì sợi"},
    {"h": "拿", "p": "ná", "m": "Cầm/Lấy"},
    {"h": "奶奶", "p": "nǎinai", "m": "Bà nội"},
    {"h": "南", "p": "nán", "m": "Phía Nam"},
    {"h": "难", "p": "nán", "m": "Khó"},
    {"h": "难过", "p": "nánguò", "m": "Buồn bã"},
    {"h": "年级", "p": "niánjí", "m": "Lớp/Khối"},
    {"h": "年轻", "p": "niánqīng", "m": "Trẻ trung"},
    {"h": "鸟", "p": "niǎo", "m": "Con chim"},
    {"h": "努力", "p": "nǔlì", "m": "Nỗ lực"},
    {"h": "爬山", "p": "páshān", "m": "Leo núi"},
    {"h": "盘子", "p": "pánzi", "m": "Cái đĩa"},
    {"h": "啤酒", "p": "píjiǔ", "m": "Bia"},
    {"h": "便宜", "p": "piányi", "m": "Rẻ"},
    {"h": "票", "p": "piào", "m": "Vé"},
    {"h": "普通话", "p": "pǔtōnghuà", "m": "Tiếng phổ thông"},
    {"h": "骑", "p": "qí", "m": "Cưỡi/Đi (xe)"},
    {"h": "其实", "p": "qíshí", "m": "Thực ra"},
    {"h": "其他", "p": "qítā", "m": "Cái khác/Người khác"},
    {"h": "起飞", "p": "qǐfēi", "m": "Cất cánh"},

    # --- Nhóm 8 ---
    {"h": "起来", "p": "qǐlái", "m": "Dậy/Đứng dậy"},
    {"h": "清楚", "p": "qīngchu", "m": "Rõ ràng"},
    {"h": "请假", "p": "qǐngjià", "m": "Xin nghỉ"},
    {"h": "秋", "p": "qiū", "m": "Mùa thu"},
    {"h": "裙子", "p": "qúnzi", "m": "Cái váy"},
    {"h": "然后", "p": "ránhòu", "m": "Sau đó"},
    {"h": "认为", "p": "rènwéi", "m": "Cho rằng"},
    {"h": "认真", "p": "rènzhēn", "m": "Chăm chỉ/Nghiêm túc"},
    {"h": "容易", "p": "róngyì", "m": "Dễ dàng"},
    {"h": "如果", "p": "rúguǒ", "m": "Nếu"},
    {"h": "伞", "p": "sǎn", "m": "Cái ô/dù"},
    {"h": "上网", "p": "shàngwǎng", "m": "Lên mạng"},
    {"h": "世界", "p": "shìjiè", "m": "Thế giới"},
    {"h": "试", "p": "shì", "m": "Thử"},
    {"h": "瘦", "p": "shòu", "m": "Gầy"},
    {"h": "叔叔", "p": "shūshu", "m": "Chú"},
    {"h": "树", "p": "shù", "m": "Cái cây"},
    {"h": "数学", "p": "shùxué", "m": "Toán học"},
    {"h": "刷牙", "p": "shuāyá", "m": "Đánh răng"},
    {"h": "双", "p": "shuāng", "m": "Đôi/Cặp"},
    {"h": "水平", "p": "shuǐpíng", "m": "Trình độ"},
    {"h": "司机", "p": "sījī", "m": "Tài xế"},
    {"h": "虽然", "p": "suīrán", "m": "Mặc dù"},
    {"h": "糖", "p": "táng", "m": "Kẹo/Đường"},
    {"h": "疼", "p": "téng", "m": "Đau"},

    # --- Nhóm 9 ---
    {"h": "提高", "p": "tígāo", "m": "Nâng cao"},
    {"h": "体育", "p": "tǐyù", "m": "Thể dục/Thể thao"},
    {"h": "甜", "p": "tián", "m": "Ngọt"},
    {"h": "条", "p": "tiáo", "m": "Lượng từ (vật dài)"},
    {"h": "同意", "p": "tóngyì", "m": "Đồng ý"},
    {"h": "图书馆", "p": "túshūguǎn", "m": "Thư viện"},
    {"h": "腿", "p": "tuǐ", "m": "Cái chân"},
    {"h": "完成", "p": "wánchéng", "m": "Hoàn thành"},
    {"h": "碗", "p": "wǎn", "m": "Cái bát"},
    {"h": "万", "p": "wàn", "m": "Vạn (10.000)"},
    {"h": "忘记", "p": "wàngjì", "m": "Quên"},
    {"h": "为", "p": "wèi", "m": "Vì"},
    {"h": "为了", "p": "wèile", "m": "Vì để"},
    {"h": "位", "p": "wèi", "m": "Lượng từ (người)"},
    {"h": "文化", "p": "wénhuà", "m": "Văn hóa"},
    {"h": "习惯", "p": "xíguàn", "m": "Thói quen"},
    {"h": "洗澡", "p": "xǐzǎo", "m": "Tắm"},
    {"h": "夏", "p": "xià", "m": "Mùa hè"},
    {"h": "先", "p": "xiān", "m": "Trước"},
    {"h": "香蕉", "p": "xiāngjiāo", "m": "Quả chuối"},
    {"h": "向", "p": "xiàng", "m": "Về hướng"},
    {"h": "像", "p": "xiàng", "m": "Giống"},
    {"h": "小心", "p": "xiǎoxīn", "m": "Cẩn thận"},
    {"h": "校长", "p": "xiàozhǎng", "m": "Hiệu trưởng"},
    {"h": "鞋", "p": "xié", "m": "Cái giày"},

    # --- Nhóm 10 ---
    {"h": "新闻", "p": "xīnwén", "m": "Tin tức"},
    {"h": "新鲜", "p": "xīnxiān", "m": "Tươi mới"},
    {"h": "信", "p": "xìn", "m": "Bức thư"},
    {"h": "行李箱", "p": "xínglǐxiāng", "m": "Va li"},
    {"h": "兴趣", "p": "xìngqù", "m": "Hứng thú"},
    {"h": "熊猫", "p": "xióngmāo", "m": "Gấu trúc"},
    {"h": "修", "p": "xiū", "m": "Sửa"},
    {"h": "需要", "p": "xūyào", "m": "Cần"},
    {"h": "选择", "p": "xuǎnzé", "m": "Lựa chọn"},
    {"h": "眼镜", "p": "yǎnjìng", "m": "Cái kính"},
    {"h": "眼睛", "p": "yǎnjing", "m": "Đôi mắt"},
    {"h": "羊肉", "p": "yángròu", "m": "Thịt dê"},
    {"h": "阳光", "p": "yángguāng", "m": "Ánh nắng"},
    {"h": "样子", "p": "yàngzi", "m": "Dáng vẻ"},
    {"h": "要求", "p": "yāoqiú", "m": "Yêu cầu"},
    {"h": "药", "p": "yào", "m": "Thuốc"},
    {"h": "爷爷", "p": "yéye", "m": "Ông nội"},
    {"h": "一般", "p": "yìbān", "m": "Bình thường"},
    {"h": "一样", "p": "yíyàng", "m": "Giống nhau"},
    {"h": "一直", "p": "yìzhí", "m": "Luôn luôn"},
    {"h": "以为", "p": "yǐwéi", "m": "Tưởng rằng"},
    {"h": "已经", "p": "yǐjīng", "m": "Đã"},
    {"h": "音乐", "p": "yīnyuè", "m": "Âm nhạc"},
    {"h": "银行", "p": "yínháng", "m": "Ngân hàng"},
    {"h": "应该", "p": "yīnggāi", "m": "Nên"},
    
    # --- Nhóm 11 ---
    {"h": "影响", "p": "yǐngxiǎng", "m": "Ảnh hưởng"},
    {"h": "游戏", "p": "yóuxì", "m": "Trò chơi"},
    {"h": "有名", "p": "yǒumíng", "m": "Nổi tiếng"},
    {"h": "又", "p": "yòu", "m": "Lại (đã xảy ra)"},
    {"h": "遇到", "p": "yùdào", "m": "Gặp phải"},
    {"h": "元", "p": "yuán", "m": "Đồng (tiền)"},
    {"h": "越", "p": "yuè", "m": "Càng"},
    {"h": "月亮", "p": "yuèliang", "m": "Mặt trăng"},
    {"h": "云", "p": "yún", "m": "Mây"},
    {"h": "运动", "p": "yùndòng", "m": "Vận động / Thể thao"},
    {"h": "照相机", "p": "zhàoxiàngjī", "m": "Máy ảnh"},
    {"h": "只", "p": "zhǐ", "m": "Chỉ / Con (lượng từ)"},
    {"h": "中间", "p": "zhōngjiān", "m": "Ở giữa"},
    {"h": "种", "p": "zhǒng", "m": "Loại / Chủng loại"},
    {"h": "重要", "p": "zhòngyào", "m": "Quan trọng"},
    {"h": "周末", "p": "zhōumò", "m": "Cuối tuần"},
    {"h": "主要", "p": "zhǔyào", "m": "Chủ yếu"},
    {"h": "祝", "p": "zhù", "m": "Chúc"},
    {"h": "著名", "p": "zhùmíng", "m": "Nổi tiếng (trang trọng)"},
    {"h": "准备", "p": "zhǔnbèi", "m": "Chuẩn bị"},
    {"h": "字典", "p": "zìdiǎn", "m": "Từ điển"},
    {"h": "自己", "p": "zìjǐ", "m": "Tự mình / Bản thân"},
    {"h": "嘴", "p": "zuǐ", "m": "Miệng"},
    {"h": "最近", "p": "zuìjìn", "m": "Gần đây"},
    {"h": "作业", "p": "zuòyè", "m": "Bài tập"},

    # --- Nhóm 12 ---
    {"h": "作用", "p": "zuòyòng", "m": "Tác dụng / Ảnh hưởng"},
    {"h": "搬", "p": "bān", "m": "Chuyển / Dời / Khiêng"},
    {"h": "办法", "p": "bànfǎ", "m": "Biện pháp / Cách làm"},
    {"h": "办公室", "p": "bàngōngshì", "m": "Văn phòng"},
    {"h": "半", "p": "bàn", "m": "Một nửa / Rưỡi"},
    {"h": "帮忙", "p": "bāngmáng", "m": "Giúp đỡ"},
    {"h": "包", "p": "bāo", "m": "Túi / Bao"},
    {"h": "饱", "p": "bǎo", "m": "No"},
    {"h": "北方", "p": "běifāng", "m": "Phương Bắc"},
    {"h": "被", "p": "bèi", "m": "Bị / Được (bị động)"},
    {"h": "鼻子", "p": "bízi", "m": "Mũi"},
    {"h": "比较", "p": "bǐjiào", "m": "Khá / Tương đối"},
    {"h": "比赛", "p": "bǐsài", "m": "Cuộc thi / Thi đấu"},
    {"h": "笔记本", "p": "bǐjìběn", "m": "Vở ghi chép / Laptop"},
    {"h": "别人", "p": "biéren", "m": "Người khác"},
    {"h": "宾馆", "p": "bīnguǎn", "m": "Khách sạn"},
    {"h": "冰箱", "p": "bīngxiāng", "m": "Tủ lạnh"},
    {"h": "不但", "p": "búdàn", "m": "Không những"},
    {"h": "而且", "p": "érqiě", "m": "Mà còn"},
    {"h": "菜单", "p": "càidān", "m": "Thực đơn"},
    {"h": "参加", "p": "cānjiā", "m": "Tham gia"},
    {"h": "超市", "p": "chāoshì", "m": "Siêu thị"},
    {"h": "刚才", "p": "gāngcái", "m": "Vừa nãy"},
    {"h": "了解", "p": "liǎojiě", "m": "Hiểu rõ / Tìm hiểu"},
    {"h": "愿意", "p": "yuànyì", "m": "Bằng lòng / Sẵn sàng"}
]

# --- 2. CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="K10 - LUYỆN TẬP 300 TỪ HSK3", page_icon="📝")
st.markdown("<style>header {visibility: hidden;} footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# --- 3. QUẢN LÝ TRẠNG THÁI (SESSION STATE) ---
if 'all_used_words' not in st.session_state:
    st.session_state.all_used_words = []

if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

if 'result_gif' not in st.session_state:
    st.session_state.result_gif = None

if 'master_questions' not in st.session_state:
    # Lọc bỏ TẤT CẢ các từ đã từng xuất hiện
    available = [v for v in vocab_db if v['h'] not in st.session_state.all_used_words]
    
    # Reset nếu hết kho từ (hoặc còn ít hơn 20 từ)
    if len(available) < 20:
        st.session_state.all_used_words = []
        available = vocab_db
        st.warning("🔄 Đã học hết kho từ! Hệ thống sẽ bắt đầu lại từ đầu.")
        
    sampled = random.sample(available, 20)
    
    for s in sampled:
        st.session_state.all_used_words.append(s['h'])
        
    questions = []
    for item in sampled:
        mode = random.choice(['p', 'm'])
        if mode == 'p':
            q_text = f"Phiên âm của từ '{item['h']}' là gì?"
            correct = item['p']
            others = list(set([v['p'] for v in vocab_db if v['p'] != correct]))
        else:
            q_text = f"Nghĩa của từ '{item['h']}' là gì?"
            correct = item['m']
            others = list(set([v['m'] for v in vocab_db if v['m'] != correct]))
            
        # Lấy 3 đáp án sai ngẫu nhiên
        distractors = random.sample(others, 3)
        options = distractors + [correct]
        random.shuffle(options)
        
        questions.append({
            "q": q_text, 
            "options": options, 
            "a": correct, 
            "word": item['h'],
            "full_info": f"{item['h']} [{item['p']}]: {item['m']}"
        })
        
    st.session_state.master_questions = questions
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.user_answers = {}
    st.session_state.quiz_done = False
    st.session_state.result_gif = None

# --- 4. HIỂN THỊ CÂU HỎI ---
if not st.session_state.quiz_done:
    st.title("🎓 K10 ÔN TẬP 300 TỪ VỰNG HSK3")
    
    total_unique = len(set([v['h'] for v in vocab_db]))
    st.info(f"Đã luyện tập: {len(set(st.session_state.all_used_words))} / {total_unique} từ. Các lần tiếp theo sẽ không trùng lại!")
    
    idx = st.session_state.current_idx
    q = st.session_state.master_questions[idx]
    
    st.progress(idx / 20)
    st.subheader(f"Câu {idx+1}/20")
    st.markdown(f"### {q['q']}")
    
    # Giữ lại lựa chọn cũ nếu học viên quay lại câu này
    saved_ans = st.session_state.user_answers.get(idx)
    default_idx = q['options'].index(saved_ans) if saved_ans in q['options'] else 0
        
    choice = st.radio("Chọn đáp án của bạn:", q['options'], index=default_idx, key=f"radio_{idx}")
    
    # Thiết kế 2 cột cho 2 nút Quay lại và Tiếp theo
    col1, col2 = st.columns(2)
    
    with col1:
        if idx > 0:
            if st.button("⬅️ Quay lại câu trước"):
                st.session_state.user_answers[idx] = choice # Lưu tạm đáp án câu hiện tại
                st.session_state.current_idx -= 1
                st.rerun()
                
    with col2:
        if idx < 19:
            if st.button("Câu tiếp theo ➡️"):
                st.session_state.user_answers[idx] = choice # Lưu đáp án câu hiện tại
                st.session_state.current_idx += 1
                st.rerun()
        else:
            if st.button("Nộp bài 🏁"):
                st.session_state.user_answers[idx] = choice
                
                # Bắt đầu tính điểm toàn bộ bài
                final_score = 0
                for i, mq in enumerate(st.session_state.master_questions):
                    if st.session_state.user_answers.get(i) == mq['a']:
                        final_score += 1
                
                st.session_state.score = final_score
                st.session_state.quiz_done = True
                
                # Random chọn 1 ảnh GIF để hiện chúc mừng
                st.session_state.result_gif = random.choice(gif_urls)
                
                st.rerun()

else:
    st.balloons()
    st.header("HOÀN THÀNH BÀI ÔN TẬP! 🎉")
    
    # Hiện thị chiếc GIF chúc mừng (Blind Box)
    if st.session_state.result_gif:
        st.image(st.session_state.result_gif, width=350)
    
    st.metric("Điểm số của bạn", f"{st.session_state.score}/20")
    
    if st.button("Làm tiếp 20 từ khác (Không trùng từ cũ) 🔄"):
        del st.session_state.master_questions
        del st.session_state.current_idx
        del st.session_state.score
        del st.session_state.user_answers
        del st.session_state.quiz_done
        del st.session_state.result_gif
        st.rerun()

    st.divider()
    st.subheader("Xem lại bài làm lần này:")
    for i, q in enumerate(st.session_state.master_questions):
        user_ans = st.session_state.user_answers.get(i, "Chưa chọn")
        is_correct = user_ans == q['a']
        icon = "✅" if is_correct else "❌"
        
        with st.expander(f"{icon} Câu {i+1}: {q['word']}"):
            st.write(f"**Câu hỏi:** {q['q']}")
            st.write(f"**Bạn chọn:** {user_ans}")
            st.write(f"**Đáp án đúng:** {q['a']}")
            st.info(f"💡 Kiến thức: {q['full_info']}")
