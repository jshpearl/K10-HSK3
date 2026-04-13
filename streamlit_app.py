import streamlit as st
import random

# --- 1. KHO DỮ LIỆU TỔNG HỢP 150 TỪ ---
vocab_db = [
    # Nhóm 1
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
    # Nhóm 2
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
    # Nhóm 3
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
    # Nhóm 4
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
    # Nhóm 5
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
    # Nhóm 6
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
]

# --- 2. CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="HSK 3 - Master Quiz 150", page_icon="🎓")
st.markdown("<style>header {visibility: hidden;} footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# --- 3. QUẢN LÝ TRẠNG THÁI ---
if 'master_questions' not in st.session_state:
    sampled = random.sample(vocab_db, 20) # Mỗi lượt bốc 20 từ ngẫu nhiên
    questions = []
    for item in sampled:
        mode = random.choice(['p', 'm']) # Ngẫu nhiên hỏi Phiên âm hay Nghĩa
        if mode == 'p':
            q_text = f"Phiên âm của từ '{item['h']}' là gì?"
            correct = item['p']
            others = list(set([v['p'] for v in vocab_db if v['p'] != correct]))
        else:
            q_text = f"Nghĩa của từ '{item['h']}' là gì?"
            correct = item['m']
            others = list(set([v['m'] for v in vocab_db if v['m'] != correct]))
            
        distractors = random.sample(others, 3)
        opts = distractors + [correct]
        random.shuffle(opts)
        questions.append({"q": q_text, "options": opts, "a": correct, "word": item['h']})
        
    st.session_state.master_questions = questions
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.quiz_done = False

# --- 4. HIỂN THỊ CÂU HỎI ---
if not st.session_state.quiz_done:
    st.title("🚀 Thử thách 150 từ vựng HSK 3")
    st.write("Học xong không lo quên! Làm bộ đề ngẫu nhiên 20 câu mỗi ngày.")
    
    idx = st.session_state.current_idx
    q = st.session_state.master_questions[idx]
    
    st.progress((idx) / 20)
    st.subheader(f"Câu {idx+1}/20")
    st.info(q['q'])
    
    choice = st.radio("Chọn đáp án:", q['options'], key=f"quiz_{idx}")
    
    if st.button("Câu tiếp theo ➡️"):
        st.session_state.user_answers.append(choice)
        if choice == q['a']:
            st.session_state.score += 1
            
        if idx < 19:
            st.session_state.current_idx += 1
            st.rerun()
        else:
            st.session_state.quiz_done = True
            st.rerun()
else:
    # --- KẾT QUẢ ---
    st.balloons()
    st.header("HOÀN THÀNH! 🎉")
    st.metric("Điểm số của bạn", f"{st.session_state.score}/20")
    
    if st.button("Làm bộ đề ngẫu nhiên mới 🔄"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
        
    st.divider()
    st.subheader("Xem lại đáp án:")
    for i, q in enumerate(st.session_state.master_questions):
        user_ans = st.session_state.user_answers[i]
        is_correct = user_ans == q['a']
        color = "green" if is_correct else "red"
        icon = "✅" if is_correct else "❌"
        
        with st.expander(f"{icon} Câu {i+1}: {q['word']}"):
            st.write(f"**Câu hỏi:** {q['q']}")
            st.write(f"**Bạn chọn:** {user_ans}")
            st.write(f"**Đáp án đúng:** {q['a']}")
