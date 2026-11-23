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
- `narrator.md` — แนวทางและเสียงผู้บรรยาย
- `art-direction.md` — สไตล์ภาพ ชุดสี prompt ฐาน
- `characters/`, `locations/` — sheet + prompt ภาพ
- `episodes/epXX/` — `EPxx_MASTER_SHOT_BREAKDOWN_vX.md` (รูปแบบเดียวกับสยามสัมปัตติ)

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
- 2026-11-21: เจน v3 ทั้ง 3 คน (คำบรรยายหน้าไทยละเอียด) — หน้าไทยชัดขึ้น · Drive: [SANO v3](https://drive.google.com/file/d/1RAMjuRpU81KBVSWfQX5mi0PuA6FTbCpc/view) · [KULA v3](https://drive.google.com/file/d/12UjnYcgUPVEFk_7m4l8cSkDe2ars1aFv/view) · [PRINCE v3](https://drive.google.com/file/d/1RFJVZIEoVI7pLoGc3tGFyAokeNqUdKfd/view)
- 2026-11-21: พระวิจิตรจินดา v4 (ยังไม่ผ่าน) → v5 หน้าไทยชัด · Drive: [PRINCE v5](https://drive.google.com/file/d/1DyZxqhyHREHAcEz9HNUqCZ8CJJcpmfW5/view)
- 2026-11-21: กุลา v4 หน้าไทยชัด · Drive: [KULA v4](https://drive.google.com/file/d/12pqwgm_weqxR_iYdofUNCszl5iYl6q0V/view)
- 2026-11-21: 🔒 **Visual Lock ตัวละครหลัก** — โสนน้อย v3 · กุลา v3 · พระวิจิตรจินดา v5
- 2026-11-21: เจนลุคอื่นตัวละครหลัก 13 ลุค + ตัวละครรอง 14 ภาพ (~276 เครดิต รวมเจนซ้ำ) อัปขึ้น Drive ครบ — รายการใน `characters/README.md` · ลบภาพที่ไม่ได้เลือกแล้ว (ย้ายไปถังขยะ Drive)
- 2026-11-21: แก้กุลา 3 ลุคให้หน้าตรง v3 + วิไลทรงมหาดไทย · 🔒 **Visual Lock สถานที่ 17 ภาพ** (`locations/README.md`) · prompt รอบนี้ `characters/prompts/batch_2026-11-21_b.json`
- 2026-11-21: EP1 Master Shot Breakdown v0.1 (รูปแบบเดียวกับสยามสัมปัตติ, มีผู้บรรยาย, 8 ซีเควนซ์ 51 ช็อต, 10:43 นาที) — `episodes/ep01/` · Drive [EP01](https://drive.google.com/drive/folders/1-zn-WRrtb_tttJqBD_Y0BygL_e1Y76nH)
- 2026-11-21: EP1 v0.2 — ผู้บรรยายแบบเบา (VO 5 จุด) เสียงหญิงเล่านิทาน (`narrator.md`)
- 2026-11-21: ✅ อนุมัติลำดับเวลา EP1 · ออกแบบเสียงผู้บรรยาย "Sano Noi Narrator" (`fDxR49QfNQOv3db3QlJY`) · ยืนยันตารางคำอ่าน (`narrator.md`) · 🔒 เพิ่มสถานที่ EP1 อีก 4 แห่ง (ห้องประสูติ สวนในฝัน เมือง/ประตูนพรัตน์ v2)
- 2026-11-21: เจนภาพต้นทาง EP1 SQ01 SH001–005 v1 (~61 เครดิต) อัปขึ้น Drive `EP01/`
- 2026-11-21: SQ01 v2 (ลบปราสาท/ธงในป่า + เงาพญานาค) · ทดลอง motion Grok vs MiniMax H3 (`tools/kie_video.py`) · เจนภาพต้นทาง SQ02 SH001–006 v1 อัปขึ้น Drive `EP01/`
- 2026-11-21: ✅ SQ02 อนุมัติ · ✅ Grok เป็นโมเดล motion หลัก · เจนภาพต้นทาง SQ03 (8 ภาพ, ~130 เครดิต รวมเจนซ้ำ 2 ภาพ) อัปขึ้น Drive `EP01/`
- 2026-11-21: ✅ SQ03 อนุมัติ · เจนภาพต้นทาง SQ04 (7 ช็อต + สถานที่ใหม่ ท้องพระโรงโรมวิสัย, ~150 เครดิต รวมเจนซ้ำ 2) อัปขึ้น Drive
- 2026-11-21: ✅ SQ04 อนุมัติ (SH003 v2 โสนน้อยอยู่คนเดียว) · เจนภาพต้นทาง SQ05 (3 ช็อต, ~54 เครดิต รวมเจนซ้ำ 1) อัปขึ้น Drive
- 2026-11-21: ✅ SQ05 อนุมัติ · เจนภาพต้นทาง SQ06 (7 ช็อต, ~108 เครดิต รวมเจนซ้ำ 1) อัปขึ้น Drive
- 2026-11-21: ✅ SQ06 อนุมัติ · เจนภาพต้นทาง SQ07 (7 ช็อต, ~143 เครดิต รวมเจนซ้ำ/ลองใหม่ 3) อัปขึ้น Drive
- 2026-11-21: ✅ SQ07 อนุมัติ · เจนภาพต้นทาง SQ08 (11 ภาพ, ~145 เครดิต) — **ภาพต้นทาง EP1 ครบทั้ง 8 ซีเควนซ์** (KIE เหลือ ~85,500 เครดิต)
- 2026-11-21: ✅ ภาพต้นทาง EP1 อนุมัติครบ · เริ่มเจน motion EP1 ด้วย Grok 720p (52 คลิป, prompt `episodes/ep01/prompts/MOTION_GROK_v1.json`) · เจน VO ผู้บรรยาย 5 จุด จุดละ 2 เทค อัปขึ้น Drive `EP01/VO_NARRATOR/` (`tools/` ไม่ต้องใช้ — สั่งผ่าน ElevenLabs connector)
- 2026-11-21: QC motion ครบ 54 คลิป — เจนซ้ำ 3 คลิป: SQ03 SH003 (บ้านบิดรูป → v2 ✅), SQ07 SH004 (หน้ากุลาเพี้ยน → v2 ✅), SQ04 SH005 (ท้าวหัสวิชัยยิ้ม → v2 ยังยิ้ม → **Grok v3 ✅**, มีสำรอง MiniMax H3 v3) · prompt `episodes/ep01/prompts/MOTION_REDO_v2_v3.json`
- 2026-11-21: ตัดหยาบ EP1 (`episodes/ep01/roughcut_ep01.py`) — รายซีเควนซ์ SQ01–08 + เต็มตอน **10:39** (720p, VO take1 + เสียง Grok เป็นไกด์) ส่งให้เจ้าของงานทางแชต (วิดีโอเกิน 3 MB อัป Drive เอง → `EP01/`)
- 2026-11-21: 🔒 ล็อกเสียงรอบ 2 — กุลา 1 · พระวิจิตรจินดา 1 · ท้าวหัสวิชัย 1 · นางเกษณี 1 (เซฟเข้าคลัง ElevenLabs) · เลือกเสียงตัวประกอบ 5 ตัวจากคลัง (`voices.md`) · เจนบทพูด EP1 ครบ 22 บรรทัด × 2 เทค อัปขึ้น Drive `EP01/DIALOGUE/` (`episodes/ep01/EP01_DIALOGUE.md`)
- 2026-11-21: เพิ่มคำอ่าน โสน = สะ-โน๋ (TTS "สะโหน") · เจน VO③④⑤ + D07 ใหม่ · ✅ เลือกเทค VO ครบ ①t1 ②t1 ③v2t1 ④v2t2 ⑤v2t1 · D07 v2 take1 · ย้ายไฟล์เก่า/ไม่เลือกไปถังขยะ Drive
- 2026-11-21: ตัดหยาบ v2 (`episodes/ep01/roughcut_ep01_v2.py`) — เสียง ElevenLabs ทั้งหมด (VO ตามที่เลือก + บทพูด take1 ทุกบรรทัด, เสียง Grok ลดเหลือ 12% เป็นบรรยากาศ) 10:39 ส่งทางแชต
- 2026-11-22: เตรียมย้ายไป PC — ส่งคลิป motion EP1 ตัวจริง 54 คลิป (zip ราย SQ) ให้เจ้าของงานเก็บใน Drive `EP01/MOTION/` · `tools/` อ่าน `KIE_API_KEY` บน PC ได้ · เพิ่มวิธีทำงานบน PC ใน `CLAUDE.md`
- 2026-11-23: เจ้าของงานเก็บคลิป motion EP1 ไว้บน PC ที่ `D:\PHI_JUK_STORY\002_SANO_NOI_RUEAN_NGAM\EP01\MOTION` → ต้องอัปขึ้น Drive [`EP01/MOTION/`](https://drive.google.com/drive/folders/1Xq4nb53dZ5TxyW7vruIfYFQvvGzAmfHS) (สร้างโฟลเดอร์ไว้แล้ว) เพื่อสำรอง + ให้ iPad/cloud ใช้ได้
- **ขั้นต่อไป:** เจ้าของงานดู rough cut v2 → บอกบรรทัดที่อยากใช้ take2/เจนใหม่ (ที่เหลือใช้ take1 แล้วลบ take2 จาก Drive) → ตัดต่อจริงใน CapCut (PC) — จูนจังหวะปาก ดนตรี SFX ซับ → บท EP2
