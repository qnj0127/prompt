import streamlit as st

# ===================== 全局美化CSS（儿童友好） =====================
st.markdown("""
<style>
/* 页面整体背景 */
.stApp {
    background-color: #fffdf8;
}
/* 主标题样式 */
h1 {
    color: #e69500 !important;
    font-family: "Microsoft YaHei";
    font-weight: bold;
}
/* 子标题、文本放大 */
.stMarkdown p {
    font-size: 16px !important;
    color: #444444;
}
/* 下拉输入框圆角放大 */
div.stSelectbox > div, div.stTextInput > div {
    border-radius: 14px !important;
}
/* 醒目的生成按钮 */
div.stButton > button:first-child {
    background: linear-gradient(90deg,#ff91a4,#ff7096);
    color: white !important;
    font-size: 22px !important;
    font-weight: bold !important;
    padding: 16px 40px !important;
    border-radius: 16px !important;
    border: none !important;
    display:block;
    margin:35px auto 15px auto;
    width: 360px;
}
div.stButton > button:first-child:hover {
    background: linear-gradient(90deg,#ff7b92,#ff5b82);
    transform: scale(1.04);
    transition: all 0.25s ease;
}
</style>
""", unsafe_allow_html=True)

# ===================== 页面标题与介绍 =====================
st.title("🎨 AI提示词生成器😊")
st.write("这是一个AI绘画提示词小工具，小朋友可以轻松制作画画指令！")
st.write("在下方选择喜欢的选项，点击【生成提示词】就可以得到绘画文案。")
st.subheader("", divider="rainbow")

# ===================== 1.选择类型 =====================
category = st.selectbox(
    "请选择 :red[**类型**]",
    ("🏞️景点", "👧人物", "🍜食物"),
    index=None,
    placeholder="请选择类型..."
)
st.write("你选择了：", f":rainbow[{category}]")

# ===================== 2.输入内容 =====================
site = st.text_input(
    "请输入 :red[**景点**]",
    placeholder="例如：龙门石窟、白马寺"
)
st.write("你填写的内容：", site)

# ===================== 3.选择画面比例 =====================
ratio = st.selectbox(
    "请选择 :red[**画面比例**]",
    (
        "1:1 正方形，头像",
        "2:3 社交媒体，自拍",
        "3:4 经典比例，拍照",
        "4:3 文章配图，插画",
        "9:16 手机壁纸，人像",
        "16:9 桌面壁纸，风景"
    ),
    index=None,
    placeholder="请选择比例..."
)
st.write("你选择了：", f":rainbow[{ratio}]")

# ===================== 4.选择绘画风格 =====================
style = st.selectbox(
    "请选择 :red[**风格**]",
    (
        "人像摄影",
        "电影写真",
        "中国风",
        "动漫",
        "3D渲染",
        "赛博朋克",
        "CG 动画",
        "水墨画",
        "油画",
        "古典",
        "水彩画",
        "卡通",
        "平面插画",
        "风景",
        "港风动漫",
        "像素风格",
        "荧光绘画",
        "彩铅画",
        "手办",
        "儿童绘画",
        "抽象",
        "锐笔插画",
        "二次元",
        "油墨印刷",
        "版画",
        "莫奈",
        "毕加索",
        "伦勃朗",
        "马蒂斯",
        "巴洛克",
        "复古动漫",
        "绘本"
    ),
    index=None,
    placeholder="请选择风格..."
)
st.write("你选择了：", f":rainbow[{style}]")

st.subheader("", divider="rainbow")

# ===================== 生成按钮 =====================
gen_btn = st.button("✨ 生成提示词 ✨")

# ===================== 点击生成逻辑 =====================
if gen_btn:
    if not category or not site or not ratio or not style:
        st.warning("⚠️ 所有选项都要填写完整哦！")
        st.stop()
    prompt = f"""
        生成一张{site}视觉素材。
        要求:
        中国河南洛阳真实文化。
        适合Scratch互动作品。
        视觉风格: {style}
        图片比例: {ratio}
        高清。
        主体突出。
        背景干净。
        无文字。
    """
    st.code(prompt, language="markdown")