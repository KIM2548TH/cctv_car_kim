import mongoengine as me
import datetime


class ParkingArea(me.Document):
    """
    เก็บข้อมูลภาพรวมและสรุปจำนวนรถของแต่ละลานจอด
    ถูกออกแบบให้เบาและรวดเร็วสำหรับการ Query เพื่อไปพล็อตสรุปลงบนแอปแผนที่
    """
    # ชื่อหรือรหัสโซนลานจอด (เช่น "Zone A", "Parking Front")
    name = me.StringField(required=True)
    
    # รายละเอียดพื้นที่เพิ่มเติม (เอาไว้แสดงผลบนเว็บ)
    description = me.StringField()
    
    # รหัสกล้องที่ดูแลพื้นที่นี้ (ลิงก์ไปยัง Camera Model สำหรับดึงสตรีมสด)
    camera_id = me.StringField(required=True)

    # --- ข้อมูลสรุปสถานะช่องจอด (อัปเดตจาก ML/กล้อง) ---
    # จำนวนที่จอดทั้งหมดกี่ช่อง
    total_slots = me.IntField(default=0, min_value=0)
    
    # จำนวนลานจอดที่ยังว่างอยู่
    available_slots = me.IntField(default=0, min_value=0)
    
    # จำนวนลานจอดที่มีรถจอดอยู่แล้ว
    occupied_slots = me.IntField(default=0, min_value=0)
    
    # จำนวนรถที่ตีความว่า "จอดผิดกฎ" หรือจอดซ้อนคัน
    violation_slots = me.IntField(default=0, min_value=0)

    # บันทึกเวลาที่ข้อมูลเปลี่ยนล่าสุด
    created_date = me.DateTimeField(default=datetime.datetime.now)
    updated_date = me.DateTimeField(default=datetime.datetime.now)

    meta = {
        "collection": "parking_areas",
        "indexes": [
            # camera_id เป็น unique key — 1 กล้องมีได้แค่ 1 parking zone
            {"fields": ["camera_id"], "unique": True},
            "name",
        ]
    }
