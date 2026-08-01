from pathlib import Path

def load_site():
    file_path = Path('template') / "sites.txt"
    if not file_path.exists():
        st.error("模板文件不存在，请检查路径。")
        st.stop()
    with open(file_path, "r", encoding="utf-8") as f:
        sites = f.readlines()
    return sites

def generate_prompt( site, ratio, style):
    template = load_site()
    prompt = template.replace("{{site}}",site)
    prompt = prompt.replace("{{style}}",style)
    prompt = prompt.replace("{{ratio}}",ratio)
    return prompt

