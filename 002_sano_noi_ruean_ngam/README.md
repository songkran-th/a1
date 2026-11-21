# 002 — โสนน้อยเรือนงาม (SANO NOI RUEAN NGAM)

## สเปก production
| รายการ | ค่า |
|---|---|
| ประเภท | วรรณคดี / นิทานพื้นบ้านไทย — **เล่าใหม่ให้ร่วมสมัย** คงฉากยุคโบราณและเหตุการณ์หลัก ดู `story/treatment-modern.md` |
| สัดส่วนภาพ | **16:9 แนวนอน** |
| ความยาวต่อตอน | 10–14 นาที |
| จำนวนตอน | **8 ตอน** (2 ภาค × 4 ตอน) — 🔒 ล็อกแล้ว ดู `story/treatment-modern.md` |
| ภาพ | gpt-image 2.6 |
| วิดีโอ | Grok หรือ MiniMax ผ่าน KIE |
| ตัดต่อ | CapCut (บน PC) |

## Google Drive
`My Drive/PHI_JUK_STORY/002_SANO_NOI_RUEAN_NGAM/`
- [โฟลเดอร์หลัก](https://drive.google.com/drive/folders/1AMfJAephlSCuK-ISDSCxRdoo9stULDSn)
- `01_REFERENCE/` ต้นฉบับ ภาพอ้างอิง · `02_CHARACTERS/` · `03_LOCATIONS/` · `99_EXPORT/`
- โฟลเดอร์ `EP01/`, `EP02/` … สร้างตอนเริ่มผลิตแต่ละตอน

## โครงไฟล์ใน repo
- `story/treatment-modern.md` — **ฉบับเล่าใหม่ (ใช้ตัวนี้เป็นหลัก)**
- `story/synopsis.md` — ลำดับเรื่องตามต้นฉบับเต็ม (34 ข้อ)
- `art-direction.md` — สไตล์ภาพ ชุดสี prompt ฐาน
- `characters/`, `locations/` — sheet + prompt ภาพ
- `episodes/epXX/` — `script.md`, `prompts.md`

## สถานะล่าสุด
- 2026-11-21: สร้างโฟลเดอร์ Drive + repo, ร่างเรื่องย่อและแผน 6 ตอน
- 2026-11-21: เขียน treatment v1 (6 ตอน) จากข้อมูลไม่ครบ
- 2026-11-21: ได้ต้นฉบับเต็ม (PDF ใน `01_REFERENCE`) → เขียน synopsis ใหม่ + **treatment v2: 12 ตอน / 2 ซีซัน**
- 2026-11-21: treatment **v3 — 8 ตอน 🔒 ล็อกเรื่อง**
- 2026-11-21: v3.1 — design bible เรือนไม้โสน (`locations/ruean-sano.md`)
- 2026-11-21: ร่าง art direction (`art-direction.md`) — ต่อยอดสไตล์ปทีปปรโลก รออนุมัติ
- **ขั้นต่อไป:** อนุมัติ art direction → character sheet + location sheet (gpt-image 2.6) → บท EP1
