# 和境心見社區 — 管理辦法工作流程說明 (CLAUDE.md)

> 本文件記錄整個社區管理辦法的編寫、管理與本機儲存的標準流程，
> 供後續作業保持一致性。

---

## 零、基本規定（必須遵守）

1. **語言**：所有 Claude 回應、處理流程說明、文件內容，一律使用**繁體中文**。
2. **文件格式**：管理辦法一律產出 **`.md`（Markdown）格式**，儲存於主工作目錄。
3. **索引頁**：所有管理辦法統一由 `index.html` 連結，提供瀏覽器開啟查詢。
4. **不使用 Google Drive**：不再上傳至 Google Drive，所有文件保存在本機目錄。

---

## 一、專案概述

**社區名稱：** 和境心見社區  
**負責人：** 社區管委會主委 (JJ)  
**目標：** 建立完整的社區管理辦法文件體系，提供管委會決議及總幹事管理使用

---

## 二、工作目錄結構

```
/Users/jesse/Documents/0_社區管理/                    ← 主工作目錄（持久保存）
│
├── CLAUDE.md                                         ← 本說明文件
├── index.html                                        ← 管理辦法總索引（瀏覽器開啟）
│
├── 00(114年正式版)和境心見住戶管理規約.pdf             ← 社區規約原始文件（27頁，21條）
├── 和境心見社區-管理辦法大綱草擬.pdf                   ← 管理辦法框架大綱
│
├── 和境心見社區-門禁磁控與Etag條碼管理辦法(草擬).md
├── 和境心見社區-健身房使用管理辦法(草擬).md
├── 和境心見社區-訪客管制與夜間安寧維護管理辦法(草擬).md
├── 和境心見社區-停車位與車輛管理辦法(草擬).md
├── 和境心見社區-公共空間空調使用管理辦法(草擬).md
├── 和境心見社區-寵物管理辦法(草擬).md
├── 和境心見社區-裝修與施工管理辦法(草擬).md
├── 和境心見社區-防災設備與流程管理辦法(草擬).md
├── 和境心見社區-財務與費用管理辦法(草擬).md
├── 和境心見社區-房屋與車位租賃媒合辦法(草擬).md
├── 和境心見社區-防災設備與流程SOP(草擬).md
├── 和境心見社區-防災設備檢查表(草擬).md
├── 和境心見社區-地下室空間使用管理辦法(草擬).md
└── 和境心見社區-違規處理與罰則辦法(草擬).md
```

### Bash 對應路徑（Claude 工作環境）

| 用途 | 使用者路徑 | Bash 路徑 |
|------|-----------|-----------|
| 主工作目錄 | `/Users/jesse/Documents/0_社區管理/` | `/sessions/amazing-quirky-dijkstra/mnt/0_社區管理/` |
| 暫存輸出目錄 | (outputs folder) | `/sessions/amazing-quirky-dijkstra/mnt/outputs/` |
| Skills 目錄 | (read-only) | `/sessions/amazing-quirky-dijkstra/mnt/.claude/skills/` |

---

## 三、管理辦法文件清單（共 14 份）

| # | 文件名稱 | 狀態 | 類別 | 檔案名稱 |
|---|---------|------|------|---------|
| 1 | 門禁磁控與Etag條碼管理辦法 | 草擬 | 門禁安全 | `和境心見社區-門禁磁控與Etag條碼管理辦法(草擬).md` |
| 2 | 健身房使用管理辦法 | 草擬 | 公共設施 | `和境心見社區-健身房使用管理辦法(草擬).md` |
| 3 | 訪客管制與夜間安寧維護管理辦法 | 草擬 | 門禁安全 | `和境心見社區-訪客管制與夜間安寧維護管理辦法(草擬).md` |
| 4 | 停車位與車輛管理辦法 | 草擬 | 停車管理 | `和境心見社區-停車位與車輛管理辦法(草擬).md` |
| 5 | 公共空間空調使用管理辦法 | 草擬 | 公共設施 | `和境心見社區-公共空間空調使用管理辦法(草擬).md` |
| 6 | 寵物管理辦法 | 草擬 | 住戶規範 | `和境心見社區-寵物管理辦法(草擬).md` |
| 7 | 裝修與施工管理辦法 | 草擬 | 住戶規範 | `和境心見社區-裝修與施工管理辦法(草擬).md` |
| 8 | 防災設備與流程管理辦法 | 草擬 | 防災安全 | `和境心見社區-防災設備與流程管理辦法(草擬).md` |
| 9 | 財務與費用管理辦法 | 草擬 | 財務管理 | `和境心見社區-財務與費用管理辦法(草擬).md` |
| 10 | 房屋與車位租賃媒合辦法 | 草擬 | 住戶規範 | `和境心見社區-房屋與車位租賃媒合辦法(草擬).md` |
| 11 | 防災設備與流程SOP | 草擬 | 防災安全 | `和境心見社區-防災設備與流程SOP(草擬).md` |
| 12 | 防災設備檢查表 | 草擬 | 防災安全 | `和境心見社區-防災設備檢查表(草擬).md` |
| 13 | 地下室空間使用管理辦法 | 草擬 | 公共安全 | `和境心見社區-地下室空間使用管理辦法(草擬).md` |
| 14 | 違規處理與罰則辦法 | 罰則 | 罰則 | `和境心見社區-違規處理與罰則辦法(草擬).md` |

---

## 四、建立新管理辦法文件（.md）

### Markdown 文件標準格式

```markdown
# 和境心見社區 — OO管理辦法（草擬）

**制定日期：** 2026.04.26
**版本：** v0.1（草擬）

---

## 第一章 總則

### 第一條（目的）

一、...
二、...

### 第二條（適用範圍）

...


─── 第二章 ... ───
```

