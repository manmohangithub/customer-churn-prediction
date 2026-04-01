import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# =========================
# LOAD DATA
# =========================
df = pd.read_excel("Telco_customer_churn.xlsx")

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "")

print("Columns:", df.columns)

# =========================
# DROP UNNECESSARY COLUMNS
# =========================
drop_cols = [
    "CustomerID", "Count", "Country", "State", "City",
    "ZipCode", "LatLong", "Latitude", "Longitude",
    "ChurnLabel", "ChurnScore", "CLTV", "ChurnReason"
]

df = df.drop(columns=[col for col in drop_cols if col in df.columns])

# =========================
# HANDLE MISSING VALUES (CORRECT WAY)
# =========================
num_cols = df.select_dtypes(include=['int64','float64']).columns
cat_cols = df.select_dtypes(include=['object','string']).columns

df[num_cols] = df[num_cols].fillna(0)
df[cat_cols] = df[cat_cols].fillna("Unknown")

# =========================
# FIX TOTAL CHARGES
# =========================
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(0)
else:
    df["TotalCharges"] = df["MonthlyCharges"] * df["TenureMonths"]

# =========================
# FEATURE SELECTION (BEST FOR THIS DATASET)
# =========================
selected_features = [
    'TenureMonths',
    'MonthlyCharges',
    'TotalCharges',
    'Contract',
    'InternetService',
    'PaymentMethod',
    'OnlineSecurity',
    'TechSupport'
]

selected_features = [col for col in selected_features if col in df.columns]

print("Using features:", selected_features)

# =========================
# TARGET
# =========================
if "ChurnValue" not in df.columns:
    raise Exception("❌ ChurnValue column not found")

X = df[selected_features]
y = df["ChurnValue"]

# =========================
# ENCODING
# =========================
encoders = {}
for col in X.select_dtypes(include="object").columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

# =========================
# TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# MODEL (OPTIMIZED RANDOM FOREST)
# =========================
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# EVALUATION
# =========================
y_pred = model.predict(X_test)

print("\n🔥 MODEL PERFORMANCE")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# =========================
# SAVE FILES
# =========================
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(encoders, open("encoders.pkl", "wb"))
pickle.dump(selected_features, open("features.pkl", "wb"))

print("\n✅ Model trained and saved successfully!")