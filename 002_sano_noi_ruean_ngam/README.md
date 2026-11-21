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
- 2026-11-21: ✅ อนุมัติ art direction · ร่าง character sheet ตัวละครหลัก 3 คน (`characters/`)
- 2026-11-21: ร่าง character sheet ตัวละครรอง 12 รายการ (`characters/supporting.md`)
- 2026-11-21: เจน Master Look v1 ทั้ง 3 คนผ่าน KIE (`tools/kie_image.py`, gpt-image-2-6/sunburst 2K 16:9, ~8 เครดิต/ภาพ) — ยังไม่ได้อัปขึ้น Drive (ไฟล์ PNG ~5 MB เกินขีดจำกัดของ connector) · ข้อสังเกต: ใบหน้าโสนน้อยและกุลาออกไปทางตะวันตก, โสนน้อยใส่รองเท้าส้นสูง, ปาน/แผลเป็นมองไม่เห็น
- 2026-11-21: เจน v2 โสนน้อย/กุลา (หน้าไทยขึ้นบ้าง รองเท้าแบน เห็นปาน พื้นหลังเรียบ) · อัปขึ้น Drive `02_CHARACTERS` เป็น JPG q95: [SANO v2](https://drive.google.com/file/d/1k__9fisO349cbw8Asd8P6k2xSNSB0vH2/view) · [KULA v2](https://drive.google.com/file/d/1CHaTLP5DNaqzQAm-VCJh3a61nh8g1xRf/view) · [PRINCE v1](https://drive.google.com/file/d/1CpN0QW49W6hf9WpELrq3rsbpFDk33BEA/view)
- ข้อจำกัด: connector อัปขึ้น Drive ได้ ~3 MB/ไฟล์ → อัปภาพเป็น JPG q95 (~1.5–1.8 MB) แทน PNG
- **ขั้นต่อไป:** อนุมัติ Master Look ตัวละครหลัก (หรือแก้ v3) → อนุมัติ (Visual Lock) → ลุคอื่น + ตัวละครรอง → location sheet → character sheet + location sheet (gpt-image 2.6) → บท EP1
