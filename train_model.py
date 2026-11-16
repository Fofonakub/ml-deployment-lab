
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# โหลดข้อมูลราคาบ้าน
data = fetch_california_housing(as_frame=False)
X, y = data.data, data.target

# แบ่งข้อมูล Train และ Test
Xtr, Xte, ytr, yte = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# สร้างและฝึกโมเดล
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(Xtr, ytr)

# บันทึกโมเดล
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")

print("บันทึกโมเดลเรียบร้อยที่ model/model.pkl")