### 命名規則
- **格式：** `和境心見社區-{辦法名稱}({狀態}).md`
- **狀態標示：** 目前統一使用 `(草擬)`；正式通過後改為無括號標示
- **儲存位置：** 直接存入 `/Users/jesse/Documents/0_社區管理/`

### 章節標題格式規定
- 章節標題使用 `─── 第X章 XXX ───` 格式
- 章節標題前後**必須各有兩行空白行**，不可緊接上文
- 新增文件後若格式有誤，執行下方修正腳本

### 章節標題格式批次修正腳本

```python
import os, re

workspace = '/sessions/amazing-quirky-dijkstra/mnt/0_社區管理'
md_files = [f for f in os.listdir(workspace) if f.endswith('.md') and f != 'CLAUDE.md']
section_pattern = re.compile(r'^─── .+ ───\s*$')

for fname in sorted(md_files):
    path = os.path.join(workspace, fname)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    changed = False
    for line in lines:
        if section_pattern.match(line.rstrip('\n')):
            while new_lines and new_lines[-1].strip() == '':
                new_lines.pop()
            new_lines.append('\n')
            new_lines.append('\n')
            new_lines.append(line)
            changed = True
        else:
            new_lines.append(line)
    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f'✓ 已修正：{fname}')
```

---

## 五、建立 HTML 索引頁（index.html）

`index.html` 放在主工作目錄，用瀏覽器開啟即可查閱所有管理辦法。

### index.html 功能
- 列出全部 14 份管理辦法，點擊名稱在頁面內彈出視窗顯示內容（GitHub Pages）
- 本機 `file://` 開啟時，點擊名稱會另開新分頁顯示 `.md` 檔案
- 支援搜尋篩選、依狀態過濾（草擬／正式／罰則）
- 中文介面，樣式簡潔

### index.html 篩選按鈕規則
- **全部**：顯示所有文件
- **草擬**：一般管理辦法（status: "草擬"）
- **正式**：已通過管委會決議（status: "正式"）
- **罰則**：違規處理與罰則類文件（status: "罰則"，badge 顯示紅色）
- **不設「草案」按鈕**：所有文件統一為草擬

### 新增文件至 index.html 的步驟
1. 在 `docs` 陣列新增一筆物件：
```javascript
{ num:15, name:"文件名稱", file:"檔案名稱.md", category:"類別", status:"草擬", version:"v0.1" }
```
2. 更新 header 的文件總數
3. 同步更新本 CLAUDE.md 的文件清單

### 更新 index.html 的時機
每次新增、修改或刪除管理辦法文件後，同步更新 `index.html`。

---

## 六、GitHub 版控

### 遠端 Repository
- **名稱：** `hejingxingjian-regulations`
- **網址：** `https://github.com/jesse994a-cell/hejingxingjian-regulations`
- **GitHub Pages 網址：** `https://jesse994a-cell.github.io/hejingxingjian-regulations/`

### 標準 Push 流程

```bash
cd /Users/jesse/Documents/0_社區管理
git add .
git commit -m "說明本次變更內容"
git push
```

### .gitignore 規則
- `*.pdf`：PDF 原始文件不納入版控（體積大）
- `.DS_Store`、`Thumbs.db`：系統檔案排除

### 注意事項
- `git add .` 可正確處理中文檔名（勿用 `*.md` glob，Shell 不一定展開中文檔名）
- GitHub Pages 上 index.html 可用彈出視窗瀏覽 .md；本機 `file://` 則另開新分頁

---

## 七、違規罰則辦法說明

### 法律限制（重要）
- 管委會**不能直接開罰鍰**，需依規約經區分所有權人會議決議後方具法律效力
- 管委會**不得**自管理費扣抵、鎖車、斷水電等方式強制執行
- 住戶拒繳罰款，得提起民事訴訟

### 罰則文件特殊設定
- `status: "罰則"`（非草擬），index.html 中顯示紅色 badge
- 寵物不落地、進出公共區域等罰款條款暫不納入，避免爭議

### 主要罰款金額（參考基準）
| 違規類型 | 首次 | 再次 |
|---------|------|------|
| 佔用他人停車格 | 500 元 | 1,000 元 |
| 車格同停汽機車 | 500 元 | 1,000 元 |
| 非指定區域充電 | 1,000 元 | 2,000 元 |
| 地下室堆物（逾期） | 500 元/日 | 500 元/日 |
| 走廊堆物（逾期） | 500 元/日 | 500 元/日 |
| 超時施工 | 1,000 元 | 2,000 元 |
| 未申報施工 | — | 2,000 元 |

---

## 八、常見問題排除

### Q: .md 文件在哪裡開啟？
A: 本機用任何 Markdown 閱讀器（VS Code、Typora、Obsidian）或透過 `index.html` 點擊開啟；GitHub Pages 上直接在瀏覽器內閱讀。

### Q: 如何新增一份管理辦法？
A: 1）在主工作目錄建立 `.md` 文件；2）更新 `index.html` 的 docs 陣列與文件總數；3）更新本 CLAUDE.md 的清單；4）執行格式修正腳本確認章節標題間距正確；5）git push。

### Q: 文件狀態如何管理？
A: 在文件標題及 index.html 中標示（草擬），正式通過後修改標題並更新索引。

### Q: GitHub Push 失敗怎麼辦？
A: 確認已 `git add .`（有 commit 才能 push）；若出現 `src refspec main does not match`，表示尚未 commit。

---

*最後更新：2026-04-26*
