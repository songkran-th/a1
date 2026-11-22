# PHI JUK STORY — บรีฟกลาง

ค่าย production เล่าเรื่อง (ละคร เรื่องเล่า เรื่องลี้ลับ วรรณกรรมไทย) ทำด้วย AI
เจ้าของงานสั่งงานได้ทั้งจาก PC (Claude Desktop) และ iPad (Claude Code บน cloud)

## ที่เก็บงาน
- **GitHub (repo นี้)**: งานเขียนทั้งหมด — story bible, บท, character/location sheet, prompt, สถานะงาน
- **Google Drive** `My Drive/PHI_JUK_STORY/`: ไฟล์ใหญ่ — ภาพ วิดีโอ เสียง คลิปที่ตัดต่อเสร็จ
- ใช้ **เลขนำหน้าเดียวกัน** ทั้งสองที่ เช่น `002_SANO_NOI_RUEAN_NGAM` (Drive) ↔ `002_sano_noi_ruean_ngam/` (repo)
- ดัชนี production ทั้งหมดอยู่ที่ `productions.md`
- ห้าม commit ไฟล์ภาพ/วิดีโอ/เสียงเข้า repo (`.gitignore` กันไว้แล้ว) — อัปขึ้น Drive แล้วจดลิงก์ไว้ใน README ของเรื่องแทน

## เริ่มงานทุกครั้ง
1. อ่าน `productions.md` และ `README.md` ของเรื่องที่จะทำ (ส่วน "สถานะล่าสุด")
2. ทำงานต่อจากขั้นตอนถัดไปที่จดไว้
3. จบงาน: อัปเดต "สถานะล่าสุด" ใน README ของเรื่อง แล้ว commit + push

## House Style ของ Phi Juk (ใช้ร่วมทุกเรื่อง)
- **Thai Cinematic Epic Painterly Fantasy** ฝีแปรงพอดี · **16:9** — ใช้ใน 000 ปทีปปรโลก, 001 สยามสัมปัตติ (เรือเที่ยวสุดท้าย) และ 002
- แต่ละเรื่องคงฐานสไตล์นี้ แล้วกำหนดโทนสี/แสงของตัวเองใน `art-direction.md` ของเรื่อง
- **Visual Lock:** อนุมัติภาพอ้างอิงตัวละคร/prop/สถานที่ก่อน แล้วใช้เป็น reference ทุกช็อต
- **Color/Lighting Baseline** ต่อสถานที่ · แสงเวทมนตร์/แสงพิเศษเป็น local spill ไม่ย้อมทั้งฉาก
- ห้ามเพิ่มตัวละคร วัตถุ ตัวหนังสือ ซับในภาพ หรือเวทมนตร์ที่ไม่มีในบท
- ตั้งชื่อช็อต: `EP01_SQ05_SH008_..._v1` (ตอน / ซีเควนซ์ / ช็อต / เวอร์ชัน)
- Motion prompt (image-to-video) ปิดท้ายด้วยประโยคล็อก เช่น
  `Lock the composition, identity, proportions, wardrobe, props and painterly palette of frame one. No music, text, subtitles, extra characters or objects.`

## มาตรฐาน production (ค่าเริ่มต้น เว้นแต่ README ของเรื่องระบุอื่น)
- ภาษาในบท/บทพูด: ไทย
- ความยาวต่อตอน: 10–14 นาที
- ถ้าดัดแปลงจากเรื่องที่มีอยู่แล้ว ให้ยึดเนื้อเรื่องเดิม ไม่แต่งเหตุการณ์หลักขึ้นใหม่ (ใช้ skill `kendo-drama-novel`)
- เครื่องมือแต่ละเรื่องอาจต่างกัน — ดูที่ README ของเรื่อง

## ทำงานบน PC (Claude Desktop / Claude Code ในเครื่อง)
- repo: `git clone https://github.com/songkran-th/a1.git` แล้ว `git checkout claude/zealous-albattani-yx19ld` (branch งานหลักตอนนี้) · เริ่มงาน `git pull` · จบงาน commit + push
- KIE บน PC: ตั้ง environment variable `KIE_API_KEY` ในเครื่อง (ห้าม commit คีย์) — `tools/kie_image.py`/`kie_video.py` อ่านเอง · บน cloud ไม่ต้องตั้ง (proxy ใส่ให้)
- ต้องมี Python 3 + ffmpeg ในเครื่อง (ใช้กับสคริปต์ตัดหยาบ `episodes/*/roughcut_*.py` ต้องแก้ path ในสคริปต์ให้ชี้โฟลเดอร์ในเครื่อง)
- ไฟล์ภาพ/เสียง/คลิปใช้จาก Google Drive for desktop (`My Drive/PHI_JUK_STORY/`) — บน PC อ่าน/เขียนไฟล์ใหญ่ได้ตรงๆ ไม่ติดขีดจำกัด 3 MB
- ElevenLabs / Google Drive connector ใช้ได้ทั้งสองที่ (ผูกกับบัญชี)

## ข้อจำกัด
- อัปไฟล์ขึ้น Drive ผ่าน connector ได้ ~3 MB ต่อไฟล์ → ภาพให้อัปเป็น JPG คุณภาพ 95 (ภาพ 2K ~1.5–1.8 MB) · ไฟล์ใหญ่กว่านั้น (วิดีโอ เสียง) เจ้าของงานอัปเอง
- เจนภาพผ่าน KIE ด้วย `tools/kie_image.py` (cloud environment "a1" เก็บ API key ไว้ · บน PC ใช้ `KIE_API_KEY`)
- การตัดต่อใน CapCut ทำได้บน PC เท่านั้น (cloud แก้โปรเจกต์ CapCut ไม่ได้)
