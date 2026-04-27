"""
rebuild_index.py
把所有 .md 全文重新嵌入 index.html 的 mdContents JS 物件。

用法（在終端機執行）：
    cd /Users/jesse/Documents/0_社區管理
    python3 rebuild_index.py

新增文件時：在下方 docs 清單加一行即可，格式：
    ('編號', '檔案名稱.md'),


#新增文件時，只需在腳本的 docs 清單加一行，例如：
#('J02', '和境心見社區-J02-新辦法名稱(草擬).md'),

cd /Users/jesse/Documents/0_社區管理
python3 rebuild_index.py
git add . && git commit -m "說明此次修改" && git push


"""

import os, re

# ── 路徑設定 ──────────────────────────────────────────
workspace  = os.path.dirname(os.path.abspath(__file__))   # 腳本所在目錄
index_path = os.path.join(workspace, 'index.html')

# ── 文件清單（編號, 檔名）────────────────────────────
docs = [
    ('規約',  '和境心見社區-規約-114年正式版住戶管理規約.md'),
    ('A01',   '和境心見社區-A01-管理委員會組織與運作辦法(草擬).md'),
    ('A02',   '和境心見社區-A02-區分所有權人會議管理辦法(草擬).md'),
    ('A03',   '和境心見社區-A03-管理委員會交接與移交作業辦法(草擬).md'),
    ('B01',   '和境心見社區-B01-住戶規約與各項管理辦法適用準則(草擬).md'),
    ('B02',   '和境心見社區-B02-違規管理與裁罰辦法(草擬).md'),
    ('C01',   '和境心見社區-C01-財務與預算暨基金管理辦法(草擬).md'),
    ('D01',   '和境心見社區-D01-資產與採購管理辦法(草擬).md'),
    ('E01',   '和境心見社區-E01-社區安全與防災管理辦法(草擬).md'),
    ('F01',   '和境心見社區-F01-公共設施使用管理辦法(草擬).md'),
    ('G01',   '和境心見社區-G01-住戶生活管理辦法(草擬).md'),
    ('G02',   '和境心見社區-G02-垃圾分類與資源回收管理辦法(草擬).md'),
    ('G03',   '和境心見社區-G03-寵物管理辦法(草擬).md'),
    ('G04',   '和境心見社區-G04-代收郵件領取管理辦法(草擬).md'),
    ('H01',   '和境心見社區-H01-車輛與門禁管理辦法(草擬).md'),
    ('I01',   '和境心見社區-I01-資訊與資料安全管理辦法(草擬).md'),
    ('J01',   '和境心見社區-J01-社區溝通與住戶服務管理辦法(草擬).md'),
    ('K01',   '和境心見社區-K01-裝修與施工管理辦法(草擬).md'),
    ('L01',   '和境心見社區-L01-租售暨仲介人員管理辦法(草擬).md'),
    ('SOP01', '和境心見社區-SOP01-社區安全維護SOP作業程序.md'),
]

# ── 工具函式 ─────────────────────────────────────────
def escape_for_template_literal(text):
    text = text.replace('\\', '\\\\')
    text = text.replace('`',  '\\`')
    text = text.replace('${', '\\${')
    return text

# ── 讀取 index.html ───────────────────────────────────
with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 建立新的 mdContents JS 物件 ───────────────────────
lines = ['const mdContents = {']
for key, fname in docs:
    fpath = os.path.join(workspace, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        escaped = escape_for_template_literal(content)
        # key 必須與 index.html 中 mdContents[doc.file] 的查詢方式一致，使用完整檔名
        lines.append(f'  "{fname}": `{escaped}`,')
        print(f'✓ {key}: {len(content):,} chars')
    else:
        print(f'✗ 找不到檔案：{fname}')
lines.append('};')
new_mdContents = '\n'.join(lines)

# ── 取代 index.html 中的舊 mdContents 區塊 ───────────
pattern  = r'const mdContents = \{.*?\};'
new_html, count = re.subn(pattern, new_mdContents, html, count=1, flags=re.DOTALL)

if count == 0:
    print('\n❌ 錯誤：找不到 mdContents 區塊，index.html 未更新。')
else:
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f'\n✓ index.html 重建完成（{len(new_html):,} chars）')
